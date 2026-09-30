# nathanschaumann.github.io

Serves nschaumann.com (custom domain since 2026-09-30; DNS at Cloudflare, domain verified in GitHub settings).
Short links for resumes, e.g. `nschaumann.com/tests` -> the proficiency tests. The list lives in `links.json`.

1. Edit `links.json` (short name -> target path or URL). Don't reuse the name of a project repo.
2. `python3 build.py` regenerates the redirect pages (and removes ones no longer listed).
3. Commit and push; after GitHub Pages publishes (~1 min), `python3 check.py` must print OK for every link.
