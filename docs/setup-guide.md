# Van Cooldown Multi-Environment Setup Guide

## Overview

This project uses **UV** for modern Python package management with **local virtual environments** per component for better isolation and organization.

## Architecture

```
van-cooldown/
├── docs/                    # Documentation component
│   ├── .venv/               # Local virtual environment
│   └── pyproject.toml       # Documentation dependencies
├── software/backend/        # Backend component
│   ├── .venv/               # Local virtual environment
│   └── pyproject.toml       # Backend dependencies
└── tools/scripts/           # Cross-platform management tools
    └── manage_envs.py       # Environment management script
```

## Installation

### Prerequisites

1. **Python 3.13+** installed
2. **UV** package manager: `pip install uv`

### Quick Setup

```bash
# Install UV
pip install uv

# Set up all environments
python tools/scripts/manage_envs.py setup --all

# Check status
python tools/scripts/manage_envs.py status
```

### Manual Setup

#### Documentation Environment

```bash
cd docs
uv sync
uv run mkdocs --version
```

#### Backend Environment

```bash
cd software/backend
uv sync
uv run pytest --version
uv run ruff --version
uv run python -m mypy --version
```

## Environment Status

Current setup includes:
- **docs**: MkDocs Material + quality tools (PySpelling, Proselint, Linkchecker)
- **software/backend**: FastAPI + testing tools (pytest, mypy, ruff)

## Usage Commands

### Documentation

```bash
# From docs/ directory
uv run mkdocs serve          # Start development server
uv run mkdocs build          # Build static site
uv run pyspelling            # Spell check
uv run proselint docs/       # Prose linting
```

### Backend

```bash
# From software/backend/ directory
uv run pytest               # Run tests
uv run ruff check           # Lint code
uv run ruff format          # Format code
uv run python -m mypy .     # Type checking
```

### Cross-Platform Management

```bash
# From project root
python tools/scripts/manage_envs.py status    # Show environment status
python tools/scripts/manage_envs.py setup --component docs    # Setup specific component
python tools/scripts/manage_envs.py setup --all              # Setup all components
```

## VS Code Integration

The project includes comprehensive VS Code tasks in `.vscode/tasks.json`:

- **Setup tasks**: Environment initialization
- **Build tasks**: Documentation building
- **Test tasks**: Running tests across components
- **Lint tasks**: Code quality checks

Access via `Ctrl+Shift+P` → "Tasks: Run Task"

## Benefits

- ✅ **Isolation**: Each component has its own dependencies
- ✅ **Organization**: Virtual environments stored locally in component directories
- ✅ **Modern tooling**: UV for fast dependency resolution
- ✅ **Cross-platform**: Works on Windows, Linux, macOS
- ✅ **IDE Integration**: Full VS Code support
- ✅ **Quality tools**: Comprehensive linting, formatting, and testing

## Privacy-First Documentation

The documentation is configured for privacy compliance:
- ❌ No cookies or tracking
- ❌ No external analytics
- ✅ Local development and static hosting ready
- ✅ GDPR compliant by design
