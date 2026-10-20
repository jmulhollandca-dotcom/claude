from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

wb = Workbook()

# ---------------- Sheet 1: PCO register (money items) ----------------
ws = wb.active
ws.title = "PCO Register"
hdr = ["PCO #", "Contract charged (proposed)", "Confirm?", "Vendor", "AP PO #", "Vendor quote / ref",
       "Lot / tender pkg", "Scope", "Amount CAD (pre-tax)", "Amount basis", "Kylie approval",
       "Status / open issue", "Source email (date)"]
ws.append(hdr)

EST = "eStruxture direct account"
PKB = "AP Package B site work (PO6246)"
DA2 = "AP DA2 Design Assist / OFCI agreement"

rows = [
 ["PCO-001", EST, "Y", "Texcan", "2766-CAL3-0002 (rev)", "Q-1018940 / OA 1750503", "GENERAL STOCK (DHA/DHE)",
  "751 m MV105 1C-750 35kV Cu EPR cable. Trevor: general stock, to be pulled for DHA/DHE in new year. Factory price adjustment to $211.44/m.",
  158791.44, "AP PO 2766 rev + Texcan OA 1750503 (tax 7,939.57 extra)", "Original approved 2026-10-05; revised PO awaiting Kylie",
  "Future-phase stock, not Phase 1 Package B scope. Prysmian stock lengths 178/187/189/197 m, 2 wk delivery, +/-5% tolerance, price subject to tariff at shipment.", "2026-10-20"],
 ["PCO-002", EST, "Y", "Magna IV Engineering", "not yet issued", "Q-188471", "TP-DHC-01I (Nishi) / DH-D per Devon",
  "CAL-3 Phase 2 DHD MV terminations & testing, lump sum. Same scope as DHC. OEM lead times do not meet schedule; alternates offered.",
  119500.00, "Magna Q-188471 lump sum, excl. tax; extras at $135/hr blended", "Conditional (Kylie 2026-10-13): lead-time alternates must be confirmed",
  "Devon told Keith to proceed 2026-10-13. Nishi re-requested approval 2026-10-20 under TP-DHC-01I. PO not yet issued. Phase 2 scope: confirm whether this is a Package B change or owner-direct.", "2026-10-13 / 2026-10-20"],
 ["PCO-003", PKB, "Y", "Magna IV Engineering", "2924-CAL3-0002", "Q-176183", "CAM-TMP-01",
  "CAL-3 temp power MV terminations & testing (June 2026 work). Original quote, PO issued 2026-10-20 after work done.",
  18950.00, "AP PO 2924 (matches Q-176183 total)", "Trevor approved quote 2026-06-13; PO issued 2026-10-20",
  "Work done June 2026 without PO. Temp power responsibility (AP vs owner) to confirm.", "2026-10-20"],
 ["PCO-004", PKB, "Y", "Magna IV Engineering", "2924-CAL3-0002 (not on PO)", "CO #001 A5344-310776", "CAM-TMP-01",
  "Change order: 126 hrs additional labour/OT/DT ($17,010) + material ($3,122.34) for temp power setup. Cable type change, delays, extra Vista switch parts and termination kits.",
  20132.34, "Magna CO #001 dated 2026-09-01", "Not approved. Keith asked 2026-10-20 whether CO can be invoiced",
  "PO 2924 covers $18,950 only. CO not on PO. Decision needed: approve/reject CO and who carries it.", "2026-10-20"],
 ["PCO-005", PKB, "Y", "Trinity Power (Sunbelt Solomon)", "2812-CAL3-0002", "RA 105124 R2 (Oct) / 105267 (Nov)", "none on PO (Kylie asked for work package no.)",
  "Rental 6 x Avtron 720 kW liquid-cooled load banks + 3000A 600V dist, 6 x 800A breakers, cam cables, SPE-1000 cert, delivery and return freight. 28-day rental, Oct requirement. Nov order (7 units) separate RA.",
  172310.00, "AP PO 2812 total", "Signed by Joey/Angelo 2026-10-14; Kylie approval requested 2026-10-15; PO sent 2026-10-15",
  "Kolostat (Adrien) confirms it is AP's PO. Kylie: needs a work package number so AP can invoice it. Nov RA 105267 not on this PO. Freight 14,319 + 12,519 return.", "2026-10-15"],
 ["PCO-006", PKB, "Y", "Sunbelt Rentals", "2866-CAL3-0002", "Q-80525227 Rev 2", "TP-DHC-01H COMMISSIONING",
  "Rental 1 x 1250 kW 480 V resistive load bank + 48 x 50 ft cam cables + 16 pigtails, 4-week rate, 3rd-party freight delivery and return.",
  15729.00, "AP PO 2866 total", "Approved; PO sent 2026-10-16",
  "Freight renegotiated (Nishi: cannot pay over $16k freight). UPS testing.", "2026-10-16"],
 ["PCO-007", PKB, "Y", "Sunbelt Rentals", "2791", "Contract 80519077", "none",
  "Temp cooling: 2 x 5T portable AC, 400A cam distro, fan, duct, spider box cables, E&D labour, 4 weeks (Oct 14 to Nov 11). Two additional 5T units requested 2026-10-13 on new PO.",
  9687.55, "Sunbelt reservation 80519077 subtotal (GST 484.39 extra)", "Approved 2026-10-15",
  "Second PO for 2 additional units not yet seen in folder.", "2026-10-15"],
 ["PCO-008", PKB, "Y", "JM Test Systems (BHD)", "2915-CAL3-0002", "RQ24624", "TP-DHC-1H",
  "Rental Fluke 1777 power quality analyzer + 3 x 6000A flex CTs, 28-day rate Oct 19 to Nov 15. Marty expects 3 months.",
  2295.00, "AP PO 2915 / RQ24624 (28 days only)", "Approved; PO sent 2026-10-19",
  "JM Test wants credit card; Nishi asking for account terms. 3-month need = ~3x this amount.", "2026-10-19"],
 ["PCO-009", PKB, "Y", "Crystal Services", "2885-CAL3-0002", "Invoice 9812", "none",
  "Equipment moves Sept 28 to Oct 2: switchgear hoist to level 2 by zoom boom, generator jack/level, exhaust piping removal, switchgear unload at warehouse. Sterling+operator, supervisor, labourers, zoom boom rental.",
  29100.00, "Invoice 9812 subtotal (GST 1,455 extra); PO 2885 matches", "Approved by Kylie 2026-10-15; PO sent 2026-10-16",
  "OFCI equipment handling. Candidate for DA2 OFCI coordination line if owner agrees; otherwise Package B.", "2026-10-16"],
 ["PCO-010", PKB, "Y", "Rodeo Cutting & Coring", "not yet issued", "Inv 58340, 57846, 57847, 58299", "none",
  "Scanning, coring, handsawing Sept 7 to Oct 3 (electrical rooms, precast walls, exterior holes, lobby slab).",
  21852.50, "Sum of 4 invoice subtotals (8,060 + 300 + 8,330 + 5,162.50); GST extra; totals incl. GST 22,945.15", "Requested 2026-10-19; Ryan confirmed work complete",
  "Four invoices with no PO. Base-building penetrations: confirm AP vs GC responsibility.", "2026-10-19"],
 ["PCO-011", PKB, "Y", "Phoenix Energy Services", "not yet issued", "Invoice PSI-73097", "SITE WORK",
  "T&M labour Oct 5 to 11 with signed tickets. Edward confirmed hours match timecards (truck and 3rd-party charges not tracked by AP).",
  None, "Invoice PDF is scanned; amount not extractable here", "Requested 2026-10-15 and 2026-10-16",
  "Amount to be read from invoice. T&M authorization lines were blank per earlier review.", "2026-10-16"],
 ["PCO-012", PKB, "N", "Unitray Systems", "2822-CAL3-0002 rev 3", "QT006732-1", "TP-CSB-04R",
  "Cable tray, fittings, rubber roof supports (30 x 457 mm, 20 x 244 mm), freight. Heat trace, fire alarm and exhaust fan access.",
  14767.11, "AP PO 2822 rev 3", "Approved 2026-10-14 (rev 3 lower than prior)", "Shipped to warehouse.", "2026-10-14"],
 ["PCO-013", EST, "Y", "Solution Control Systems", "2271-CAL3-002 / 2273-CAL3-0002 / CAL3-SCS26-2095 / CAL3-SCS26-2038", "Jonny Lee email 2026-07-22", "GEN LB camlock / UPS busducts",
  "Camlocks sourced via US; cost impact $22k to $25k plus shipping and tariffs (SCS). Separate: battery cabinet covers crate to Edmonton for ground-bus modification, freight liability unresolved.",
  22000.00, "SCS estimate low end ($22k to $25k), not quoted", "No approval on record",
  "OFCI vendor scope change. Who pays camlock premium and cover freight is open. CAL3-SCS26 numbers look like owner POs: confirm contract.", "2026-10-20"],
 ["PCO-014", PKB, "N", "Anixter / Wesco", "pending", "Q00HQ9GG", "MR-TP-DHC-1E",
  "768 m 600 kcmil Cu RW90 + 900 m #2 Cu RW90 green. Alberta stock.",
  77485.20, "Anixter quote total", "Approved 2026-10-19", "Price valid 5 days, metal escalation. Flat deck freight extra.", "2026-10-19"],
 ["PCO-015", PKB, "N", "Texcan", "pending", "Q-1021418", "TP-DHC-01A",
  "450 m RW90 250 MCM Cu (MR asked 400 m). Calgary stock.",
  16776.00, "Texcan quote (450 m x $37.28)", "Approved 2026-10-20", "450 vs 400 m not resolved; metal adjustment at shipment.", "2026-10-20"],
 ["PCO-016", PKB, "N", "Noramco", "pending", "Q-1600617", "TP-DHC-04",
  "94 m 250 MCM Cu RW90 (30 m + 64 m). Only supplier with stock.",
  3815.46, "Noramco quote", "Approved 2026-10-16", "", "2026-10-16"],
 ["PCO-017", PKB, "N", "Gescan", "pending", "18240937-00", "TP-CSB-02B",
  "Wiremold floor box parts for NOC room missed box + $200 expedite freight.",
  1153.05, "Gescan quote incl. freight", "Requested 2026-10-16", "7 to 15 working days from Wiremold.", "2026-10-16"],
 ["PCO-018", PKB, "N", "Gescan", "pending", "18247665-00", "TP-CSB-09",
  "15 x 4 in square covers (30 requested, 15 in stock).",
  459.92, "Gescan quote (30 pcs); 15 pcs = 229.96", "Requested 2026-10-16", "", "2026-10-16"],
 ["PCO-019", PKB, "N", "Graybar", "pending", "516513-00 rev", "TP-DHC-03B",
  "150 x T&B universal clamps (tray down), air freight from Quebec. 350 requested.",
  868.00, "Graybar quote: 828 + 40 freight (GST 43.40 extra)", "Approved 2026-10-20", "Remaining 200 to be sourced elsewhere.", "2026-10-20"],
]
for r in rows:
    ws.append(r)

# ---------------- Sheet 2: Lot material requests (Package B, no PCO) ----------------
ws2 = wb.create_sheet("Lot materials (Pkg B)")
ws2.append(["Vendor", "Quote / bid", "Lot / tender pkg", "Note from thread", "Kylie approval", "Date", "Amount"])
lots = [
 ["EWCL", "S1813982 / S1813988 / S1814008", "various", "Jeff Bosch chasing approval", "Pending", "2026-10-20", "in bid PDF"],
 ["EWCL", "S1814255", "TP-DHC-1A", "wire, 2 to 3 day ETA", "Pending", "2026-10-19", "in bid PDF"],
 ["EWCL", "S1814232", "TP-CSB-09B", "in-stock items only", "Pending", "2026-10-19", "in bid PDF"],
 ["EWCL", "S1814203", "TP-CSB-09", "in-stock items only", "Pending", "2026-10-19", "in bid PDF"],
 ["EECOL", "Q-956984", "TP-DHC-02A", "stocked, pickup same day", "Pending", "2026-10-20", "in quote PDF"],
 ["EECOL", "Q-954829", "CAM-TMP-01", "spider box, in stock", "Pending", "2026-10-19", "in quote PDF"],
 ["EWCL", "S1813895 / S1813896", "TP-CSB-05A / TP-DHC-05A", "all in stock; acknowledged, ships Monday", "Approved 2026-10-15", "2026-10-15", "in bid PDF"],
 ["EWCL", "S1813292 / S1813295 / S1813302", "GENERAL STOCK", "in stock + under 1 week; MR revised", "Requested 2026-10-16", "2026-10-16", "in bid PDF"],
 ["EWCL", "S1813595", "CAM-TMP-01", "in-stock only; HAL UHBS2 substituted for RENO HBU", "Requested 2026-10-16", "2026-10-16", "in bid PDF"],
 ["EECOL", "Q-2997666", "TP-DHC-08A", "stocked", "Approved 2026-10-16", "2026-10-16", "in quote PDF"],
 ["EECOL", "Q-951766", "TP-DHC-03B", "1 item in stock", "Approved 2026-10-16", "2026-10-16", "in quote PDF"],
 ["Amazon", "n/a", "TP-DHC-01B", "rubber edge, short 2000; 30 pcs 50 ft", "Requested 2026-10-16", "2026-10-16", "n/a"],
 ["EECOL", "955640", "TP-CSB-04R", "all in stock", "Approved 2026-10-15", "2026-10-15", "in quote PDF"],
 ["EECOL", "Q-299786", "TP-DHC-08C", "in stock", "Approved 2026-10-15", "2026-10-15", "in quote PDF"],
 ["City Electric", "NEC/053215", "TP-DHC-02A", "in stock", "Approved 2026-10-15", "2026-10-15", "in quote PDF"],
 ["EECOL", "Q-955980", "TP-CSB-09", "all in stock", "Approved 2026-10-15", "2026-10-15", "in quote PDF"],
 ["EECOL", "Q-956063", "TP-DHC-01C", "3 items", "Approved 2026-10-15", "2026-10-15", "in quote PDF"],
 ["Texcan", "Q-1020827", "TP-DHC-01C", "stock, weekend work", "Approved 2026-10-15", "2026-10-15", "in quote PDF"],
 ["Bolt Supply", "9482309-00", "TP-DHC-01C", "all non-electrical items", "Approved 2026-10-15 (after call)", "2026-10-15", "in quote PDF"],
 ["EWCL", "S1813928", "DHC 2A", "in-stock items; 2 not stocked", "Pending", "2026-10-15", "in bid PDF"],
 ["EWCL", "S1813874", "TP-CSB-02A", "4 week ETA", "Pending", "2026-10-15", "in bid PDF"],
 ["EWCL", "S1813894", "TP-CSB-09", "PVC boxes declined", "Declined", "2026-10-15", "n/a"],
 ["EWCL", "S1813893", "TP-DHC-02A", "in stock", "Pending", "2026-10-15", "in bid PDF"],
 ["EWCL", "S1813825", "TP-DHD-01B", "multiple options", "Pending", "2026-10-15", "in bid PDF"],
 ["EWCL", "S1812850", "TP-CDB-09", "blue liquid tight; pre-approved by Angelo", "Approved 2026-10-15", "2026-10-15", "in bid PDF"],
 ["EBH", "Q-11338521", "TP-CSB-09", "basket tray covers, only supplier before month end", "Requested 2026-10-14", "2026-10-14", "in quote PDF"],
 ["Amazon", "n/a", "TP-CSB-02F", "Brady lockbox LOTO", "Approved 2026-10-14", "2026-10-14", "n/a"],
 ["EWCL", "S1813542", "TP-DHC-02A", "in stock; ships Friday", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["City Electric", "NEC/053203", "TP-DHC-01E", "30 m in stock", "Approved 2026-10-14", "2026-10-14", "in quote PDF"],
 ["City Electric", "NEC/053208", "TP-DHC-01A", "2 items", "Approved 2026-10-14", "2026-10-14", "in quote PDF"],
 ["City Electric", "NEC 053143", "TP-DHC-02B", "all in stock", "Approved 2026-10-14", "2026-10-14", "in quote PDF"],
 ["EWCL", "S1812899", "TP-CSB-04R", "in-stock items; 10 KO fillers sold out", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1813747", "TP-DHC-01C", "1 week ETA items only", "Pending", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1812912", "TP-DHC-08A", "slotted shipped in error; RMA, solid in stock", "n/a (RMA)", "2026-10-14", "n/a"],
 ["EWCL", "S1813609", "TP-DHD-01A", "4 options", "Pending", "2026-10-14", "in bid PDF"],
 ["EECOL", "Q-955351", "n/a", "motion sensor switch (Devon)", "Approved 2026-10-14", "2026-10-14", "in quote PDF"],
 ["Alberta Breaker", "Q-29225 / Q-29227", "TP-DHC-01E", "18 in stock + 100 air freight", "Approved 2026-10-14", "2026-10-14", "in quote PDF"],
 ["EWCL", "S1813601", "DHC-01F", "in-stock items", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1813305", "TP-DHC-01E", "20 pcs in stock", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1813568", "TP-DHD-1E", "in-stock items", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1813502", "TP-CSB-05A", "in-stock items", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["Amazon", "n/a", "TP-DHC-01B", "rubber edge, $60/roll vs EECOL $500/roll", "Approved 2026-10-14", "2026-10-14", "n/a"],
 ["EECOL", "Q-2425750", "TP-CSB-02B", "extra exit signs, Joey pre-approved", "Approved 2026-10-14", "2026-10-14", "in quote PDF"],
 ["EWCL", "S1813346", "TP-DHC-1F", "all items incl. short lead", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1813332", "TP-DHC-01E", "in stock + MR qty 20 line 2", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1813360", "TP-DHC 2A", "in-stock items", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["EWCL", "S1813351", "CAM-TMP-01", "all in stock", "Approved 2026-10-14", "2026-10-14", "in bid PDF"],
 ["Uline", "n/a", "TP-CSB-05A", "only stocked at Uline", "Requested 2026-10-14", "2026-10-14", "n/a"],
 ["CES (City Electric)", "NEC053193", "TP-CSB-09", "2 items", "Approved 2026-10-13", "2026-10-13", "in quote PDF"],
 ["City Electric", "NEC53172", "TP-DHC-01D", "4 items in stock", "Approved 2026-10-13", "2026-10-13", "in quote PDF"],
 ["EWCL", "S1813349", "TP-DHC-1E", "60 m or 45 m options, 2 to 6 wk", "Pending", "2026-10-13", "in bid PDF"],
 ["EWCL", "S1813370", "TP-CSB-05A", "3 options", "Pending", "2026-10-13", "in bid PDF"],
 ["Bolt Supply", "9477946-00 / 9470948-00 / 9471032-00", "GENERAL STOCK", "bulk order, Allan; PO done, OA received, no ETA", "Approved (prior)", "2026-10-13", "in quote PDF"],
 ["EECOL", "Q-954899", "TP-DHC-01B", "rubber edge; Kylie flagged $500/roll vs Amazon $60", "Challenged", "2026-10-13", "in quote PDF"],
 ["EBH", "Q11347666", "TP-DHC-05A", "1 item", "Approved 2026-10-13", "2026-10-13", "in quote PDF"],
 ["Bolt Supply", "9482312-00", "TP-CSB-09", "in stock", "Approved 2026-10-13", "2026-10-13", "in quote PDF"],
 ["City Electric", "NEC53170", "TP-DHC-02A", "see Kylie note", "Approved 2026-10-13", "2026-10-13", "in quote PDF"],
 ["Gescan", "18221956-00", "TP-DHC-01E", "14 x #6 lugs", "Approved 2026-10-06", "2026-10-06", "in quote PDF"],
 ["Westburn / Burndy", "LUGS.xlsx list", "various", "LLSCO lug shortage, 22+ wk leads; air freight option", "Open", "2026-10-20", "n/a"],
]
for r in lots:
    ws2.append(r)

# ---------------- Sheet 3: Contract summary ----------------
ws3 = wb.create_sheet("Contracts")
ws3.append(["Contract", "Parties", "Value CAD", "Source"])
ws3.append(["Package B PO6246 (electrical subcontract, supplemental conditions)", "Leeswood Construction / AP Electric (CGL)", 72260828.62, "SoV memo 2026-08-27 (Attachment R4)"])
ws3.append(["DA2 / OFCI Coordination Services Agreement", "eStruxture / CGL Inc. direct", 2739171.38, "SoV memo 2026-08-27 (Attachment R3)"])
ws3.append(["eStruxture direct accounts", "eStruxture / vendor", None, "Owner-direct purchases (future phase stock, OFCI vendor changes)"])

# ---------------- Sheet 4: Bucket totals ----------------
ws4 = wb.create_sheet("Totals")
ws4.append(["Contract charged (proposed)", "Count", "Amount CAD (pre-tax, items with amounts)"])
from collections import OrderedDict
tot = OrderedDict()
for r in rows:
    k = r[1]; tot.setdefault(k, [0, 0.0]); tot[k][0] += 1
    if r[8]: tot[k][1] += r[8]
for k, (c, a) in tot.items():
    ws4.append([k, c, round(a, 2)])

# formatting
for w in (ws, ws2, ws3, ws4):
    for c in w[1]:
        c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1F3864")
        c.alignment = Alignment(wrap_text=True, vertical="top")
    for row in w.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, col in enumerate(w.columns, 1):
        w.column_dimensions[get_column_letter(i)].width = 22
    w.freeze_panes = "A2"
ws.column_dimensions["H"].width = 60; ws.column_dimensions["L"].width = 50
for row in ws.iter_rows(min_row=2, min_col=9, max_col=9):
    for c in row: c.number_format = '#,##0.00'
for row in ws3.iter_rows(min_row=2, min_col=3, max_col=3):
    for c in row: c.number_format = '#,##0.00'
for row in ws4.iter_rows(min_row=2, min_col=3, max_col=3):
    for c in row: c.number_format = '#,##0.00'

wb.save("/home/user/claude/CAL3_PCO_Register_2026-10-20.xlsx")
print("rows", len(rows), "lots", len(lots))
for k, v in tot.items(): print(k, v)
