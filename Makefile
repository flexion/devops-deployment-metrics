.PHONY: help install test coverage lint audit xdoctest docs docs-serve benchmark typecheck

help:  ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*//' | while read target; do \
		grep "^$$target:.*##" $(MAKEFILE_LIST) | sed 's/^[^#]*## */  /' | sed "s/^/$$target: /"; \
	done

install:  ## Install dependencies using uv sync --all-groups
	uv sync --all-groups

test:  ## Run tests with coverage tracking
	uv run coverage run --parallel -m pytest --no-nox

coverage:  ## Generate coverage report
	@if find . -maxdepth 1 -name '.coverage.*' -print -quit | grep -q .; then \
		uv run coverage combine; \
	fi
	uv run coverage report

lint:  ## Lint code using pre-commit
	uv run pre-commit run --all-files --hook-stage=manual --show-diff-on-failure

audit:  ## Audit dependencies for vulnerabilities
	uv run pip-audit

xdoctest:  ## Run doctest examples
	uv run python -m xdoctest --modname=devops_deployment_metrics --command=all

docs:  ## Build documentation
	@rm -rf docs/_build
	uv run --group docs sphinx-build docs docs/_build

docs-serve:  ## Build and serve documentation with live reloading
	@rm -rf docs/_build
	uv run --group docs sphinx-autobuild --open-browser docs docs/_build

benchmark:  ## Run performance benchmarks
	uv run pytest --benchmark-json=benchmark-output.json tests/test_metrics.py tests/test_config.py

typecheck:  ## Type-check code using mypy
	uv run mypy src tests docs/conf.py
