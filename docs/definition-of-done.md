# Definition of Done

We use a definition of done to ensure quality in every user story. In principle,
we should be able to "continuously deploy", meaning when we complete each story,
the system must be in a production-ready state. No one should say "Oh. We can't
deploy until we…"

However, for practical reasons, sometimes we can't complete a separate instance of
each for every user story. For example, usability tests may occur more at a feature
level than at an individual story level. What is important is that no user story
should be considered done until it has been included in a passing usability test.
In these cases, the user stories stay "in progress" or some other not-done column
until every criteria is checked off.

The default definition of done listed below should be tailored to meet the needs and
requirements of each project. In short, **everything that can be done incrementally
should be done incrementally**, while the context and details are fresh. If it's
inefficient or "hard" to do so, the team should figure out *why* and add OPEX/DEVEX
backlog items to make it easier and more efficient.

1. **Acceptance criteria met** - Verify every acceptance criterion in the linked issue is satisfied. Note any deviations or intentional descoping in the PR description.
1. **Usability validated** - Demo the working change to at least one other team member and confirm it is easy to use. Note N/A for non-interactive changes.
1. **Design QA passed** - Verify all visual UI matches the agreed design. Include screenshot evidence in the PR if the UI changed.
1. **Browser interaction verified** *(when applicable)* - For any story that introduces a browser-only interaction, manually verify the interaction works at `localhost:8000` in a real browser. Add automated tests if there is an installed framework like `playwright`. Note N/A for non-browser changes.
1. **Accessibility checks passed** *(when applicable)* - Note N/A for non-UI changes.
1. **Prod measurement identified** - Define the production signal or metric that confirms success before merging. Note it in the PR description. Note N/A only if the change has no observable production effect.
1. **Code refactored for clarity** - After tests pass, refactor until a reviewer can understand the change without asking questions. No "I'll clean this up later" commits.
1. **Dependency Rule followed** - Confirm that more important code (domain) does not directly import less important code (adapters). Violated imports block merge.
1. **Development debt eliminated** - Remove any technical debt introduced by the change. If intentional debt cannot be avoided, open a tracking issue and link it in the PR.
1. **Source code merged** - Code has been merged into the main branch.
1. **Automated quality checks passed** - Run tests and linters. All pre-commit hooks pass. All CI/CD passes.
1. **Code reviewed** - At least one other team member has approved the PR before merge.
1. **Security and threat model reviewed** - Review `docs/threat_model.md` and confirm whether new data flows, external integrations, secrets, permissions, or attack surfaces are introduced; update the threat model when they are. Document the threat model outcome in the PR description ("threat model: no new threats — X is covered by existing Y" or "threat model: updated section Z").
1. **Build process updated** - Update CI/CD to include any new build steps, test targets, or pipeline stages the story introduces. Confirm N/A if the pipeline is unchanged.
11. **Load/performance tests passed** - Confirm performance tests cover the new functionality. Add or update tests if load-sensitive paths changed. Note N/A for changes with no performance impact.
1. **README.md updated** - Document any user-facing CLI behavior change with examples. Note N/A if no CLI or operator-visible behavior changed.
1. **Configuration guide updated** - If this story adds or changes a TOML config section, add or update the matching entry in the configuration guide. Note N/A if no config surface changed. 
1. **ADRs created** - Write an ADR for every significant architectural decision (new external dependency, new layer, new pattern). If unsure, err toward writing one. Note N/A with a brief reason if no decision was made.
