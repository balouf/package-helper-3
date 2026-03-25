# LLM-Assisted Maintenance

:::{admonition} This page will age quickly
LLM tooling evolves rapidly. This page reflects practices as of early 2026.
The general principles should remain relevant, but specific tools and commands will change.
:::

Maintaining a Python package involves a mix of mechanical tasks (updating dependencies,
modernizing CI, fixing linting) and judgment calls (API design, release decisions,
deprecation policies). LLMs are remarkably effective at the first category and increasingly
useful — but not autonomous — for the second.

## What LLMs Excel At

### Routine maintenance

Dependency updates, CI workflow modernization, Python version matrix adjustments,
pre-commit hook upgrades. These follow well-known patterns that LLMs handle reliably.

### Code review and refactoring

"Is there dead code?", "Are there unused imports?", "Can this function be simplified?"
— LLMs are good at spotting these issues across a codebase. They can also apply
refactorings consistently (e.g. renaming a function everywhere it appears).

### Documentation

Writing docstrings, README sections, changelog entries, and tutorial prose.
LLMs produce clean first drafts that need human editing for accuracy and tone,
but save significant time compared to starting from scratch.

### Boilerplate generation

GitHub Actions workflows, configuration files, test scaffolding, CI/CD setup.
These follow established patterns and LLMs produce working versions quickly.

### Migration assistance

Moving from Poetry to UV, from `setup.py` to `pyproject.toml`, from one CI
provider to another. LLMs can read the old configuration and produce the new one,
handling the tedious mapping of options.

## What Humans Must Do

### Review all diffs

LLMs over-engineer. They add error handling for impossible cases, create abstractions
for one-time operations, and "improve" code that was fine. **Read every diff before
committing.** If a change seems unnecessary, it probably is.

### Make architectural decisions

Which Python versions to support, when to make breaking changes, how to structure
the public API — these require understanding the users, the ecosystem, and the
project's goals. LLMs can inform these decisions with data, but should not make them.

### Verify compatibility claims

When an LLM says "this is compatible with Python 3.10+", verify it. When it says
"this dependency version is safe to upgrade", check the changelog. LLMs are confident
but not always correct about version compatibility.

### Test before releasing

LLMs can run tests, but they cannot judge whether the test suite is adequate.
After LLM-assisted changes, run the full test suite, check CI, and do a manual
smoke test before releasing.

### Final review before publishing

Never let an LLM make a PyPI release autonomously. The release checklist
(version bump, changelog, tag, publish) should always have a human in the loop.

## Cost-Effective Split

The most efficient workflow mirrors what works for any LLM collaboration:

- **LLM for the 90% mechanical work**: dependency updates, CI modernization,
  linting fixes, documentation drafts, boilerplate, migration scaffolding.
- **Human for the 10% requiring judgment**: API design, version policy,
  release decisions, security review, user-facing documentation tone.

The LLM produces the first draft; the human reviews, corrects, and makes
structural decisions. Total effort is a fraction of doing everything manually,
with human time focused where it matters most.

## Practical Tips

### Custom maintenance routines

Most LLM coding tools support custom commands or prompt templates. You can create
a reusable maintenance routine that systematically reviews your package's health.
A good routine covers:

- **Build system and tooling** — is the package using current best practices?
- **Python version support** — does CI test at least the last four stable minor versions?
- **Dependency health** — are there outdated or unused dependencies?
- **CI/CD configuration** — are action versions current? Is the deployment modern?
- **Code quality** — linting, dead code, test coverage.
- **Documentation** — are docstrings present? Is the README up to date?

The routine should present findings grouped by effort (quick wins, medium-term,
long-term) and **wait for human approval** before making any changes.

### Commit frequently

After each logical group of LLM-assisted changes, commit. This creates save
points you can revert to if a later change breaks something. It also makes
the git history readable: each commit should be one coherent change.

### One concern at a time

Resist the temptation to fix everything in one session. Process one category
of changes (e.g. "update all CI workflows") before moving to the next.
This keeps diffs reviewable and rollbacks clean.

### Working with Claude Code

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) is a CLI tool
that can assist with package maintenance. A few features are particularly useful:

- **CLAUDE.md**: Create a `CLAUDE.md` file at the root of your package with
  project-specific instructions (coding conventions, things to avoid, architectural
  decisions). Claude Code reads this file automatically and uses it as context.
- **Plan mode**: For non-trivial changes (build system migration, major refactoring),
  use plan mode. This forces a discussion before any code is written, which catches
  misunderstandings early.
- **Custom commands**: You can define reusable prompts as markdown files in
  `~/.claude/commands/` (global) or `.claude/commands/` (per-project). This is
  how you would implement a maintenance routine like the one described above.

## Anti-Patterns to Avoid

- **Blindly accepting suggestions.** LLMs will happily add type annotations to
  your entire codebase, refactor working code, or add features you did not ask for.
  Always check that changes match what you requested.
- **Trusting version claims.** "This works with Python 3.10" is an assertion, not a fact.
  Check CI results.
- **Skipping tests after LLM changes.** LLMs do not always predict side effects correctly.
  Run the full test suite.
- **Over-relying on LLMs for security.** LLMs can spot obvious issues (hardcoded secrets,
  SQL injection) but are not a substitute for proper security review of sensitive code.
- **Letting sessions drag on.** If an LLM is going in circles or making the same mistake
  repeatedly, stop, rethink the approach, and start a fresh session with clearer context.
