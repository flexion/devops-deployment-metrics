# 13. Automated Dependency Management with Renovate

## Status

Accepted

## Context

Outdated dependencies are a source of risk to any software project. Main risks include security vulnerabilities, outdated performance issues and the danger of bit rot as time goes by.

For a software project where development happens in bursts, it is even more important to keep the dependencies up to date during time periods where there are not human eyes on the project.

In the absence of automation, the ongoing process of dependency upgrades introduce considerable toil for the development team. Since dependency upgrades follow a fairly deterministic workflow, this is a prime candidate for automation. The good news is, there are several automation tools available.

## Decision

Use [Renovatebot](https://www.mend.io/renovate/) to automate dependency management. We decided Renovatebot meet our needs better than `snyk`. Below, each piece of Renovatebot high-level functionality is
discussed in it's own section.

We feel confident in automated dependency management because we are confident in our automated tests and security scans, as well as our option-enabling software architecture.

### Automerging and Handling Different Levels of Upgrades

As part of working to reduce toil and needless human intervention, we have configured Renovatebot to create PRs with needed updates, which then allows the CI checks to run. If these CI checks pass, it then hits a decision branch point:

- If the patches are changing a semver major version, the PR is created but left for a human to merge.
- If the patches are changing a semver minor version, the PR is automerged, but only after a few days.
- If the patches are changing a semver patch version, the PR is automerged.

This scheme allows us to balance the competing needs of taking an appropriate amount of caution for each change on the project's main branch, but also reducing the amount of human effort needed to do low risk tasks. It was decided that for minor
and patch version, the risk of breakage was sufficiently low and the coverage of our CI checks is sufficiently high to allow Renovate to merge without human intervention reducing toil. For Major versions, which are far more rare, it was
decided that
it was worth the effort to have a human grant final approval. However, the human effort in this case is still very low, just minimally merging the PR, as Renovatebot still creates and tests the PR for the human.

### Noise Reduction with Scheduling and Batching

In order to keep the automated dependency PRs from overwhelming the humans, we apply scheduling and batching strategies to reduce the noise.

Renovatebot has been configured to be active during times outside the normal working time of the development team, so dependency management automation happens during night and weekends.

All patch dependency upgrades are grouped together in one PR, while all minor dependency upgrades are grouped in another. Major version upgrades each get their own PR, but these occur at a much lower frequency.

### Pinning (deterministic builds)

Using explicit versions of libraries and other dependencies (actions, Docker images, ...) makes your builds deterministic and adds certainty to your process and code. Any point in time in your repository will yield reproducible build results when you pin your dependencies. Renovate encourages this and automates the maintenance of dependency updates.

### Pinning actions (security)

Pinning versions using a full length commit SHA is important because you want to know that you are using a GitHub action that was created by a trusted source. This is a security concern beyond automation, but there is a strategy for supporting pinning to SHA hashes instead of only the semver for actions. Renovatebot supports a special tag in a comment so SHA pinning can be used to guarantee the provenance of an action, while supporting major/minor/patch update rules, using the `# tag=<version>` comment in action workflow files.

```yaml
uses: actions/checkout@2541b1294d2704b0964813337f33b291d3f8596b # tag=v3
```

## Consequences

We'll need to handle manual PR approval for major versions and when proposed updates break the build.
