#!/usr/bin/env python3
"""Apply the latest considered-candidate decisions to the master database HTML."""
from __future__ import annotations

import json
import re
from html import escape
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "index.html"
DATA = ROOT / "considered_candidates.json"
STATUSES = {
    "Retained problem-led",
    "Conditional project",
    "Evidence pending",
    "Pruned fit",
    "Reference only",
}
CAPS = {
    "Conditional project": "Medium",
    "Evidence pending": "Watch",
    "Pruned fit": "Low",
    "Reference only": "Watch",
}
ATTENTION_ORDER = {"Low": 0, "Watch": 1, "Medium": 2, "High": 3, "Highest": 4}


def latest_decision(candidate: dict) -> dict:
    latest = candidate.get("latest")
    decisions = candidate.get("decisions")
    if isinstance(latest, dict):
        return latest
    if isinstance(decisions, list) and decisions:
        # For same-date corrections, the last appended decision is authoritative.
        return max(enumerate(decisions), key=lambda pair: (str(pair[1].get("date", "")), pair[0]))[1]
    if isinstance(decisions, dict):
        return decisions
    raise ValueError(f"Candidate {candidate.get('key')!r} has no latest decision")


def add_controls(source: str) -> str:
    if ".screening-badge{" not in source:
        anchor = ".small{color:var(--muted);font-size:.9rem}"
        style = ".screening-badge{display:block;width:max-content;max-width:100%;margin-top:4px;padding:1px 6px;border-radius:9px;background:#edf2f6;font-size:.78rem;line-height:1.45}"
        if source.count(anchor) != 1:
            raise ValueError("Could not locate the base small-text style exactly once")
        source = source.replace(anchor, anchor + style, 1)
    if ".screening-attention-note{" not in source:
        anchor = ".screening-badge{"
        style = ".screening-attention-note{display:block;margin-top:3px;color:var(--muted);font-size:.82rem;line-height:1.3}"
        at = source.find(anchor)
        if at < 0:
            raise ValueError("Could not locate screening badge style for attention note style")
        end = source.find("}", at) + 1
        source = source[:end] + style + source[end:]
    if 'id="screening-filter"' not in source:
        anchor = '<button id="program-rank"'
        if source.count(anchor) != 1:
            raise ValueError("Could not locate the program-rank control exactly once")
        control = (
            '<label>Pruning disposition <select id="screening-filter">'
            '<option value="focus">Focus: retained problem-led</option>'
            '<option value="conditional">Conditional project</option>'
            '<option value="pending">Evidence pending</option>'
            '<option value="pruned">Pruned fit</option>'
            '<option value="reference">Reference only</option>'
            '<option value="all">All dispositions</option></select></label>'
        )
        source = source.replace(anchor, control + anchor, 1)
    if "function screeningFilterOK(r)" not in source:
        anchor = "function programFilterOK(r){"
        start = source.find(anchor)
        if start < 0:
            raise ValueError("Could not locate programFilterOK")
        end = source.find("\n}\n", start) + 3
        if end < 3:
            raise ValueError("Could not locate end of programFilterOK")
        js = '''
function screeningFilterOK(r){
  const v=document.querySelector('#screening-filter')?.value||'focus';
  const status=r.dataset.screening||'';
  if(v==='all')return true;
  if(v==='focus')return status==='Retained problem-led';
  if(v==='conditional')return status==='Conditional project';
  if(v==='pending')return status==='Evidence pending';
  if(v==='pruned')return status==='Pruned fit';
  if(v==='reference')return status==='Reference only';
  return true;
}
document.querySelector('#screening-filter').addEventListener('change',filt);
'''
        source = source[:end] + js + source[end:]
    source = source.replace(
        "&&programFilterOK(r);",
        "&&programFilterOK(r)&&screeningFilterOK(r);",
        1,
    )
    clear_old = "document.querySelector('#clear').onclick=()=>{document.querySelector('#q').value='';document.querySelectorAll('.menu input').forEach(x=>x.checked=false);filt()};"
    clear_new = "document.querySelector('#clear').onclick=()=>{document.querySelector('#q').value='';document.querySelectorAll('.menu input').forEach(x=>x.checked=false);document.querySelector('#screening-filter').value='focus';document.querySelector('#program-filter').value='all';filt()};"
    if clear_old in source:
        source = source.replace(clear_old, clear_new, 1)
    if "const screeningCandidateKey=new URLSearchParams(location.search).get('candidate');" not in source:
        deep_link = '''
<script>
const screeningCandidateKey=new URLSearchParams(location.search).get('candidate');
if(screeningCandidateKey){
  const target=document.getElementById('candidate-'+screeningCandidateKey);
  if(target){
    document.querySelector('#q').value='';
    document.querySelectorAll('.menu input').forEach(x=>x.checked=false);
    document.querySelector('#screening-filter').value='all';
    document.querySelector('#program-filter').value='all';
    filt();
    requestAnimationFrame(()=>target.scrollIntoView({block:'center',behavior:'smooth'}));
  }
}
</script>
'''
        source = source.replace("</body>", deep_link + "</body>", 1)
    return source


def main() -> None:
    if not DATA.exists():
        raise SystemExit(f"Required decision file is missing: {DATA.name}")
    data = json.loads(DATA.read_text(encoding="utf-8"))
    candidates = data.get("candidates")
    if not isinstance(candidates, list):
        raise SystemExit("considered_candidates.json must contain a candidates array")
    source = HTML.read_text(encoding="utf-8")
    soup = BeautifulSoup(source, "html.parser")
    db_rows = {row.get("data-key"): row for row in soup.select("#db tbody tr[data-key]")}
    decisions: dict[str, dict] = {}
    for candidate in candidates:
        key = candidate.get("key")
        if not key or key in decisions:
            raise SystemExit(f"Missing or duplicate candidate key: {key!r}")
        decision = latest_decision(candidate)
        status = decision.get("status")
        if status not in STATUSES:
            raise SystemExit(f"{key}: unsupported screening status {status!r}")
        decisions[key] = decision
    missing = sorted(set(db_rows) - set(decisions))
    if missing:
        raise SystemExit(
            "Every master database row needs a screening decision; "
            f"missing={missing[:12]}{'…' if len(missing)>12 else ''}"
        )

    # Update just candidate row fragments so the surrounding hand-authored HTML stays intact.
    for key, decision in decisions.items():
        if key not in db_rows:
            continue  # A project-scoped entry lives in the considered register only.
        row = db_rows[key]
        row["id"] = "candidate-" + key
        row["data-screening"] = decision["status"]
        row["data-screening-reason"] = str(decision.get("reason", ""))
        prior_cap = row.get("data-original-attention-cap")
        if prior_cap is None:
            prior_cap = row.get("data-attention-cap", "")
            row["data-original-attention-cap"] = prior_cap
        caps = [cap for cap in (prior_cap, CAPS.get(decision["status"]), decision.get("attention_cap")) if cap]
        invalid_caps = [cap for cap in caps if cap not in ATTENTION_ORDER]
        if invalid_caps:
            raise SystemExit(f"{key}: invalid attention cap(s): {invalid_caps}")
        if caps:
            row["data-attention-cap"] = min(caps, key=lambda cap: ATTENTION_ORDER[cap])
        else:
            row.attrs.pop("data-attention-cap", None)
        if "data-original-attention" not in row.attrs:
            row["data-original-attention"] = row.get("data-attention", "")
        cap = row.get("data-attention-cap")
        current_tier = row.get("data-attention-review") or row.get("data-original-attention") or row.get("data-attention")
        effective_tier = current_tier
        if cap in ATTENTION_ORDER and current_tier in ATTENTION_ORDER:
            if ATTENTION_ORDER[current_tier] > ATTENTION_ORDER[cap]:
                effective_tier = cap
        row["data-attention"] = effective_tier
        attention_cell = row.select_one(".attention-tier")
        if attention_cell:
            attention_cell.string = effective_tier
            classes = [c for c in attention_cell.get("class", []) if c not in {"att-highest", "att-high", "att-medium"}]
            tier_class = {"Highest": "att-highest", "High": "att-high", "Medium": "att-medium"}.get(effective_tier)
            if tier_class:
                classes.append(tier_class)
            attention_cell["class"] = classes
        attention_reason = row.select_one(".attention-reason")
        if attention_reason:
            for previous_note in attention_reason.select(".screening-attention-note"):
                previous_note.decompose()
            if cap:
                note = soup.new_tag("span")
                note["class"] = ["screening-attention-note"]
                note.string = f"Screening status: {decision['status']} · attention capped at {cap} pending project, ownership, or route verification."
                attention_reason.append(note)
        cells = row.find_all("td", recursive=False)
        person_cell = cells[4] if len(cells) > 4 else None
        if person_cell is None:
            raise SystemExit(f"{key}: expected person/PI cell at column 5")
        old_badge = person_cell.select_one(".screening-badge")
        if old_badge:
            old_badge.decompose()
        badge = soup.new_tag("a", href=f"considered_candidates.html?candidate={key}")
        badge["class"] = ["screening-badge", "small"]
        badge["title"] = str(decision.get("reason", "Open screening decision"))
        badge.string = str(decision["status"])
        person_cell.append(badge)
        pattern = re.compile(
            r"<tr\b(?=[^>]*\bdata-key=[\"']" + re.escape(key) + r"[\"'])[^>]*>.*?</tr>",
            re.DOTALL,
        )
        source, count = pattern.subn(str(row), source, count=1)
        if count != 1:
            raise SystemExit(f"Could not update source row for {key}")

    counts = Counter(decisions[key]["status"] for key in db_rows)
    if 'id="screening-summary"' not in source:
        audit = BeautifulSoup(source, "html.parser").select_one("#problem-solving-audit")
        if audit is None or str(audit) not in source:
            raise SystemExit("Could not locate #problem-solving-audit card for summary insertion")
        summary = soup.new_tag("div", attrs={"class": "card", "id": "screening-summary"})
        summary.append(soup.new_tag("strong"))
        summary.strong.string = "Current problem-led screening"
        p = soup.new_tag("p")
        p.append('Working identity: “Owner of a difficult real problem who is willing and able to descend all the way into fundamental research when the problem demands it.” The status is about whether the direction survives this filter; it does not certify student ownership or an available route. Unknown evidence stays pending rather than counting as rejection.')
        summary.append(p)
        counts_p = soup.new_tag("p", attrs={"class": "small", "id": "screening-counts"})
        counts_p.string = "Latest decisions: " + " · ".join(
            f"{status}: {counts[status]}" for status in sorted(STATUSES)
        )
        summary.append(counts_p)
        summary.append(BeautifulSoup(
            '<p><a href="considered_candidates.html"><b>Open the pruned register</b></a> (opens on Pruned fit by default) · '
            '<a href="considered_candidates.html?status=all"><b>View all dispositions and audit history</b></a></p>',
            "html.parser",
        ))
        source = source.replace(str(audit), str(audit) + str(summary), 1)

    # Refresh the existing summary count on every run, even when the card already exists.
    count_text = "Latest decisions: " + " · ".join(
        f"{status}: {counts[status]}" for status in sorted(STATUSES)
    )
    count_pattern = re.compile(
        r"<p\b(?=[^>]*\bid=[\"']screening-counts[\"'])[^>]*>.*?</p>", re.DOTALL
    )
    count_match = count_pattern.search(source)
    if not count_match:
        raise SystemExit("Screening summary count element is missing")
    count_element = '<p class="small" id="screening-counts">' + escape(count_text) + "</p>"
    source = source[:count_match.start()] + count_element + source[count_match.end():]

    # Update stale hand-authored row count and all new behavior in the existing script.
    source = re.sub(r"Database — \d+ candidate rows", f"Database — {len(db_rows)} candidate rows", source, count=1)
    source = add_controls(source)
    HTML.write_text(source, encoding="utf-8")
    register_only = len(decisions) - len(db_rows)
    print(
        f"Applied latest screening decisions to {len(db_rows)} master rows"
        + (f" ({register_only} project-scoped register-only entries validated)." if register_only else ".")
        + " Master-row statuses: "
        + ", ".join(f"{s}={counts[s]}" for s in sorted(STATUSES))
    )


if __name__ == "__main__":
    main()
