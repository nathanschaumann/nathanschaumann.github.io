"""Checks every short link on the live site: the redirect page exists, points at the right target,
and the target itself loads. Usage: python3 check.py [base URL, default https://nschaumann.com]"""
import json, sys, pathlib, urllib.request, urllib.parse

base = (sys.argv[1] if len(sys.argv) > 1 else "https://nschaumann.com").rstrip("/")
links = json.loads((pathlib.Path(__file__).parent / "links.json").read_text())

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "short-link-check"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.status, r.geturl(), r.read().decode("utf-8", "replace")

bad = 0
for name, target in links.items():
    try:
        status, _, body = get(f"{base}/{name}/")
        assert status == 200, f"short page returned {status}"
        assert f'url={target}"' in body, "short page points somewhere else"
        tstatus, final, _ = get(urllib.parse.urljoin(base + "/", target))
        assert tstatus == 200, f"target returned {tstatus}"
        print(f"OK   {base}/{name} -> {final}")
    except Exception as e:
        bad += 1
        print(f"FAIL {base}/{name}: {e}")
sys.exit(1 if bad else 0)
