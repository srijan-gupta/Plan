---
name: update-phd-master
description: Safely research and update the canonical PhD lab master GitHub Pages database in this repository without losing rows, columns, filters, scoring, profiles, styling, or interactive behavior. Use whenever adding/updating labs, deep profiles, scores/attention tiers, filters, layout, or GitHub Pages content.
---

# Update PhD Master Database

## Canonical artifact

- Repository: `srijan-gupta/Plan`.
- GitHub Pages is served from the repository's canonical `index.html`.
- Treat `index.html` on `main` as the source of truth. Do **not** create chains of versioned HTML files for normal updates.
- Before editing, fetch the current `index.html` from GitHub. Never start from an older sandbox/download copy merely because it is locally available.
- Preserve Git history through commits; the repository history replaces the old proliferation of static HTML copies.

## Governing principle

This is a **coverage-first research database and decision tool**, not a prestige ranking. Preserve all existing information unless there is a specific evidence-based reason to change it. Add/update data without silently deleting columns, rows, profiles, controls, CSS, JavaScript, localStorage behavior, or metadata.

The user's target research identity is:

> Physics + modelling/inference + algorithms + computational optimization + systems implementation + experiment, on important long-horizon problems.

Preferred loop:

> physical problem → model/simulate → experiment/measurement → infer → when observation disagrees, debug mechanism → refine model/setup → optimize/implement → probe again.

Implementation and experiment are important because they close the loop; they are not necessarily the intellectual objective.

## Mandatory workflow for every update

1. **Fetch current `index.html` from `main`.**
2. **Inventory before modifying:** row count, column count/order, grouped headers/colspans, profile count, filter widgets/data attributes, scoring/attention JS, localStorage keys, frozen-column widths/offsets, and important CSS classes.
3. Make the **smallest targeted change**. Do not rebuild the workbook from scratch unless explicitly requested.
4. If research facts are being changed, research the **specific PI/group/project**, preferring current primary sources: official lab/faculty/project pages, current openings, theses, publications and student outcomes.
5. Populate **all applicable columns**, not only the field that triggered the update. A newly added row must be complete enough to compare with existing rows.
6. Deep-profile claims must be group/project specific. Do not copy generic track-level prose.
7. Recompute dependent scores/priority fields if an input factor changes.
8. If adding a filterable column, update **all three layers**: visible filter control, row `data-*` attributes, and JS filter field/label configuration.
9. Validate structurally before commit: same or intentionally changed row/column counts; every body row aligned to headers; colspans correct; profile links resolve; filters work; score adjustment works; localStorage still works; table/frozen columns remain aligned.
10. Commit the updated **same `index.html`** to `main` with a concise message. Do not create another public HTML copy unless explicitly requested.
11. Report what changed and any evidence gaps. Do not claim a group is deeply researched when it is not.

## Research standard

For each serious candidate, answer concretely:

- What is the group actually trying to accomplish?
- What **genuinely remains unknown or blocked**, not merely unpublished?
- Why does resolving it matter? State the chain:
  **unknown/bottleneck → inability to predict/control/build → scientific/technological consequence**.
- What does a PhD student actually do day to day?
- What did 2–3 recent students model, simulate, code, build, measure, optimize or deploy?
- Does the student touch a **real physical/system experiment**, or only offline data/simulation?
- What is the likely loop: model → experiment → inference/debug → refinement?
- What implementation ownership exists?
- What scientific outcome and engineering outcome can the thesis produce?
- What transferable capability remains if the exact thesis topic becomes obsolete?
- Where do graduates go?
- What evidence exists about PI technical depth, teaching/mentoring engagement and student autonomy?
- What is the admissions/funding structure and how plausible is it for the user's profile?
- Does the work preserve/develop valuable C/C++/DSP/optimization/systems skills where relevant?

Do not infer advisor quality, field impact, or student experience from fame or citation count alone.

### Evidence quality

Use the existing labels consistently:

- **Deeply researched** — repeated project/group-level investigation with strong primary-source grounding; mission, loop, student work, risks and remaining diligence are understood.
- **Moderate** — group direction is credible, but thesis loop/current openings/student/advisor evidence still needs another pass.
- **Preliminary** — broad ecosystem, uncertain mapping, or limited project-level evidence; not decision-grade.

Never promote to Deeply researched merely because a paragraph was written.

## PhD value filters

A project should strongly satisfy at least one:

1. **Fundamental physics:** genuinely unresolved physical phenomenon; output is new physical understanding.
2. **Physics blocking an important technology:** resolving the mechanism improves ability to predict/control/build an important technology.
3. **Deep transferable R&D capability:** physical/system modelling, simulation, experimental inference, inverse problems/parameter estimation, signal processing, optimization, numerical/HPC, measurement/instrumentation, or hardware/software co-design.

Avoid elevating narrow/incremental publishable niches with neither important new physics nor valuable transferable capability.

Also evaluate:
- worth solving / problem importance;
- long investigation timescale and potential 10–20 year technical thread;
- implementation ownership;
- scientific and engineering outcome potential;
- industry optionality;
- full-stack integration;
- advisor/learning confidence based on evidence;
- group field impact with explicit evidence;
- admissions practicality separately from intrinsic research quality.

## Frozen scoring model

Unless the user explicitly changes the weights, preserve this intrinsic-fit model.

### Technical core — 40%
- Physics: **9%**
- Modelling & Simulation: **8%**
- Inference / Estimation: **7%**
- Algorithms: **4%**
- Computational Optimization: **5%**
- Systems Implementation: **4%**
- Experiment / Measurement: **3%**

Technical Flavor Fit is a summary only and receives **0% additional weight** to avoid double-counting.

### Problem / thesis value — 40%
- Problem Importance: **10%**
- Unknown / Bottleneck Clarity: **6%**
- Why-it-matters Chain: **6%**
- Transferable R&D Capability: **5%**
- Implementation Ownership: **4%**
- Scientific Outcome Potential: **4%**
- Engineering Outcome Potential: **3%**
- Industry Optionality: **2%**

### Time / integration / advisor — 20%
- Long Horizon: **8%**
- Full-stack Fit: **4%**
- Advisor / Learning Confidence: **8%**

Excluded from intrinsic fit:
- Technical Flavor Fit summary;
- Group Field Impact;
- h-index;
- Institution visibility/prestige;
- admissions difficulty.

Rating conversion:
- Very high / Very strong / S = 10
- High / Strong / A = 9
- Medium / Promising / B = 8
- Low–Medium = 7.5
- Low / C = 7
- Unknown/verify ≈ 8 when a numerical fallback is unavoidable.

### Research-next priority

This is **diligence priority**, not intrinsic research quality:
- Target/Safer: **+0.35**
- Target: **+0.20**
- Reach/Target: **+0.08**
- Reach: **−0.05**
- Unknown: **0**

Do not let admissions make a lab intrinsically “better”; it only changes where diligence effort is most useful.

## Holistic Attention

Attention is intentionally selective and is the main **where should I spend research time now?** field.

- **Highest** — cherry-picked primary targets deserving immediate deep investigation. Keep this small, roughly **8–12 out of ~100**, not “all excellent labs.”
- **High** — genuine contenders worth full profiles; also selective, roughly the next **15–25**.
- **Medium** — retained for coverage; not current-focus shortlist.

Holistic Attention synthesizes **all factors**, not just Base Overall Score: technical weighting, actual mission/loop, fundamental-vs-engineering character, problem importance, long horizon, implementation ownership, admissions practicality, evidence confidence, background bridge, transferable capability and industry optionality.

Whenever a candidate is promoted to Highest:
- require a full deep profile;
- compare it explicitly against existing Highest candidates;
- if the Highest bucket grows beyond the intended cherry-picked range, reconsider who should fall to High;
- do not promote simply because a lab is prestigious.

Interconnect groups must be evaluated at **project level**, not dismissed as “integrated photonics.” Distinguish device/fabrication-heavy projects from system-level work spanning link/device physics → modelling → architecture/DSP/control → integration/testbed → measurement/debug.

Likewise, broad fusion/HEDP facilities are ecosystems, not single research agendas. Map to the actual PI/project before assigning decision-grade fit.

## Deep profiles

For Highest and serious High candidates, profiles should cover:
1. What the group actually is / mission.
2. Specific bottleneck and why it matters.
3. Actual likely PhD research loop.
4. Fit to the user's technical identity.
5. Implementation/experiment ownership evidence.
6. Recent student/thesis evidence where available.
7. Long-horizon scientific + engineering outcomes.
8. Industry/career bridge.
9. Admissions/practical structure.
10. Advisor/learning evidence.
11. Main risks / project-selection caveats.
12. Evidence checked and date.

A profile must distinguish **group-level evidence** from assumptions about a specific future project.

## Admissions labels

Treat these as profile-calibrated planning estimates, not acceptance probabilities:
- Reach
- Reach/Target
- Target
- Target/Safer
- Unknown

There is no true “Safety” for PI-funded PhDs. Unknown means insufficient admissions evidence, not poor fit.

## HTML/UI invariants — do not break

The database is a feature-rich workbook. Preserve:
- all existing rows/columns unless intentionally changed;
- grouped header bands and correct colspans;
- column filters and search;
- score-range filters;
- S/A/B/C and numeric color coding;
- editable Adjustment in ±0.2 steps and Final score recomputation;
- editable user category/comments where present;
- localStorage persistence;
- JSON import/export if present;
- internal deep-profile navigation;
- sticky headers;
- seven frozen Identity columns;
- desktop wide introductory prose/cards;
- horizontal scrolling/table usability.

### Frozen columns / resizing

The seven frozen identity columns are delicate. Current behavior stores their widths under:
`phdMasterFrozenWidthsV2`.

Rules:
- Resize only the intended frozen columns unless a broader resize system is deliberately engineered and tested.
- Do **not** force the whole table into `table-layout: fixed` as a shortcut; a previous attempt broke the layout.
- After any width change, recompute/check sticky left offsets and the divider after University.
- Newly merged rows must carry the same group/frozen classes as existing rows.
- Test at ordinary desktop zoom after CSS/JS changes.
- Do not reintroduce the old mobile pinch-zoom / `visualViewport` sticky-header workaround; it previously broke the page. Prefer conservative native CSS sticky behavior.

## Safe modification rules

- Do not replace the current HTML with an older “cleaner” version.
- Do not infer that a missing field means it can be dropped.
- Do not rename columns casually: JS and data attributes may depend on exact names.
- When inserting columns, update grouped-header colspans, filter row, body cells, JS index/field mappings and any score logic.
- When adding rows, ensure every row has the exact current number/order of cells and the expected classes/data attributes.
- When editing scoring JS, verify Base, Adjustment and Final independently.
- Preserve user-entered/localStorage semantics across releases where possible.
- For major structural changes, first make a local/test copy, validate it, then update canonical `index.html`.
- Prefer targeted DOM/data edits over regex/string replacement for structural HTML changes.

## Quality gate before pushing

At minimum verify programmatically:
- body row count;
- header column count;
- every row cell count == header count;
- grouped-header colspan sum == column count;
- filter-row cell count == column count;
- every `.profile-link` target exists;
- every filter field used by JS has corresponding row data where required;
- all Highest candidates have a working deep profile;
- Attention distribution remains intentionally selective;
- no duplicate PI/group rows were accidentally introduced;
- HTML contains the expected scoring weights;
- canonical `index.html` still contains the existing JS/CSS/localStorage machinery.

For UI/JS edits, also inspect the rendered page or otherwise test the affected interaction before claiming it is fixed.

## GitHub Pages update discipline

Normal update:
1. fetch `index.html`;
2. edit and validate;
3. update `index.html` on `main` using its current blob SHA;
4. use a descriptive commit message;
5. verify the committed file and, when feasible, the Pages result.

Do not create `index_v2.html`, `latest_final.html`, etc. The permanent Pages URL should remain stable.

## Reporting

After an update, report concisely:
- what rows/profiles/UI logic changed;
- any score/attention changes;
- validation counts/results;
- evidence-quality limitations or unresolved diligence;
- commit/Pages status.

Never say “fixed” solely because the file wrote successfully. Validate the relevant behavior first.
