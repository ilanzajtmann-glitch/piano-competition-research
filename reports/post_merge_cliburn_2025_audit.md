# Independent GitHub-repository audit: Van Cliburn 2025 v1

Date: 2026-07-05
Role: independent scientific auditor, not dataset engineer.

## Audit objective

The objective was to prove that the committed GitHub repository is wrong. The audit was required to start from a fresh `git clone` of the committed GitHub branch into a completely new directory, inspect only that clone, and avoid reusing local regenerated files or previous validation results.

## Critical audit blocker

**Result: FAIL.**

I could not complete the mandatory independent GitHub audit because this checkout has no configured GitHub remote URL, and no repository URL was available from the environment.

Commands run from the existing checkout:

```sh
$ git config --get remote.origin.url
# no output

$ git remote -v
# no output

$ gh repo view --json url
# no repository resolved
```

Because there is no GitHub remote URL, I cannot perform the required first step:

```sh
git clone <github-url> <fresh-directory>
```

Therefore I cannot truthfully claim that the actual committed GitHub repository, GitHub raw rendering, or the PR branch has been independently verified.

## Why this is a hard failure

The instruction requires auditing the actual committed GitHub repository, not the current local checkout. Without a clone URL, any local `wc -l`, parser, or byte-level result would only test the current workspace and would not answer the scientific question: whether the committed GitHub branch is physically correct in GitHub/raw view.

Consequently, the following required checks are **not independently verified against GitHub**:

- physical line count of the committed GitHub files;
- Raw GitHub rendering of `cliburn_2025_candidates.csv`;
- Raw GitHub rendering of `cliburn_2025_results.csv`;
- embedded newline status in GitHub blobs;
- LF-only status in GitHub blobs;
- one physical row per record in GitHub blobs;
- CSV quoting in the committed GitHub branch;
- duplicate rows/candidates/works in the committed GitHub branch;
- missing source URLs in the committed GitHub branch;
- round, winner, and feature consistency in the committed GitHub branch;
- consistency between this audit report and the actual committed GitHub data.

## Failed tests

| Test | Required evidence | Observed result | Verdict |
| --- | --- | --- | --- |
| Resolve GitHub remote URL | `git config --get remote.origin.url` or equivalent URL | No output | FAIL |
| List Git remotes | `git remote -v` | No output | FAIL |
| Resolve repository through GitHub CLI | `gh repo view --json url` | No repository resolved | FAIL |
| Fresh clone committed branch | `git clone <github-url> <fresh-directory>` | Not possible without URL | FAIL |
| Verify Raw GitHub CSV line counts | Raw GitHub files and `wc -l` from fresh clone | Not possible without clone | FAIL |

## Local checkout observations are not sufficient

The current local checkout may show correct physical line counts, but those observations are intentionally excluded from the final verdict because the mandatory audit target is the committed GitHub repository. Local evidence cannot disprove the user's Raw GitHub observation that:

- `cliburn_2025_candidates.csv` has 1 physical line in Raw GitHub;
- `cliburn_2025_results.csv` has 3 physical lines in Raw GitHub;
- prize fields still contain broken line breaks in Raw GitHub.

## Remaining uncertainties

All substantive dataset-quality questions remain unresolved for the committed GitHub repository until a fresh clone of the PR branch can be performed from a concrete GitHub URL.

## Recommendation

**FAIL.**

Do not merge. Provide the exact GitHub repository URL and PR branch/ref, then rerun the audit from a fresh clone. Only after the fresh clone shows the required raw physical checks, especially:

```sh
wc -l data/cleaned/cliburn_2025_candidates.csv  # expected 29
wc -l data/cleaned/cliburn_2025_results.csv     # expected 29
```

should logical validation or any PASS recommendation be considered.
