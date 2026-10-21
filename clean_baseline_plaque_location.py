"""Where does plaque appear at FU in patients with a clean baseline (BL ct_cag_sis == 0 and ct_cag_sss == 0)?

    python CGPS_data/clean_baseline_plaque_location.py [--bl BL_FILE] [--fu FU_FILE]

Uses BL_PATH / FU_PATH from cgps_stats.py unless overridden. Prints aggregate tables only (small
counts suppressed as in cgps_stats.py); nothing is written to disk.

Developed plaque: FU ct_cag_sis > 0. A segment has plaque at FU when its decoded stenosis is minimal
or worse. Segments are grouped into LM, the three trunks (TRUNKS) and the side
branches. Tables:
1. cohort: clean baseline, paired with FU, developed plaque;
2. share of all FU plaque segments (and of the summed stenosis grades) in each unit;
3. share of the patients who developed plaque that have plaque in each unit (adds up to > 100 %),
   and how many have plaque only outside the three trunks.
Everything is shown for the whole clean cohort and for the part with BL segment reads (about half of
the BL patients have no segment reads but SIS/SSS recorded as 0, see clean_baseline_count.py).
"""
from __future__ import annotations

import argparse

import pandas as pd

from cgps_stats import BL_PATH, FU_PATH, SEGMENTS, count, decode_segments, load, num, pct

TRUNKS = {"LAD": ("plad", "mlad", "dlad"), "CX": ("pcx", "mcx", "dcx"), "RCA": ("prca", "mrca", "drca")}
SIDE_BRANCHES = ("d1", "d2", "im", "om1", "om2", "pda", "pla")
UNITS = {"LM": ("lm",), **{f"{v} trunk": segs for v, segs in TRUNKS.items()},
         **{s.upper(): (s,) for s in SIDE_BRANCHES}}
GROUPS = {"three trunks (LAD + CX + RCA)": sum(TRUNKS.values(), ()), "LM": ("lm",), "side branches": SIDE_BRANCHES}


def table(rows, header):
    print("| " + " | ".join(header) + " |")
    print("|" + "---|" * len(header))
    for r in rows:
        print("| " + " | ".join(str(x) for x in r) + " |")
    print()


def report(title, F):
    """F: decoded FU rows of the clean-baseline patients that developed plaque."""
    seg_cols = {s: f"ct_cag_{s}_stenosis" for s in SEGMENTS if f"ct_cag_{s}_stenosis" in F}
    grade = pd.DataFrame({s: num(F[c]) for s, c in seg_cols.items()})
    plaque = (grade >= 1).astype(int)
    n_pat = len(F)
    total_seg, total_grade = int(plaque.to_numpy().sum()), int(grade.where(grade >= 1, 0).to_numpy().sum())

    print(f"## {title}\n")
    print(f"patients who developed plaque: {count(n_pat)}; FU plaque segments: {count(total_seg)}; "
          f"summed FU stenosis grades: {count(total_grade)}\n")

    def unit_rows(units):
        rows = []
        for name, segs in units.items():
            segs = [s for s in segs if s in plaque]
            k_seg = int(plaque[segs].to_numpy().sum())
            k_grade = int(grade[segs].where(grade[segs] >= 1, 0).to_numpy().sum())
            k_pat = int(plaque[segs].any(axis=1).sum())
            rows.append((name, count(k_seg), pct(k_seg, total_seg), pct(k_grade, total_grade),
                         count(k_pat), pct(k_pat, n_pat)))
        return rows

    header = ["unit", "plaque segments", "% of plaque segments", "% of stenosis grades",
              "patients with plaque here", "% of patients"]
    print("### per unit\n")
    table(unit_rows(UNITS), header)
    print("### grouped\n")
    table(unit_rows(GROUPS), header)

    trunk_segs = [s for s in GROUPS["three trunks (LAD + CX + RCA)"] if s in plaque]
    in_trunk = plaque[trunk_segs].any(axis=1)
    outside_only = int((~in_trunk).sum())
    print("### patients by where their plaque is\n")
    table([("plaque in at least one trunk", count(int(in_trunk.sum())), pct(int(in_trunk.sum()), n_pat)),
           ("plaque only in LM and/or side branches", count(outside_only), pct(outside_only, n_pat))],
          ["", "n", "% of patients who developed plaque"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bl", default=BL_PATH)
    ap.add_argument("--fu", default=FU_PATH)
    args = ap.parse_args()

    bl = load(args.bl).drop_duplicates("study_id").set_index("study_id")
    fu = load(args.fu).drop_duplicates("study_id").set_index("study_id")
    fu, _ = decode_segments(fu)

    clean = (num(bl["ct_cag_sis"]) == 0) & (num(bl["ct_cag_sss"]) == 0)
    read = bl[[f"ct_cag_{s}_stenosis" for s in SEGMENTS if f"ct_cag_{s}_stenosis" in bl]].notna().any(axis=1)
    ids = clean[clean].index.intersection(fu.index)
    fu_sis = num(fu.loc[ids, "ct_cag_sis"])
    developed = fu_sis[fu_sis > 0].index

    print("## cohort\n")
    n_clean, n_dev = len(ids), len(developed)
    n_clean_read, n_dev_read = int(read.loc[ids].sum()), int(read.loc[developed].sum())
    table([("clean baseline with a FU scan", count(n_clean), count(n_clean_read)),
           ("FU ct_cag_sis recorded", count(fu_sis.notna().sum()), count(fu_sis.notna()[read.loc[ids]].sum())),
           ("developed plaque (FU ct_cag_sis > 0)", count(n_dev), count(n_dev_read)),
           ("% developed plaque", pct(n_dev, n_clean), pct(n_dev_read, n_clean_read))],
          ["", "all clean", "with BL segment reads"])

    report("all clean-baseline patients who developed plaque", fu.loc[developed])
    report("only those with BL segment reads", fu.loc[developed[read.loc[developed].to_numpy()]])


if __name__ == "__main__":
    main()
