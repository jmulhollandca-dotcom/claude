# Local session brief: REF spaces vs ACC locations

Start a local Claude Code session on this repo, branch `claude/gallant-heisenberg-ho49a9`, and paste this file as the first message.

## Background

John (VP Engineering, Javco; owner's rep for eStruxture CAL3) believes all REF spaces are loaded into Autodesk Construction Cloud (ACC) locations. Verify it by API and tie the result back to the CAL3 PCO register. This runs locally because the API keys are on John's machine; John handles unlocking them and will export them as environment variables (`APS_CLIENT_ID`, `APS_CLIENT_SECRET`, `ACC_ACCOUNT_ID`, `ACC_PROJECT_ID`, `MONDAY_API_TOKEN`). Never echo key values into chat or commit them.

Branch contents:
- `build_pco_register.py`: openpyxl generator. Sheets: PCO Register (19 rows), Lot materials (Pkg B) (59 rows), eStruxture vendors, Contracts, Totals. Lot codes look like `TP-DHC-01H`, `TP-CSB-05A`, `CAM-TMP-01`.
- `CAL3_PCO_Register_2026-10-20.xlsx`: generated output.

Monday workspace: CAL3 WAR ROOM. ADMIN · CHANGE ORDERS = 18428212263, ADMIN · POs = 18428192175. REF spaces/rooms board id unknown; find it by name. Load the `cal3-war-room-board` skill if present (codes drive links, never invent codes, one line per thing).

Standing rules: straight facts, no fluff. Nothing goes to an eStruxture direct account unless the vendor is an active eStruxture trader or John says so.

## Task

1. Read the credentials from the environment variables above.
2. Pull the full ACC locations tree for CAL3 (ACC Locations API, paged). Save `acc_locations.csv` (id, parent, name, code/barcode, path).
3. Pull the REF spaces board from Monday (GraphQL). Save `ref_spaces.csv`.
4. Diff by code, then normalized name: REF not in ACC, ACC not in REF, name/code mismatches. Write `ref_vs_acc_diff.md`, counts at top, one line per discrepancy.
5. Add an "ACC location" column to the PCO Register and Lot materials sheets in `build_pco_register.py`, keyed on lot codes; regenerate the xlsx.
6. Commit and push to the same branch. Report counts matched / missing each way and whether the load is complete.

## Result (2026-10-20)

- ACC Locations tree pulled live with the signed-in APS token: 486 nodes, 447 room-level nodes, 485 with barcodes. Saved as `acc_locations.csv` (id, parent, name, code, type, path).
- Monday steps dropped on John's instruction during the run ("never mind monday we are done with it"). No REF export or REF-vs-ACC diff is kept.
- `build_pco_register.py` now adds an "ACC location" column to the PCO Register and Lot materials sheets. Lot codes are AP tender packages (`TP-<block>-<package><letter>`); the package number is not a level, so each lot resolves to its ACC block node (name, barcode, node id). Rows with no block in the lot text are marked as not mapped.
