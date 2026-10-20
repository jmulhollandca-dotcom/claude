#!/usr/bin/env python3
"""Build a layered (OCG) Room Regime plan PDF.

Usage: make_regime_plan.py rooms.csv out.pdf [--base base_plan.pdf --page N] [--rev 03 --date 2026-10-20 --dwg JV-RR-101]

rooms.csv columns: space,name,regime,tier,exclusion,x0,y0,x1,y1
  regime: GC | ESTRUXTURE | blank (not in any occupancy package)
  coords in PDF points on the target page. Polygons: use x0..y0 pairs as
  'poly' column "x,y;x,y;..." instead of the rectangle columns.
Layers: Base plan, GC areas, eStruxture areas, Not in package, Exclusions, Labels, Legend.
"""
import csv, sys, argparse
from pypdf import PdfWriter, PdfReader
from pypdf.generic import (DictionaryObject, NameObject, ArrayObject, FloatObject,
                           TextStringObject, StreamObject, NumberObject)

GC = (1.0, 0.55, 0.0)      # orange
ES = (0.0, 0.45, 0.85)     # blue
NP = (0.6, 0.6, 0.6)       # grey outline
EX = (0.85, 0.0, 0.0)      # red outline
ALPHA = 0.30

def esc(s): return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

def room_path(r):
    if r.get("poly"):
        pts = [tuple(map(float, p.split(","))) for p in r["poly"].split(";")]
    else:
        x0,y0,x1,y1 = (float(r[k]) for k in ("x0","y0","x1","y1"))
        pts = [(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
    ops = [f"{pts[0][0]:.1f} {pts[0][1]:.1f} m"] + [f"{x:.1f} {y:.1f} l" for x,y in pts[1:]] + ["h"]
    cx = sum(p[0] for p in pts)/len(pts); cy = sum(p[1] for p in pts)/len(pts)
    return " ".join(ops), (cx, cy)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv"); ap.add_argument("out")
    ap.add_argument("--base"); ap.add_argument("--page", type=int, default=0)
    ap.add_argument("--rev", default="00"); ap.add_argument("--date", default="")
    ap.add_argument("--dwg", default="JV-RR-000"); ap.add_argument("--title", default="ROOM REGIME AND ACCESS CONTROL PLAN")
    a = ap.parse_args()
    rooms = list(csv.DictReader(open(a.csv)))

    w = PdfWriter()
    if a.base:
        base = PdfReader(a.base).pages[a.page]
        page = w.add_page(base)
        W = float(page.mediabox.width); H = float(page.mediabox.height)
    else:
        W, H = 1000, 700
        page = w.add_blank_page(W, H)

    # Optional content groups
    names = ["Base plan","GC areas","eStruxture areas","Not in package","Exclusions","Labels","Legend"]
    ocgs = {}
    for n in names:
        g = DictionaryObject({NameObject("/Type"): NameObject("/OCG"), NameObject("/Name"): TextStringObject(n)})
        ocgs[n] = w._add_object(g)
    w._root_object[NameObject("/OCProperties")] = DictionaryObject({
        NameObject("/OCGs"): ArrayObject(list(ocgs.values())),
        NameObject("/D"): DictionaryObject({NameObject("/Order"): ArrayObject(list(ocgs.values())),
                                             NameObject("/ON"): ArrayObject(list(ocgs.values()))})})
    props = DictionaryObject({NameObject(f"/L{i}"): ocgs[n] for i,n in enumerate(names)})
    L = {n: f"/L{i}" for i,n in enumerate(names)}

    gs = DictionaryObject({NameObject("/Type"): NameObject("/ExtGState"), NameObject("/ca"): FloatObject(ALPHA), NameObject("/CA"): FloatObject(1)})
    font = DictionaryObject({NameObject("/Type"): NameObject("/Font"), NameObject("/Subtype"): NameObject("/Type1"), NameObject("/BaseFont"): NameObject("/Helvetica")})
    fontb = DictionaryObject({NameObject("/Type"): NameObject("/Font"), NameObject("/Subtype"): NameObject("/Type1"), NameObject("/BaseFont"): NameObject("/Helvetica-Bold")})

    c = []
    def layer(n, body):
        c.append(f"/OC {L[n]} BDC"); c.extend(body); c.append("EMC")

    if not a.base:  # dummy base plan: walls only
        b = ["q 0 0 0 RG 1.5 w"]
        for r in rooms:
            p,_ = room_path(r); b.append(f"{p} S")
        b.append("Q")
        layer("Base plan", b)

    for key, col, n in (("GC", GC, "GC areas"), ("ESTRUXTURE", ES, "eStruxture areas")):
        b = [f"q /GSa gs {col[0]} {col[1]} {col[2]} rg"]
        for r in rooms:
            if r["regime"].strip().upper() == key:
                p,_ = room_path(r); b.append(f"{p} f")
        b.append("Q"); layer(n, b)

    b = [f"q {NP[0]} {NP[1]} {NP[2]} RG 2 w [6 4] 0 d"]
    for r in rooms:
        if not r["regime"].strip():
            p,_ = room_path(r); b.append(f"{p} S")
    b.append("Q"); layer("Not in package", b)

    b = [f"q {EX[0]} {EX[1]} {EX[2]} RG 3 w"]
    for r in rooms:
        if r.get("exclusion","").strip():
            p,(cx,cy) = room_path(r); b.append(f"{p} S")
            b.append(f"BT /F1 8 Tf {cx-60:.1f} {cy-26:.1f} Td ({esc(r['exclusion'][:40])}) Tj ET")
    b.append("Q"); layer("Exclusions", b)

    b = ["q 0 0 0 rg"]
    for r in rooms:
        _,(cx,cy) = room_path(r)
        b.append(f"BT /F2 11 Tf {cx-30:.1f} {cy+4:.1f} Td ({esc(r['space'])}) Tj ET")
        b.append(f"BT /F1 8 Tf {cx-30:.1f} {cy-8:.1f} Td ({esc(r['name'])}) Tj ET")
        b.append(f"BT /F2 12 Tf {cx+34:.1f} {cy+2:.1f} Td ({esc(r['tier'])}) Tj ET")
    b.append("Q"); layer("Labels", b)

    # Legend / title block
    lx, ly = W-160, 20
    b = [f"q 1 1 1 rg 0 0 0 RG 1 w {lx} {ly} 150 150 re B 0 0 0 rg",
         f"BT /F2 9 Tf {lx+6} {ly+136} Td ({esc(a.title)}) Tj ET",
         f"BT /F1 8 Tf {lx+6} {ly+124} Td (DWG {esc(a.dwg)}  REV {esc(a.rev)}  {esc(a.date)}) Tj ET",
         f"BT /F1 7 Tf {lx+6} {ly+113} Td (Issued for information. Governs site access from rev date.) Tj ET",
         f"q /GSa gs {GC[0]} {GC[1]} {GC[2]} rg {lx+6} {ly+92} 14 10 re f Q BT /F1 8 Tf {lx+24} {ly+94} Td (GC area  -  GC prime contractor) Tj ET",
         f"q /GSa gs {ES[0]} {ES[1]} {ES[2]} rg {lx+6} {ly+76} 14 10 re f Q BT /F1 8 Tf {lx+24} {ly+78} Td (eStruxture area  -  eStruxture prime) Tj ET",
         f"q {NP[0]} {NP[1]} {NP[2]} RG 1.5 w [4 3] 0 d {lx+6} {ly+60} 14 10 re S Q BT /F1 8 Tf {lx+24} {ly+62} Td (Not yet in an occupancy package) Tj ET",
         f"q {EX[0]} {EX[1]} {EX[2]} RG 2 w {lx+6} {ly+44} 14 10 re S Q BT /F1 8 Tf {lx+24} {ly+46} Td (Open exclusion / override, see schedule) Tj ET",
         f"BT /F1 8 Tf {lx+6} {ly+28} Td (Letter in room = security tier A/B/C) Tj ET",
         f"BT /F1 7 Tf {lx+6} {ly+10} Td (Layers: toggle in viewer. Print with all layers on.) Tj ET", "Q"]
    layer("Legend", b)

    stream = StreamObject(); stream._data = ("\n".join(c)).encode("latin-1"); 
    res = page.get("/Resources")
    if res is None:
        res = DictionaryObject(); page[NameObject("/Resources")] = res
    res = page["/Resources"]
    res[NameObject("/Properties")] = props
    res.setdefault(NameObject("/ExtGState"), DictionaryObject())[NameObject("/GSa")] = gs
    fonts = res.setdefault(NameObject("/Font"), DictionaryObject())
    fonts[NameObject("/F1")] = font; fonts[NameObject("/F2")] = fontb
    existing = page.get("/Contents")
    new = w._add_object(stream)
    if existing is None:
        page[NameObject("/Contents")] = new
    else:
        arr = existing.get_object()
        if isinstance(arr, ArrayObject): arr.append(new)
        else: page[NameObject("/Contents")] = ArrayObject([existing, new])
    w.write(a.out)
    print("wrote", a.out, "rooms:", len(rooms))

if __name__ == "__main__":
    main()
