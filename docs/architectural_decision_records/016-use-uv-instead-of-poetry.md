# Replace Poetry with uv for Dependency Management

## Context

Our project previously used **Poetry** for dependency management, packaging, and versioning. While Poetry provides a comprehensive toolset for Python projects, we identified several pain points:

- **Performance**: Poetry can be slow, particularly in resolving dependencies and managing lockfiles.
- **Complexity**: The Poetry CLI has a large feature set, but we were primarily using it for dependency management and builds, making some features redundant.
- **Compatibility**: Our project needs fast, reliable dependency management with reproducible builds, and we are looking for a more minimalistic and modern solution.

**uv** from **astal.sh** is a new Python packaging tool designed to simplify dependency management, improve performance, and provide reproducible builds with a straightforward workflow.

## **Decision**

We will replace **Poetry** with **uv** for managing dependencies, creating lockfiles, and building the project.

## Alternatives Considered

1. **Continue Using Poetry**

   - Pros:
     - Well-established and widely adopted in the Python community.
     - Comprehensive feature set.
   - Cons:
     - Slower dependency resolution and build times.
     - More complex than needed for our current workflow.

2. **Switch to pip-tools**

   - Pros:
     - Lightweight toolset for managing dependencies.
     - Works well with native `pip`.
   - Cons:
     - No built-in support for project metadata (PEP 621).
     - Requires additional tools to handle building and packaging.

3. **Adopt uv** (Chosen)
   - Pros:
     - Faster dependency resolution and lockfile creation.
     - Native support for `pyproject.toml` and PEP 621.
     - Minimalistic and modern toolchain.
   - Cons:
     - Newer tool with a smaller community compared to Poetry.
     - Requires some workflow adjustments (e.g., versioning).

## Consequences

### Positive Impacts

- **Faster Builds**: `uv` provides faster dependency resolution and package builds.
- **Simplified Workflow**: The tool is more aligned with our goal of a lean, efficient build process.
- **Reproducible Builds**: uv generates a `uv.lock` file to ensure consistent environments across installations.

### Negative Impacts

- **Learning Curve**: Team members need to become familiar with uv’s CLI.
- **Ecosystem**: `uv` is a newer tool, so it may have fewer third-party resources and integrations compared to Poetry.

## Status

Approved

## **Consequences of Not Making This Change**

- Continued slow builds and dependency resolution times.
- Complexity in maintaining our dependency management workflows.
- Potential frustration with overly complex tooling for our use case.
