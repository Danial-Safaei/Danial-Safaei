"""Render the README metrics strip from the website's live data.

Single source of truth: https://danial-safaei.github.io/data/scholar.json
(citation metrics, refreshed from Google Scholar by the website's own Action)
and data/publications.json (the curated publication list, whose length is the
"works" count). This script writes assets/metrics-light.svg,
assets/metrics-dark.svg and the matching alt text in README.md, touching the
files only when something changed. Standard library only; on any fetch or
parse error it exits 0 and leaves everything as it is.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from datetime import date
from html import escape
from pathlib import Path

SITE = "https://danial-safaei.github.io"
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

SANS = "-apple-system,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,monospace"

THEMES = {
    "light": {
        "bg": "#ffffff", "border": "#d8dee6", "rule": "#e2e5ea",
        "label": "#6c6e73", "value": "#45464a", "note2": "#83868d",
        "metrics": ["#2563eb", "#7c3aed", "#0f766e", "#be123c"],
        "grad": ("#7c3aed", "#2563eb"), "ytd": "#2563eb", "ytd_fill": "0.35", "ytd_stroke": "0.65",
    },
    "dark": {
        "bg": "#0d1117", "border": "#2a2c31", "rule": "#2a2c31",
        "label": "#8b8d92", "value": "#b7b8bb", "note2": "#6f727a",
        "metrics": ["#8ab4ff", "#c1a4ff", "#63d8cc", "#ff9eb3"],
        "grad": ("#c1a4ff", "#8ab4ff"), "ytd": "#8ab4ff", "ytd_fill": "0.45", "ytd_stroke": "0.7",
    },
}


def log(message: str) -> None:
    print(f"[render_metrics] {message}")


def fetch_json(path: str) -> dict:
    request = urllib.request.Request(f"{SITE}/{path}", headers={"Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def describe(m: dict, today: date) -> tuple[str, str]:
    """Return (svg aria-label, README alt text)."""
    years = m["years"]
    per_year = m["perYear"]
    ytd_year = str(today.year)
    parts_label = [f"{per_year[y]} {'so far in' if y == ytd_year else 'in'} {y}" for y in years]
    parts_alt = [f"{per_year[y]} ({y}{' to date' if y == ytd_year else ''})" for y in years]
    head = (f"{m['citations']} citations, h-index {m['hIndex']}, "
            f"i10-index {m['i10Index']}, {m['works']} works")
    label = (f"Research metrics: {head}. Citations per year: {', '.join(parts_label)}. "
             f"Source: Google Scholar, {m['month']}.")
    alt = f"{head}. Citations per year: {', '.join(parts_alt)}. Source: Google Scholar."
    return label, alt


def render_svg(m: dict, theme: dict, today: date) -> str:
    label, _ = describe(m, today)
    c = theme
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="132" viewBox="0 0 1000 132" '
        f'role="img" aria-label="{escape(label)}">',
        "  <defs>",
        '    <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">',
        f'      <stop offset="0" stop-color="{c["grad"][0]}"/>',
        f'      <stop offset="1" stop-color="{c["grad"][1]}"/>',
        "    </linearGradient>",
        "  </defs>",
        "",
        f'  <rect x="0.5" y="0.5" width="999" height="131" rx="10" fill="{c["bg"]}" stroke="{c["border"]}"/>',
        "",
        f'  <g font-family="{SANS}">',
    ]
    metrics = [("CITATIONS", m["citations"]), ("H-INDEX", m["hIndex"]),
               ("i10-INDEX", m["i10Index"]), ("WORKS", m["works"])]
    for (name, value), x, colour in zip(metrics, (46, 178, 286, 404), c["metrics"]):
        out.append(f'    <text x="{x}" y="56" font-size="30" font-weight="700" fill="{colour}">{value}</text>')
        out.append(f'    <text x="{x}" y="76" font-size="9.5" letter-spacing="1.7" font-family="{MONO}" '
                   f'fill="{c["label"]}">{name}</text>')
    out += [
        "  </g>",
        "",
        f'  <line x1="516" y1="26" x2="516" y2="106" stroke="{c["rule"]}"/>',
        "",
        f'  <text x="558" y="24" font-family="{MONO}" font-size="9.5" letter-spacing="1.7" '
        f'fill="{c["label"]}">CITATIONS PER YEAR</text>',
        "",
        f'  <g font-family="{MONO}" font-size="9" fill="{c["label"]}">',
    ]
    years = m["years"]
    peak = max([m["perYear"][y] for y in years] + [1])
    ytd_year = str(today.year)
    for i, year in enumerate(years):
        value = m["perYear"][year]
        x = 562 + 62 * i
        centre = x + 14
        height = max(round(value / peak * 47), 3)
        top = 95 - height
        out.append(f'    <text x="{centre}" y="{top - 6}" text-anchor="middle" fill="{c["value"]}">{value}</text>')
        if year == ytd_year:
            out.append(f'    <rect x="{x}" y="{top}" width="28" height="{height}" rx="2.5" fill="{c["ytd"]}" '
                       f'opacity="{c["ytd_fill"]}" stroke="{c["ytd"]}" stroke-opacity="{c["ytd_stroke"]}"/>')
        else:
            out.append(f'    <rect x="{x}" y="{top}" width="28" height="{height}" rx="3" fill="url(#bar)"/>')
        out.append(f'    <text x="{centre}" y="110" text-anchor="middle">{year}</text>')
    out += [
        "  </g>",
        "",
        f'  <line x1="556" y1="95.5" x2="790" y2="95.5" stroke="{c["rule"]}"/>',
        "",
    ]
    if years and years[-1] == ytd_year:
        out.append(f'  <text x="812" y="60" font-family="{SANS}" font-size="10.5" '
                   f'fill="{c["label"]}">{ytd_year} is year to date.</text>')
    out.append(f'  <text x="812" y="77" font-family="{SANS}" font-size="10.5" '
               f'fill="{c["note2"]}">Source: Google Scholar</text>')
    out.append(f'  <text x="812" y="94" font-family="{SANS}" font-size="10.5" '
               f'fill="{c["note2"]}">Updated {m["month"]}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def write_if_changed(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    log(f"updated {path.relative_to(ROOT)}")
    return True


def main() -> int:
    try:
        scholar = fetch_json("data/scholar.json")
        pubs = fetch_json("data/publications.json").get("publications", [])
        per_year = {str(k): int(v) for k, v in scholar["perYear"].items()}
        updated = date.fromisoformat(scholar["updated"])
        m = {
            "citations": int(scholar["citations"]),
            "hIndex": int(scholar["hIndex"]),
            "i10Index": int(scholar["i10Index"]),
            "works": len(pubs) or int(scholar.get("works", 0)),
            "perYear": per_year,
            "years": sorted(per_year)[-4:],
            "month": f"{MONTHS[updated.month - 1]} {updated.year}",
        }
        if m["citations"] <= 0 or not m["years"]:
            raise ValueError("implausible metrics")
    except Exception as exc:
        log(f"could not read the website data, leaving files untouched: {exc}")
        return 0

    today = date.today()
    for name, theme in THEMES.items():
        write_if_changed(ROOT / "assets" / f"metrics-{name}.svg", render_svg(m, theme, today))

    _, alt = describe(m, today)
    readme = README.read_text(encoding="utf-8")
    new_readme = re.sub(r'(<img alt=")[^"]*(" src="assets/metrics-light\.svg")',
                        lambda x: x.group(1) + escape(alt) + x.group(2), readme)
    write_if_changed(README, new_readme)
    return 0


if __name__ == "__main__":
    sys.exit(main())
