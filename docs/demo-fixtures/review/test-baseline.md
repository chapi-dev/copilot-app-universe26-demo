<!-- universe26-dashboard-fixture:v1:review:03 -->
# [DEMO] Document expected cart test failures

> Explicitly requested demonstration fixture. This is documentation, not a cart bug fix or proof that an app feature is enabled.

## Purpose

Explain the deliberate baseline without hiding failures or claiming a fix.

## Presenter notes

- Run python -m pytest sample-app to inspect the actual current result.
- On the unfixed baseline, test_subtotal passes.
- test_discount_never_negative fails because a discount can produce a negative total.
- test_total_rounded_to_cents fails because the floating-point total is not rounded.
- Report additional failures separately; these documentation fixtures do not repair the bugs.

## Integrity

- The cart implementation, existing tests, and workflows are unchanged.
- The two deliberate cart failures remain part of the unfixed baseline.
- This fixture must not be presented as a completed product feature.
- Publishing the fixture does not authorize merging or further automation runs.
