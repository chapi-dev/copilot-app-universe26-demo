# 3. Automate recurring work

**Goal:** show recurring work that runs on a schedule, in two flavours.

## A. Copilot app Automations (agent runs a prompt on a schedule)
Prompts are ready in [`/automations`](../../automations):
- `daily-triage.md` – daily: summarise new issues/PRs, label, propose next actions
- `weekly-dependency-check.md` – weekly: check outdated deps and prepare a PR
- `flaky-test-watch.md` – manual/hourly: re-run tests and report flakiness

Steps: Automations view -> New -> paste prompt -> pick interval (use *manual* for the demo) -> **Run now** -> open the session it created.

## B. GitHub Actions (deterministic, in this repo)
- `.github/workflows/ci.yml` – tests on every push/PR
- `.github/workflows/nightly-health.yml` – nightly run; opens an issue labelled `demo` if tests fail

Trigger live: Actions tab -> *Nightly health* -> **Run workflow**.

## Talking points
- Actions = deterministic pipelines. Automations = judgement-based recurring tasks. Use both.
- Each automation run starts a fresh session you can review.
