<!-- universe26-dashboard-fixture:v1:review:06 -->
# [DEMO] Add the safe demo reset checklist

> Explicitly requested demonstration fixture. This is documentation, not a cart bug fix or proof that an app feature is enabled.

## Purpose

Repeat a rehearsal without discarding unrelated work or merging demonstration fixtures.

## Presenter notes

- Use a fresh worktree from the intended base commit for each repeat.
- Preserve useful diffs and generated artifacts before cleaning up a session.
- Do not run a hard reset or blanket restore in the preparation checkout.
- Leave demonstration PRs unmerged and the three original demo issues open.
- Close or delete fixtures only after a separate cleanup decision.

## Integrity

- The cart implementation, existing tests, and workflows are unchanged.
- The two deliberate cart failures remain part of the unfixed baseline.
- This fixture must not be presented as a completed product feature.
- Publishing the fixture does not authorize merging or further automation runs.
