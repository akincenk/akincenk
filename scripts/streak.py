"""Build assets/streak{,-dark}.svg from USER's contribution calendar (last year).

Replaces streak-stats.demolab.com, which kept timing out and showed a broken image."""
import json, os, urllib.request
from datetime import date, timedelta

USER = "akincenk"
TOKEN = os.environ.get("LANGS_TOKEN") or os.environ.get("GITHUB_TOKEN")
QUERY = """query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date contributionCount}}}}}}"""


def calendar():
    body = json.dumps({"query": QUERY, "variables": {"u": USER}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", body,
                                 {"Authorization": f"Bearer {TOKEN}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        cal = json.load(r)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = [(d["date"], d["contributionCount"]) for w in cal["weeks"] for d in w["contributionDays"]]
    return cal["totalContributions"], sorted(days)


def streaks(days, today):
    """Current streak counts back from today; a quiet today does not break it yet."""
    counts = dict(days)
    longest = run = 0
    for _, n in days:
        run = run + 1 if n else 0
        longest = max(longest, run)
    d = date.fromisoformat(today)
    if not counts.get(today):
        d -= timedelta(days=1)
    current = 0
    while counts.get(d.isoformat()):
        current += 1
        d -= timedelta(days=1)
    return current, longest


def svg(total, current, longest, dark):
    fg, sub, bg = ("#e6edf3", "#8b949e", "#0d1117") if dark else ("#24292f", "#57606a", "#ffffff")
    cols = ((total, "Contributions", "last 12 months"), (current, "Current streak", "days"),
            (longest, "Longest streak", "days, last 12 months"))
    body = "".join(
        f'<text x="{x}" y="75" font-size="28" font-weight="600" fill="{"#2f81f7" if i == 1 else fg}">{v:,}</text>'
        f'<text x="{x}" y="105" font-size="13" fill="{fg}">{a}</text>'
        f'<text x="{x}" y="125" font-size="11" fill="{sub}">{b}</text>'
        for i, (v, a, b) in enumerate(cols) for x in [80 + i * 160])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="165" viewBox="0 0 480 165">'
            f'<rect width="480" height="165" rx="6" fill="{bg}"/>'
            f'<g font-family="Segoe UI,Ubuntu,sans-serif" text-anchor="middle">{body}</g></svg>\n')


assert streaks([("2026-01-01", 1), ("2026-01-02", 2), ("2026-01-03", 0), ("2026-01-04", 1)], "2026-01-05") == (1, 2)
assert streaks([("2026-01-01", 1), ("2026-01-02", 1)], "2026-01-02") == (2, 2)

if __name__ == "__main__":
    total, days = calendar()
    current, longest = streaks(days, days[-1][0])
    os.makedirs("assets", exist_ok=True)
    for dark, path in ((False, "assets/streak.svg"), (True, "assets/streak-dark.svg")):
        with open(path, "w") as f:
            f.write(svg(total, current, longest, dark))
    print(total, current, longest)
