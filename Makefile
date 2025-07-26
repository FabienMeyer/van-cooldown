# Van Cooldown Documentation Makefile
# Manages Python environment, linting, and documentation building

.PHONY: help install clean lint vale spell markdown-lint prose-lint build serve dev quality-check all

# Default target
help: ## Show this help message
	@echo "Van Cooldown Documentation Makefile"
	@echo "===================================="
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Environment setup
install: ## Set up Python environment with UV
	@echo "🐍 Setting up Python environment with UV..."
	@if ! command -v uv >/dev/null 2>&1; then \
		echo "❌ UV not found. Please install UV first:"; \
		echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"; \
		exit 1; \
	fi
	@echo "✅ UV is available"
	@echo "📦 Installing dependencies..."
	uv sync --all-extras
	@echo "✅ Python environment setup complete!"

# Vale setup
vale-sync: ## Sync Vale packages and styles
	@echo "📝 Syncing Vale packages..."
	-uv run vale sync
	@echo "✅ Vale sync complete!"

# Cleaning
clean: ## Clean build artifacts and cache
	@echo "🧹 Cleaning build artifacts..."
	rm -rf site/
	rm -rf .uv-cache/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	@echo "✅ Clean complete!"

# Linting targets
spell: install ## Run spell checking
	@echo "🔤 Running spell check..."
	uv run python scripts/spell_check.py

vale: install vale-sync ## Run Vale prose linting
	@echo "📝 Running Vale prose linting..."
	uv run vale src/

markdown-lint: install ## Run markdown linting with pymarkdown
	@echo "📋 Running markdown linting..."
	uv run pymarkdown scan src/

prose-lint: install ## Run prose linting with proselint
	@echo "✍️  Running prose linting..."
	uv run proselint src/

# Combined linting
lint: spell vale markdown-lint prose-lint ## Run all linting checks

# Quality check with detailed output
quality-check: install ## Run comprehensive quality checks
	@echo "🔍 Running comprehensive quality checks..."
	@echo "=================================="
	@echo ""
	@echo "1/4 - Spell Check"
	@echo "------------------"
	@if uv run python scripts/spell_check.py; then \
		echo "✅ Spell check passed"; \
	else \
		echo "❌ Spell check failed"; \
		exit 1; \
	fi
	@echo ""
	@echo "2/4 - Vale Prose Linting"
	@echo "-------------------------"
	@if uv run vale src/; then \
		echo "✅ Vale prose linting passed"; \
	else \
		echo "❌ Vale prose linting failed"; \
		exit 1; \
	fi
	@echo ""
	@echo "3/4 - Markdown Linting"
	@echo "----------------------"
	@if uv run pymarkdown scan src/; then \
		echo "✅ Markdown linting passed"; \
	else \
		echo "❌ Markdown linting failed"; \
		exit 1; \
	fi
	@echo ""
	@echo "4/4 - Prose Linting"
	@echo "-------------------"
	@if uv run proselint src/; then \
		echo "✅ Prose linting passed"; \
	else \
		echo "❌ Prose linting failed"; \
		exit 1; \
	fi
	@echo ""
	@echo "🎉 All quality checks passed!"

# Documentation building
build: install ## Build the documentation
	@echo "🏗️  Building documentation..."
	uv run mkdocs build --clean
	@echo "✅ Documentation build complete!"

serve: install ## Serve documentation locally
	@echo "🚀 Starting development server..."
	@echo "📝 Documentation will be available at http://localhost:8000"
	uv run mkdocs serve

# Development workflow
dev: install build ## Set up development environment and build docs
	@echo "🚀 Development environment ready!"
	@echo ""
	@echo "Next steps:"
	@echo "  make serve     - Start development server"
	@echo "  make lint      - Run all linting checks"
	@echo "  make build     - Build documentation"

# Full pipeline
all: clean install quality-check build ## Run complete pipeline: clean, install, check, build
	@echo "🎉 Complete pipeline finished successfully!"
	@echo ""
	@echo "📁 Built documentation is in: site/"
	@echo "🌐 Run 'make serve' to start development server"

# Verification targets
verify: ## Verify all tools are working
	@echo "🔍 Verifying installation..."
	@echo "Testing MkDocs..."
	@if uv run mkdocs --version >/dev/null 2>&1; then \
		echo "✅ MkDocs is working"; \
	else \
		echo "❌ MkDocs check failed"; \
		exit 1; \
	fi
	@echo "Testing spell checker..."
	@if uv run python scripts/spell_check.py --help >/dev/null 2>&1; then \
		echo "✅ Spell checker is working"; \
	else \
		echo "❌ Spell checker check failed"; \
		exit 1; \
	fi
	@echo "Testing proselint..."
	@if uv run proselint --version >/dev/null 2>&1; then \
		echo "✅ Proselint is working"; \
	else \
		echo "❌ Proselint check failed"; \
		exit 1; \
	fi
	@echo "Testing pymarkdown..."
	@if uv run pymarkdown version >/dev/null 2>&1; then \
		echo "✅ PyMarkdown is working"; \
	else \
		echo "❌ PyMarkdown check failed"; \
		exit 1; \
	fi
	@echo "Testing Vale..."
	@if uv run vale --version >/dev/null 2>&1; then \
		echo "✅ Vale is working"; \
	else \
		echo "❌ Vale check failed"; \
		exit 1; \
	fi
	@echo "🎉 All tools verified successfully!"

# Docker targets (if you want to keep Docker workflow)
docker-build: ## Build Docker image for documentation
	@echo "🐳 Building Docker image..."
	docker-compose build docs-lint

docker-lint: ## Run linting in Docker
	@echo "🐳 Running linting in Docker..."
	docker-compose run --rm docs-lint make lint

docker-serve: ## Serve documentation using Docker
	@echo "🐳 Starting documentation server in Docker..."
	docker-compose up docs-serve
