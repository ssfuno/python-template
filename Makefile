.PHONY: help lint format fix check setup

help:
	@echo "Usage: make <target>"
	@echo
	@echo "Available targets:"
	@echo "  help    Show this help"
	@echo "  setup   Set up the development environment"
	@echo "  lint    Run ruff lint checks (runs 'uv check')"
	@echo "  format  Format source files with ruff (runs 'uv format')"
	@echo "  fix     Try to automatically fix lint issues (runs 'uv check --fix')"
	@echo "  check   Run lint + formatting checks"

lint:
	@echo "==> Running ruff lint checks"
	uv run ruff check .

format:
	@echo "==> Formatting source with ruff"
	uv run ruff format .

fix:
	@echo "==> Attempting to auto-fix issues with ruff"
	uv run ruff check --fix .

check:
	@echo "==> Running lint and format checks"
	uv run ruff check .
	uv run ruff format --check .

setup:
	@echo "==> Setting up development environment"
	uv sync --dev
	@echo "==> Installing pre-commit hooks"
	uv run pre-commit install
