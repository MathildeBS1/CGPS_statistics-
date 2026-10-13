# Centerline quality report

Source `/data/kimbr/centerlines_hø_10Y.zip`: 744 cases found (expected 744), 744 read, **744 analysed**, 0 with read errors.

Settings: JOIN_TOL 1.0 mm, DEDUP_TOL 0.01 mm, gap > max(3.0 mm, 5.0x median spacing), numeric labels read as: **raw**.

## How the files were read

Most common parse results (arrays/columns found, which one was used as label):

- 26 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "5:LM", "6:pLAD", "7:mLAD", "8:dLAD", "9:D1", "11:pCx", "12:OM1", "13:LCx", "14:L-PLB", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": 2, "LINES": 1, "POINT`
- 19 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "5:LM", "6:pLAD", "7:mLAD", "8:dLAD", "9:D1", "11:pCx", "12:OM1", "13:LCx", "14:L-PLB", "17:RI", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": 2, "LINES": `
- 15 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "2:mRCA", "3:dRCA", "4:R-PDA", "16:R-PLB", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": 2, "LINES": 1, "POINTS": 1, "POINT_DATA": 1}}`
- 12 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "5:LM", "6:pLAD", "7:mLAD", "8:dLAD", "9:D1", "11:pCx", "12:OM1", "13:LCx", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": 2, "LINES": 1, "POINTS": 1, "POIN`
- 9 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "5:LM", "6:pLAD", "7:mLAD", "8:dLAD", "9:D1", "11:pCx", "12:OM1", "13:LCx", "14:L-PLB", "15:L-PDA", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": 2, "LINES`
- 8 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "5:LM", "6:pLAD", "7:mLAD", "8:dLAD", "9:D1", "11:pCx", "12:OM1", "13:LCx", "14:L-PLB", "15:L-PDA", "17:AL", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": `
- 7 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": 2, "LINES": 1, "POINTS": 1, "POINT_DATA": 1}}`
- 7 files: `{"cell_arrays": [], "field_data": {"segment_names": ["1:pRCA", "2:mRCA", "3:dRCA", "4:R-PDA", "5:LM", "6:pLAD", "7:mLAD", "8:dLAD", "9:D1", "11:pCx", "12:OM1", "16:R-PLB", "24:unlabelled"]}, "label_array": "segment_label", "label_lookup": true, "point_arrays": ["segment_label", "branch"], "vtk_header": ["# vtk DataFile Version 5.1", "vtk output", "BINARY"], "vtk_keywords": {"DATASET": 1, "FIELD": `

## Label values

Raw labels and the segment they were mapped to (`?x` = not recognised, `#n` = number not mapped, empty = unlabelled). **Check this first** - all other numbers depend on it.

| raw_label | mapped_to | n_points |
|---|---|---|
| 24 | #24 | 128875 |
| 24:unlabelled |  | 97270 |
| 8 | #8 | 66883 |
| 9 | #9 | 55125 |
| 16 | #16 | 54599 |
| 12 | #12 | 40886 |
| 1 | #1 | 38509 |
| 4 | #4 | 37315 |
| 2 | #2 | 36691 |
| 3 | #3 | 35645 |
| 7 | #7 | 30427 |
| 13 | #13 | 29715 |
| 8:dLAD | dLAD | 28647 |
| 11 | #11 | 27281 |
| 28 | #28 | 25300 |
| 13:LCx | CX | 24242 |
| 12:OM1 | OM1 | 23011 |
| 10 | #10 | 22958 |
| 1:pRCA | pRCA | 22741 |
| 17 | #17 | 21527 |
| 9:D1 | D1 | 21329 |
| 22 | #22 | 21316 |
| 6 | #6 | 20882 |
| 18 | #18 | 15017 |
| 5 | #5 | 12636 |
| 11:pCx | pCX | 12397 |
| 21 | #21 | 11557 |
| 7:mLAD | mLAD | 11522 |
| 6:pLAD | pLAD | 10215 |
| 14:L-PLB | PLA | 8672 |
| 4:R-PDA | PDA | 8091 |
| 17:RI | IM | 7224 |
| 2:mRCA | mRCA | 6477 |
| 3:dRCA | dRCA | 6205 |
| 19 | #19 | 5948 |
| 16:R-PLB | PLA | 5530 |
| 5:LM | LM | 5096 |
| 10:D2 | D2 | 2509 |
| 20 | #20 | 1813 |
| 15:L-PDA | PDA | 1530 |
| 17:AL | ?AL | 434 |

## Overview per case

| metric | n | mean | min | p5 | q1 | median | q3 | p95 | max |
|---|---|---|---|---|---|---|---|---|---|
| total_mm | 744.0 | 690.2 | 36.6 | 320.2 | 521.9 | 685.4 | 849.5 | 1054.2 | 3645.7 |
| unlabelled_mm | 744.0 | 63.2 | 0.0 | 0.0 | 0.0 | 0.0 | 66.5 | 316.5 | 2446.5 |
| unlabelled_pct | 744.0 | 9.6 | 0.0 | 0.0 | 0.0 | 0.0 | 13.9 | 44.8 | 100.0 |
| n_polylines | 744.0 | 16.0 | 3.0 | 7.0 | 11.0 | 15.0 | 19.0 | 27.0 | 165.0 |
| n_points | 744.0 | 1403.3 | 77.0 | 648.6 | 1059.0 | 1391.0 | 1726.5 | 2144.3 | 7531.0 |
| n_branch_points | 744.0 | 13.1 | 0.0 | 4.0 | 8.0 | 12.0 | 16.0 | 23.0 | 160.0 |
| n_end_points | 744.0 | 18.7 | 4.0 | 9.0 | 14.0 | 18.0 | 22.0 | 30.0 | 168.0 |
| max_degree | 744.0 | 3.1 | 2.0 | 3.0 | 3.0 | 3.0 | 3.0 | 4.0 | 4.0 |
| n_components | 744.0 | 2.8 | 1.0 | 2.0 | 2.0 | 3.0 | 3.0 | 4.0 | 6.0 |
| n_tiny_components | 744.0 | 0.4 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 2.0 | 3.0 |
| n_gaps | 744.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| n_joins | 744.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| overlap_mm | 744.0 | 18.0 | 0.0 | 5.8 | 11.8 | 16.8 | 22.4 | 31.3 | 224.4 |
| median_spacing_mm | 744.0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| max_spacing_mm | 744.0 | 0.7 | 0.5 | 0.6 | 0.6 | 0.7 | 0.7 | 0.8 | 0.8 |
| extent_x | 744.0 | 109.5 | 25.7 | 82.2 | 102.1 | 111.5 | 119.8 | 130.7 | 186.6 |
| extent_y | 744.0 | 93.1 | 29.5 | 67.7 | 84.9 | 94.4 | 103.0 | 113.5 | 125.9 |
| extent_z | 744.0 | 88.9 | 20.6 | 66.0 | 83.0 | 89.8 | 96.7 | 107.5 | 133.0 |
| median_radius | 0.0 |  |  |  |  |  |  |  |  |

Units: total lengths of ~200-800 mm and extents of ~50-150 mm mean mm; much smaller values suggest cm, much larger voxels.

Unlabelled length over all cases: 47046 of 513515 mm (**9.2 %**); cases with any unlabelled length: 250 of 744.

Connected components per case (expect 2: left and right tree):

| components | cases |
|---|---|
| 1 | 9 |
| 2 | 339 |
| 3 | 244 |
| 4 | 118 |
| 5 | 28 |
| 6 | 6 |

## Segments: presence and length (mm)

| segment | cases | % cases | mean | min | p5 | q1 | median | q3 | p95 | max |
|---|---|---|---|---|---|---|---|---|---|---|
| LM | 204 | 27.4 | 12.4 | 2.9 | 5.4 | 8.8 | 11.7 | 15.2 | 20.2 | 48.3 |
| pLAD | 210 | 28.2 | 24.6 | 5.2 | 9.1 | 15.5 | 22.9 | 31.5 | 47.6 | 82.1 |
| mLAD | 194 | 26.1 | 29.8 | 3.9 | 17.8 | 30.0 | 30.4 | 30.7 | 39.8 | 53.3 |
| dLAD | 187 | 25.1 | 76.3 | 1.6 | 11.6 | 52.2 | 80.2 | 103.9 | 127.4 | 147.3 |
| D1 | 193 | 25.9 | 54.0 | 5.0 | 8.7 | 28.4 | 48.8 | 69.9 | 119.9 | 159.5 |
| D2 | 31 | 4.2 | 39.6 | 5.6 | 13.7 | 25.9 | 36.6 | 52.4 | 72.9 | 88.6 |
| IM | 54 | 7.3 | 65.2 | 5.0 | 10.1 | 32.3 | 53.2 | 93.2 | 139.5 | 231.4 |
| pCX | 217 | 29.2 | 28.3 | 3.7 | 10.7 | 21.0 | 26.4 | 33.5 | 51.7 | 84.4 |
| CX | 175 | 23.5 | 69.2 | 3.4 | 13.3 | 46.3 | 70.6 | 93.6 | 118.7 | 137.4 |
| OM1 | 169 | 22.7 | 66.9 | 4.2 | 8.6 | 31.5 | 57.4 | 93.7 | 156.0 | 221.4 |
| pRCA | 242 | 32.5 | 46.9 | 5.5 | 10.8 | 36.5 | 46.0 | 57.4 | 83.4 | 119.3 |
| mRCA | 93 | 12.5 | 34.9 | 4.2 | 10.0 | 31.5 | 37.9 | 42.0 | 51.5 | 66.5 |
| dRCA | 92 | 12.4 | 33.9 | 3.2 | 9.4 | 30.5 | 38.0 | 41.9 | 50.9 | 67.0 |
| PDA | 102 | 13.7 | 46.0 | 4.5 | 8.9 | 20.6 | 29.3 | 46.1 | 91.7 | 971.1 |
| PLA | 180 | 24.2 | 38.5 | 3.6 | 6.7 | 18.0 | 29.1 | 53.9 | 88.0 | 168.3 |
| #1 | 490 | 65.9 | 39.2 | 4.7 | 30.8 | 35.7 | 38.8 | 43.3 | 49.1 | 60.0 |
| #10 | 264 | 35.5 | 42.3 | 4.4 | 7.9 | 18.0 | 34.0 | 56.8 | 105.1 | 174.1 |
| #11 | 490 | 65.9 | 27.5 | 6.6 | 12.9 | 15.5 | 26.5 | 34.8 | 52.8 | 76.3 |
| #12 | 331 | 44.5 | 60.6 | 4.6 | 10.6 | 28.1 | 49.4 | 79.9 | 142.8 | 256.2 |
| #13 | 424 | 57.0 | 34.9 | 2.2 | 9.0 | 23.0 | 33.7 | 46.1 | 64.5 | 86.6 |
| #16 | 433 | 58.2 | 61.9 | 9.3 | 14.2 | 29.5 | 52.2 | 85.2 | 138.9 | 374.5 |
| #17 | 141 | 19.0 | 74.7 | 3.6 | 8.1 | 30.1 | 61.1 | 116.5 | 173.0 | 290.4 |
| #18 | 375 | 50.4 | 19.0 | 3.0 | 5.2 | 8.6 | 13.6 | 22.6 | 47.0 | 260.5 |
| #19 | 161 | 21.6 | 17.4 | 2.5 | 4.9 | 7.4 | 10.7 | 20.0 | 51.0 | 164.4 |
| #2 | 476 | 64.0 | 38.7 | 5.2 | 28.8 | 34.7 | 38.4 | 43.0 | 48.6 | 59.6 |
| #20 | 55 | 7.4 | 15.5 | 3.2 | 5.0 | 6.4 | 11.0 | 16.6 | 42.5 | 78.8 |
| #21 | 210 | 28.2 | 26.7 | 4.2 | 6.5 | 11.8 | 21.3 | 35.8 | 65.9 | 110.8 |
| #22 | 238 | 32.0 | 43.9 | 3.1 | 6.6 | 17.1 | 34.9 | 62.3 | 107.9 | 187.6 |
| #24 | 486 | 65.3 | 127.9 | 4.9 | 16.6 | 67.1 | 116.6 | 175.6 | 276.9 | 801.5 |
| #28 | 184 | 24.7 | 67.2 | 2.7 | 5.8 | 16.8 | 48.3 | 101.4 | 180.6 | 309.8 |
| #3 | 464 | 62.4 | 38.5 | 6.1 | 29.0 | 34.8 | 38.2 | 42.9 | 48.8 | 90.8 |
| #4 | 358 | 48.1 | 51.1 | 8.8 | 18.9 | 33.3 | 48.5 | 63.2 | 92.1 | 157.3 |
| #5 | 480 | 64.5 | 13.1 | 0.5 | 6.0 | 10.0 | 12.6 | 16.0 | 21.5 | 47.2 |
| #6 | 489 | 65.7 | 21.6 | 3.5 | 7.3 | 14.4 | 21.5 | 26.1 | 40.4 | 59.3 |
| #7 | 488 | 65.6 | 31.3 | 6.7 | 14.0 | 30.0 | 30.5 | 31.2 | 48.9 | 57.4 |
| #8 | 413 | 55.5 | 80.8 | 1.1 | 20.1 | 55.6 | 83.6 | 108.0 | 130.9 | 202.8 |
| #9 | 432 | 58.1 | 62.3 | 4.7 | 12.9 | 31.9 | 55.1 | 81.6 | 142.4 | 282.0 |
| ?AL | 4 | 0.5 | 52.7 | 20.6 | 20.9 | 22.2 | 45.7 | 76.2 | 94.3 | 98.8 |

Whole arteries present (any of their segments):

- LM: 204 of 744 (27.4 %)
- LAD: 210 of 744 (28.2 %)
- CX: 217 of 744 (29.2 %)
- RCA: 245 of 744 (32.9 %)

## Expected connections

Among cases that have both the segment and one of its parents: `direct` = an edge joins them, `via_unlabelled` = joined through unlabelled points, `missing` = not joined (a gap > 1.0 mm or the segment hangs elsewhere).

| segment | parent(s) | cases | direct | via_unlabelled | missing |
|---|---|---|---|---|---|
| pLAD | LM | 204 | 204 | 0 | 0 |
| pCX | LM | 203 | 203 | 0 | 0 |
| mLAD | pLAD | 194 | 194 | 0 | 0 |
| dLAD | mLAD | 178 | 178 | 0 | 0 |
| mRCA | pRCA | 91 | 90 | 1 | 0 |
| dRCA | mRCA | 91 | 91 | 0 | 0 |
| CX | LM/pCX | 175 | 175 | 0 | 0 |
| D1 | LAD/dLAD/mLAD/pLAD | 193 | 193 | 0 | 0 |
| D2 | LAD/dLAD/mLAD/pLAD | 31 | 31 | 0 | 0 |
| IM | CX/LAD/LM/pCX/pLAD | 54 | 54 | 0 | 0 |
| OM1 | CX/dCX/mCX/pCX | 169 | 169 | 0 | 0 |
| PDA | CX/RCA/dCX/dRCA/mCX/mRCA/pCX/pRCA | 102 | 101 | 1 | 0 |
| PLA | CX/PDA/RCA/dCX/dRCA/mCX/mRCA/pCX/pRCA | 179 | 178 | 1 | 0 |

Unexpected segment contacts (pairs not in the expected list; number of cases):

- #28-pCX: 49
- dLAD-pLAD: 9
- #28-CX: 3
- ?AL-pLAD: 3
- #28-mRCA: 1
- #28-OM1: 1
- ?AL-pCX: 1

## Red flags

Cases without any flag: 45 of 744.

| flag | cases |
|---|---|
| unknown_labels | 546 |
| no_LM | 540 |
| no_LAD | 534 |
| no_CX | 527 |
| no_RCA | 499 |
| >2_components | 396 |
| unlabelled>20% | 144 |
| total_length_odd(units?) | 2 |
| segment<2mm | 1 |

- **unknown_labels** (546): 12, 13, 14, 16, 17, 21, 22, 24, 29, 31, 34, 36, 41, 42, 44, 55, 60, 65, 67, 68, 71, 78, 88, 96, 98, 109, 111, 112, 114, 115, 126, 131, 132, 141, 146, 147, 149, 154, 161, 162 ...
- **no_LM** (540): 12, 13, 14, 16, 21, 22, 24, 29, 31, 34, 36, 41, 44, 47, 49, 55, 60, 65, 67, 68, 71, 78, 88, 92, 96, 98, 111, 112, 114, 115, 126, 131, 132, 134, 137, 146, 147, 149, 154, 162 ...
- **no_LAD** (534): 12, 13, 14, 16, 21, 22, 24, 29, 31, 34, 36, 41, 44, 47, 49, 55, 60, 65, 67, 68, 71, 78, 88, 92, 96, 98, 111, 112, 114, 115, 126, 131, 132, 134, 137, 146, 147, 149, 154, 162 ...
- **no_CX** (527): 12, 13, 14, 16, 21, 22, 24, 29, 31, 34, 36, 41, 44, 47, 49, 55, 60, 65, 67, 68, 71, 78, 88, 92, 96, 98, 111, 112, 114, 115, 126, 131, 132, 134, 146, 147, 149, 154, 162, 167 ...
- **no_RCA** (499): 12, 13, 14, 16, 21, 22, 24, 29, 31, 34, 36, 41, 44, 55, 60, 65, 67, 68, 71, 78, 88, 96, 98, 111, 112, 114, 115, 126, 131, 132, 137, 146, 147, 149, 154, 162, 167, 178, 185, 188 ...
- **>2_components** (396): 11, 13, 22, 24, 28, 29, 34, 47, 49, 55, 60, 65, 67, 68, 69, 71, 78, 80, 86, 88, 92, 96, 98, 109, 111, 112, 114, 126, 131, 135, 141, 146, 147, 161, 185, 188, 189, 190, 196, 212 ...
- **unlabelled>20%** (144): 11, 47, 49, 69, 80, 81, 92, 107, 109, 120, 134, 135, 137, 177, 189, 227, 245, 255, 266, 313, 323, 333, 338, 404, 405, 411, 427, 428, 456, 483, 528, 532, 539, 547, 587, 594, 613, 629, 638, 655 ...
- **total_length_odd(units?)** (2): 1360, 1716
- **segment<2mm** (1): 28

Flag meanings: `no_LM/LAD/CX/RCA` = artery missing (a missing LM can be real - separate ostia - but check); `unlabelled>20%`; `>2_components` = fragments; `left_and_right_in_one_tree` = left and right trees joined (should be separate); `impossible_contact` = e.g. LAD touching RCA; `disconnected_segment` = an expected connection is missing; `segment<2mm`; `gaps_in_polyline` = jump inside one polyline; `unknown_labels` = labels not mapped (see label table); `overlapping_polylines` = > 20 % of length runs on top of another polyline.

Figures: `figures/segment_lengths.png`, `segment_presence.png`, `unlabelled_pct.png`, `branch_points.png`, `total_length.png`, `components.png`.
