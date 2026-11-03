# 1. Work smarter with Copilot Fusion

**Goal:** show that the same task can be routed to different model strategies and compare the outcome.

## Setup
`sample-app` has a failing test `test_discount_never_negative`.

## Steps
1. Open two sessions on this repo.
2. Session A: model **Auto**, lowest tier (efficiency). Session B: Auto with the **Fusion** tier (if listed in the picker).
3. Same prompt in both:
   > Fix the failing test in sample-app without changing the tests. Explain the root cause in 3 lines.
4. Compare: time, diff size, explanation quality, extra edge cases covered.

## Talking points
- Pick the tier per task: cheap for mechanical work, Fusion/intelligence for ambiguous bugs.
- Same prompt, same repo: only the strategy changes.

## Reset
`git restore .` in each worktree.
