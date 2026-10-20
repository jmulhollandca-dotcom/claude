# CAL-3 Staged Building Handoff Process

Status: DRAFT for adoption. Owner: John Mulholland. Rev 0, 2026-10-20.

## 1. Purpose

Hand the building over in stages, not as one event at the end. The stages are set by the permits: each occupancy area on the building permit, with its occupancy date, is one handoff package. Inside each package a fixed readiness ladder runs room by room and system by system. Each handoff is a registered link with a producer, a receiver, defined evidence, and the receiver's ack. Nothing is handed over that is not acked. Nothing is held back that is finished.

This document is the admin procedure. The contract language that binds contractors to it is in `docs/specs/01 77 19 Staged Handoff.md`. The forms are in `templates/handoff/`.

## 2. The trigger: permit occupancy dates

1. **The AHJ occupancy schedule defines the handoff packages.** One package per occupancy area (phased or partial occupancy) on the building permit. Package ID = the permit number plus the occupancy area as the AHJ names it.
2. **The occupancy date on the permit is the handoff date for that package.** It is the only date that sets a package's handoff. Schedule dates, meeting dates, and emails forecast toward it; they do not replace it.
3. **The occupancy date is the highest-confidence date in the register.** It is entered on SCHED · ROOM DATES with Source doc = the permit, Said by = the AHJ, Date confidence = CONTRACT (register label; a PERMIT label is proposed in section 7). A re-issued permit is a new claim; the prior stays.
4. **Every room and system is mapped to exactly one occupancy package.** A room in no package has no handoff date and is a visible gap, not a blank. Systems serving more than one package belong to the first package that needs them operational.
5. **The occupancy inspection is the gate, the occupancy date is the deadline.** Occupancy is granted by the AHJ on inspection. The package handoff (H6) cannot be acked before the occupancy permit or partial occupancy permit for that area is issued, and is late if the ack lands after the occupancy date on the permit.
6. **Work back from the occupancy date.** For each package, the H ladder below is scheduled backward from its occupancy date with the AHJ pre-occupancy inspections (fire alarm verification, sprinkler, life safety, electrical final, mechanical final, accessibility, exiting) as named predecessors of H6.

## 3. Rules

1. **A handoff is a registered link, not a meeting.** Producer's output row and receiver's start-list row, same ID, with acked-by, acked-on, and evidence attached.
2. **The receiver's ack closes the stage.** The producer saying "done" does not. Sending the package does not. Ack means "received, and it is what I needed."
3. **Each stage holds only its dependents.** A room released holds nothing in any other room. An occupancy package holds nothing in any other package. A stage that claims to hold "everything after it" is a modelling error.
4. **Finished work hands over the day it is finished.** No batching rooms to the package date, no holding a finished system for an unfinished one. A finished, unreleased stage goes on the holding list, aged in days, with the receivers it is starving.
5. **Every stage date carries provenance.** Said by, source doc, date sighted, confidence. No source means HEARSAY or nothing.
6. **Overrides are logged, never silent.** A stage accepted with open items records who accepted, why, when, and the open items by ID.
7. **Codes in the register, plain words to people.** Stage records carry package ID, SPACE, JAID, WBS, LOT, MS codes. Humans get the room name and the plain description.

## 4. Grain

| Grain | Unit | Register key |
|---|---|---|
| Occupancy package | One occupancy area on the permit | Permit no. + area |
| Room / zone | One room, one yard, one corridor segment | SPACE code, MS code |
| System | One commissionable system (UPS string, gen set, CRAH loop, fire alarm, BMS, EPMS, telecom backbone) | System ID, JAID of head-end asset |
| Building / project | The whole facility | PRJ |

A higher grain is complete only when every lower grain inside it is acked or explicitly N/A with a reason.

## 5. The stage ladder inside each occupancy package

Stages map one-to-one onto the gate dates on SCHED · ROOM DATES and the T / V2P / Cx gate families in the register.

| Stage | Grain | Name | Producer → Receiver | Register gate |
|---|---|---|---|---|
| H0 | Building | Enclosure | GC → Owner's Rep | Enclosed / weathertight |
| H1 | Room | Room release | GC → Owner's Rep, then trades / OFCI | MS room release, Room ready |
| H2 | Room | Equipment landed | OFCI logistics / installer → Owner's Rep | V2P G-gate, Equipment landed |
| H3 | System | Energized | Electrical contractor → Cx agent | Energized |
| H4 | System | Commissioning complete | Cx agent → Owner's Rep | Cx complete (PFC / FPT), CIL dispositioned |
| H5 | System | Integrated systems test passed | Cx agent → Owner | IST |
| H6 | Package | Occupancy and operational turnover | Owner's Rep → Owner operations | Occupancy permit issued, Room status Complete |
| H7 | Building | Final turnover | Owner's Rep → Owner | Owner ack of the zip |

### What each stage holds and does not hold

| Stage | Holds | Does not hold |
|---|---|---|
| H0 | Interior fitout in weather-sensitive rooms | Yard work, exterior pads, design, procurement |
| H1 | Field lots inside that room | Any other room |
| H2 | Power and controls connection to those assets | Other rooms, other assets |
| H3 | Cx start on that system | Other systems, non-electrical fitout |
| H4 | IST scheduling for that system | Other systems |
| H5 | H6 for packages served by that system, 90% billing for that system | Other systems |
| H6 | Operations taking the package, revenue use of the area | Other packages |
| H7 | Close, holdback release | Nothing. Terminal. |

## 6. Stage entry and exit criteria

Each stage has a certificate in `templates/handoff/`. Summary:

**H0 Enclosure.** Roof, walls, doors, glazing closed. Permanent or approved temporary heat. Field review letter for envelope. Water test record. Envelope punch list with dates. Evidence: inspection record, photos keyed to grid, AHJ field review.

**H1 Room release.** Room clean and secured. Finishes to the room data sheet or an exception logged. Lighting on. Power for tools. Fire protection active or fire watch in place. Access control or keyed lock. Room data sheet signed against. Evidence: room release checklist, photos, key register entry.

**H2 Equipment landed.** Every JAID scheduled for the room set in final position, anchored, levelled. Receiving inspection done, damage noted or none. Serial numbers recorded against JAID. Shipping braces removed. Evidence: asset register extract showing gate state, receiving reports, photos.

**H3 Energized.** Pre-functional checks on upstream distribution complete. Megger, torque, settings records. Protective device settings per coordination study, as-left recorded. Lock-out tag-out log transferred. AHJ electrical inspection passed. Evidence: energization permit, PFC records, inspection certificate.

**H4 Commissioning complete.** Functional performance tests executed per the Cx plan. Every test passed or on the CIL with a disposition. Trend data reviewed. As-left settings recorded. Training delivered or dated. Evidence: executed FPT scripts, CIL extract, settings sheet.

**H5 IST passed.** IST executed at the agreed load profile. Failure scenarios per script run and passed. Open CIL items closed or accepted by the Owner as not blocking with a reason logged. Evidence: IST report, witnessed sign sheet, CIL disposition.

**H6 Occupancy and operational turnover.** Occupancy permit or partial occupancy permit for the area issued by the AHJ and filed. All AHJ pre-occupancy inspections passed with certificates on file. All H1 through H5 for the rooms and systems in the package acked. Punch list closed or accepted with dates. Keys, access credentials, badge rights handed to operations. O&M documentation for assets in the package filed and indexed. Spare parts delivered and signed. Evidence: occupancy permit, inspection certificates, package turnover certificate, key receipt, O&M index.

**H7 Final turnover.** Every package at H6. Every system at H5 or N/A with a reason. Final occupancy permit for the whole building issued. The zip assembled complete against its manifest (record documents, asset register, block record, commissioning, quality, regulatory including all permits closed, warranty, O&M, commercial, the log). Evidence: zip manifest checked line by line, Owner's ack in writing.

## 7. Who does what

| Role | Responsibility |
|---|---|
| Producer (GC, trade, Cx agent per stage) | Assembles the evidence, submits the certificate, states open items with IDs. Submits the day the stage is finished. |
| GC | Owns the permit. Books AHJ inspections, obtains occupancy, files the permit and certificates the day received. |
| Owner's Rep | Reviews within the review window, acks or rejects with reasons, logs any override. Maintains the package map and the holding list. |
| Receiver | Confirms received and fit for use. Ack is the receiver's, never the producer's. |
| Register keeper | Writes stage dates with provenance, moves the Tasks row State, attaches the certificate. |
| Owner | Acks H5 per system, H6 per package, H7. |

Review window: 3 working days from submission for H0 through H4, 5 working days for H5 through H7. Silence past the window is not an ack. It goes on the holding list as owed by the reviewer.

Proposed register change for John's ruling: add a `PERMIT` value to Date confidence on SCHED · ROOM DATES above CONTRACT, and a `Occupancy package` column (text, permit no. + area) on SCHED · ROOM DATES and Tasks. Until ruled, permit dates go in as CONTRACT with the permit number in Source doc, and the package ID goes in the Codes field.

## 8. Register mechanics

- **Package map.** One list, kept by the Owner's Rep: package ID, occupancy date, permit source, rooms (SPACE codes), systems. Every room and system appears exactly once.
- **SCHED · ROOM DATES** carries the dates per room. The occupancy date for the room's package is entered first, with the permit as source. Each H stage date is entered with Said by, Source doc, Date sighted on, Date confidence. Re-quoted dates are new claims. The prior claim stays.
- **Tasks** carries one row per stage per room, system, or package, named `H<n> <stage name> - <room, system, or package>`, one WBS package, Contract party set, Task owner set or blank as a chase, package ID in Codes. Predecessor links hold the physical chain inside the room (H1 before H2 before H3), the named feeding links (MMR/IDF H4 before the rooms it serves at H6), and every AHJ pre-occupancy inspection as a predecessor of the package's H6 row.
- **State** moves READY → DONE on producer submission, INSPECTED on Owner's Rep review, CLOSED on receiver ack.
- **Overrides** are an Update on the Tasks row with who, why, when, open item IDs. No override lives only in email.
- **The holding list** is any row at DONE older than the review window without INSPECTED, and any at INSPECTED older than the window without CLOSED. Plus any H6 row whose occupancy date has passed without CLOSED. Read out at every review.

## 9. Rejects, partials, late occupancy

- A reject names the failed criteria by line on the certificate. The producer resubmits the whole certificate.
- A partial release (room released except one wall, system energized except one feeder) is a logged override with the exclusion named by code and a date to clear it. The exclusion becomes its own Tasks row linked as a predecessor to whatever it blocks.
- An AHJ inspection failure is an Issue Register row at P1, Agent = the GC's named contact, Due = the re-inspection date, linked to the package's H6 row. It is never absorbed into the schedule silently.
- If an occupancy date on the permit is going to be missed, the GC states it in writing with the cause and the recovery date before the date passes. The recovery date is a new claim at SCHEDULE confidence. The permit date remains the baseline against which the miss is measured.
- A stage is never re-opened. A defect found after ack is an Issue Register row, not a reversal.

## 10. Reuse on future projects

The trigger rule, ladder, rules, certificates, and spec section are project-independent. Per project, fill in: the permit and its occupancy areas, the room-to-package map, the system list, review windows if different, named roles, and gate labels if the register uses different ones. See `docs/admin/Adoption_Guide.md`.
