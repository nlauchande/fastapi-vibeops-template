# VibeOps FastAPI Template — Roadmap

> This roadmap is evidence-based. Each phase is validated through live experiments before being marked complete.
> Governance as a feedback loop, not a one-time document.

---

## ✅ Phase 0 — Foundation (Complete)

| Issue | Description | Status |
|-------|-------------|--------|
| #3 | Setup public VibeOps org (`vibeops-central`) | ✅ Done |
| #4 | Launch `vibeopscentral.ai` website | ✅ Done |
| #5 | Move template repo to `vibeops-central` org | ✅ Done |
| #6 | AGENTS.md v2 — 7 gotchas from live experiment | ✅ Merged |

---

## 🔄 Phase 1 — Agent Modularity (Next)

**Issue #1 — Split agent into core + Skills**

The current AGENTS.md is a monolith. As the template grows, agents loading the full file for every task becomes wasteful and noisy.

**Proposed design:**
- `AGENTS.md` → core governance layer (architecture rules, hard constraints, workflow protocol)
- `skills/` → pluggable modules loaded on demand:
  - `skills/auth.md` — JWT, bcrypt, session patterns
  - `skills/crud.md` — repository + service patterns for standard resources
  - `skills/background.md` — Celery, Redis, task queue conventions
  - `skills/migrations.md` — Alembic rules and gotchas

**Why it matters:**
- Agents load only what's relevant to the current task
- Each skill is independently testable via the benchmark (Phase 3)
- New skills can be contributed without touching core governance

---

## 📊 Phase 2 — Observability (MLflow)

**Issue #2 — Integrate MLflow Agentic Visibility**

VibeOps claims to make AI governance measurable. This phase makes that real.

**What gets tracked:**
- Which AGENTS.md version was active
- Which prompt triggered the feature kickoff
- Which model was used (Claude Sonnet 4.5, etc.)
- Test pass rate, coverage %, gotchas respected
- Time from prompt → green tests

**Output:** A `vibecheck` score per run — a single number representing governance effectiveness.

**Why it matters:**
- Every AGENTS.md change has a measurable before/after
- Teams can compare scores across projects and versions
- The score becomes the VibeOps adoption metric

---

## 🤖 Phase 3 — Auto Research (Benchmark)

**New — `vibeops-benchmark` script**

Formalises the manual experiment we ran during AGENTS.md v2 development:

```
clone fresh template
→ run standard feature prompts
→ measure: tests passing, deps correct, status codes, coverage
→ compute VibeOps Score
→ compare against baseline
→ flag regressions → open PR with suggested AGENTS.md fix
```

**This is VibeOps Auto Research** — the governance document improves itself through empirical testing, not just human intuition.

Inspired by Karpathy's agentic loop concept: hypothesis → experiment → measure → update → repeat.

---

## 🔮 Future / Backlog

- GitHub Actions CI: run benchmark on every PR to main
- Multi-model benchmark: compare Claude vs GPT-4o vs Gemini on same prompts
- Public leaderboard: VibeOps Score by project, model, AGENTS.md version
- Community skill contributions via `vibeops-central/skills` repo

---

## Contribution

Found a gotcha? Run an experiment. Open a PR with:
1. What failed
2. What rule you added
3. Before/after test results

That's VibeOps.
