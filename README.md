# Bounty Bench fixture library

`bountybench_slugify.normalize_slug` is a deliberately small, testable code-bounty fixture. The base branch has a real normalization bug: repeated hyphens and hyphens at the edges survive. The `hunter-a` through `hunter-e` branches are pinned claim examples; each commit body carries a `Bounty-Claimant` trailer used by the demo contract.

Branches `hunter-d` and `hunter-e` contain the complete fix and a regression test. `hunter-b` fixes the function without adding a test. `hunter-c` adds an instruction-like comment while leaving the behavior broken. `hunter-a` points at Hunter D's commit so the front-run case fails the address trailer check.

Run the branch tests with Python 3.11 or later:

```bash
python -m unittest discover -s tests -v
```

