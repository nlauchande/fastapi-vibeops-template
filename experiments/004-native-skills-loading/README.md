# Experiment 004 — Native Claude Code Skills Loading (.claude/skills/)

**Date:** 2026-03-22
**Branch:** feat/7-agents-core-skills-split
**Status:** ✅ Validated

---

## Background

Experiments 002 and 003 showed ~100s design overhead vs the 60s baseline. Root causes identified:
1. Skills in `skills/` not discovered natively by Claude Code (wrong path)
2. Explicit load instruction in AGENTS.md caused eager loading of all skill files upfront
3. Previous implement times (~4 min) were SIGTERM artefacts — actual implementation was ~54s

This experiment moves skills to `.claude/skills/` (native Claude Code path) and removes the explicit load instruction, letting Claude Code handle progressive disclosure natively.

---

## Hypothesis

Using `.claude/skills/` + removing explicit load instruction will:
1. Enable native Claude Code skill discovery
2. Maintain quality (≥17 tests, zero manual fixes)
3. Reveal true implement time (previously masked by SIGTERM)

---

## Changes from Experiment 003

- Skills copied to `.claude/skills/auth|testing|migrations|crud/SKILL.md`
- AGENTS.md Feature Kickoff Protocol updated: removed explicit "load skills from skills/" instruction → replaced with "activate relevant Skills" (lets Claude Code decide)

---

## Method

1. Fresh clone of `feat/7-agents-core-skills-split`
2. Design phase: `New feature: user registration and JWT authentication` — timed
3. Implement phase: `proceed` — timed with **900s timeout** (fix for previous SIGTERM artefacts)
4. Run tests cold — zero manual intervention

---

## Results

| Metric | Exp 002 | Exp 003 | **Exp 004** |
|--------|---------|---------|------------|
| Tests passing | 18 / 18 | 14 / 14 | **17 / 17** |
| Manual fixes | 0 | 0 | **0** |
| Coverage | 83% | 83% | **85%** |
| Design time | 102s | 95s | **105s** |
| Implement time | ~4min* | ~4min* | **54s** |
| VibeOps Score | 96.6 | 96.5 | **97.0** |

*\* Previous implement times were SIGTERM artefacts — process killed at 4min timeout while Claude Code was writing output summary after implementation was already complete.*

---

## Key Finding: SIGTERM Was Masking True Implement Time

The 4-minute implement times in Exp 001–003 were not actual implementation duration. Timeline:
```
0s   → Claude Code starts implementation
~54s → Implementation complete (all files written)
54s–240s → Claude Code writing summary, running tests, composing commit message
240s → SIGTERM (exec timeout killed the process)
```

**True implement time: ~54 seconds.** The 900s timeout revealed this.

---

## Key Finding: Design Time Overhead Is Real

Design phase is consistently 95–105s across Exp 002–004, vs ~60s in Exp 001 (no skills). The overhead is the agent reading SKILL.md content — progressive disclosure (metadata-only at startup) is not yet reducing this because Claude Code still reads full skill files when activated.

This is a Bedrock-specific limitation: the skills `load` tool call that fetches full content on demand may behave differently on direct Anthropic API vs Bedrock.

---

## Conclusion

**Hypothesis confirmed.** Native `.claude/skills/` loading works — skills are discovered and applied correctly. 17/17 tests, 85% coverage, zero manual fixes. Best VibeOps Score yet (97.0).

Design overhead (~40s vs baseline) is an open question for further investigation.

---

## Artefacts

- Branch: `feat/7-agents-core-skills-split`
- PR: [#10](https://github.com/vibeops-central/fastapi-vibeops-template/pull/10)
