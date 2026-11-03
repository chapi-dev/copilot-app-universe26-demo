# 2. Parallelize work with Projects

**Goal:** one coordinator splits work across isolated child sessions.

## Setup
Create three issues from the `demo-task` template:
1. Fix discount going negative (`sample-app/src/cart.py`)
2. Fix rounding of totals (`sample-app/src/cart.py`)
3. Add a usage section to `sample-app` docs and a CLI stub

## Steps
1. Create a Project for this repo.
2. Prompt the coordinator:
   > Look at the open issues labelled `demo`. Start one session per issue, each in its own worktree, and report back when done.
3. Show the sessions list: each has its own branch/worktree and status.
4. Review one result, redirect another with a follow-up message.

## Talking points
- Isolation: each child works in its own worktree, so no conflicts while running.
- You supervise and decide; the coordinator tracks status.
