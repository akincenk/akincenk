"""Build assets/top-langs{,-dark}.svg from public, non-fork repos of USER."""
import json, os, urllib.request
from collections import Counter
from html import escape

USER = "akincenk"
TOP = 6
COLORS = {"Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
          "HTML": "#e34c26", "CSS": "#663399", "Shell": "#89e051", "Dockerfile": "#384d54",
          "Jupyter Notebook": "#DA5B0B", "Go": "#00ADD8", "Swift": "#F05138", "Mako": "#7e858d"}


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def totals():
    repos = get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner")
    c = Counter()
    for r in repos:
        if not r["fork"] and not r["archived"]:
            c.update(get(r["languages_url"]))
    return c


def svg(langs, dark):
    fg, bg = ("#e6edf3", "#0d1117") if dark else ("#24292f", "#ffffff")
    total = sum(n for _, n in langs)
    w, x, bar = 380, 25, ""
    for name, n in langs:
        seg = (w - 50) * n / total
        bar += f'<rect x="{x:.1f}" y="45" width="{seg:.1f}" height="8" fill="{COLORS.get(name, "#8b949e")}"/>'
        x += seg
    rows = ""
    for i, (name, n) in enumerate(langs):
        cx, cy = 25 + (i % 2) * 170, 80 + (i // 2) * 25
        rows += (f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{COLORS.get(name, "#8b949e")}"/>'
                 f'<text x="{cx + 15}" y="{cy}">{escape(name)} {100 * n / total:.1f}%</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="165" viewBox="0 0 {w} 165">'
            f'<rect width="{w}" height="165" rx="6" fill="{bg}"/>'
            f'<g font-family="Segoe UI,Ubuntu,sans-serif" fill="{fg}">'
            f'<text x="25" y="30" font-size="18" font-weight="600">Most Used Languages</text>'
            f'<g font-size="12">{rows}</g></g>'
            f'<clipPath id="c"><rect x="25" y="45" width="{w - 50}" height="8" rx="4"/></clipPath>'
            f'<g clip-path="url(#c)">{bar}</g></svg>\n')


if __name__ == "__main__":
    langs = totals().most_common(TOP)
    assert langs, "no languages found"
    os.makedirs("assets", exist_ok=True)
    for dark, path in ((False, "assets/top-langs.svg"), (True, "assets/top-langs-dark.svg")):
        with open(path, "w") as f:
            f.write(svg(langs, dark))
    print(langs)
