# Experiments

This folder contains VibeOps experiments — structured tests that validate changes to AGENTS.md, Skills, or the benchmark before they're merged.

## Structure

```
experiments/
  001-agents-md-v2/       — first validated experiment
  002-skills-split/       — in progress
  ...
```

## What Goes in an Experiment

Each experiment folder contains:
- `hypothesis.md` — what we're testing and why
- `results.md` — what happened, pass/fail, evidence
- `diff.md` — what changed in AGENTS.md or Skills as a result

## Convention

- Experiments are numbered sequentially
- A merged experiment = validated change
- A failed experiment = its findings still get documented (failures are data)
