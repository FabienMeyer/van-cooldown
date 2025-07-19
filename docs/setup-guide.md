# Van Cooldown Documentation Setup Guide

## Overview

This project supports **two development approaches** for documentation:

1. **🐳 Docker-based** (Recommended): Consistent environment with all tools pre-installed
2. **🐍 Local UV-based**: Local virtual environments with UV package management

## 🐳 Docker-Based Development (Recommended)

### Prerequisites

- **Docker** installed and running
- **Git** for version control

### Quick Start with Docker

```bash
cd docs

# Build the documentation container
./docker-docs.sh build           # Linux/macOS
.\docker-docs.ps1 build          # Windows PowerShell

# Start development server
./docker-docs.sh serve           # Linux/macOS  
.\docker-docs.ps1 serve          # Windows PowerShell

# Visit http://localhost:8000
```

### Docker Commands

```bash
# Development workflow
./docker-docs.sh build           # Build container with all tools
./docker-docs.sh serve           # Start dev server (localhost:8000)
./docker-docs.sh docs            # Build static documentation
./docker-docs.sh lint            # Run quality checks
./docker-docs.sh linkcheck       # Check documentation links
./docker-docs.sh clean           # Clean up artifacts

# Using Docker Compose (alternative)
docker-compose up                # Start development server
docker-compose --profile build up docs-build     # Build docs
docker-compose --profile lint up docs-lint       # Run quality checks
```

### Included Tools in Docker Container

- ✅ **MkDocs Material** - Documentation framework
- ✅ **PySpelling** - Spell checking
- ✅ **Proselint** - Prose quality checking
- ✅ **Linkchecker** - Link validation
- ✅ **markdownlint-cli** - Markdown linting
- ✅ **Vale** - Advanced prose linting
- ✅ **@axe-core/cli** - Accessibility testing

## 🐍 Local UV-Based Development

### Prerequisites

1. **Python 3.13+** installed
2. **UV** package manager: `pip install uv`

### Quick Setup

```bash
cd docs
uv sync                          # Install dependencies
uv run mkdocs serve              # Start development server
```

### Local UV Commands

```bash
# From docs/ directory
uv run mkdocs serve          # Start development server
uv run mkdocs build          # Build static site
uv run pyspelling            # Spell check
uv run proselint src/        # Prose linting
uv run linkchecker site/     # Link checking (after build)
```

## Monorepo Multi-Environment Setup

The project also supports **multiple local virtual environments** for different components:

### Architecture

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

### Backend Environment

```bash
cd software/backend
uv sync                      # Install dependencies
uv run pytest               # Run tests
uv run ruff check           # Lint code
uv run ruff format          # Format code
uv run python -m mypy .     # Type checking
```

### Cross-Platform Management

```bash
# From project root
python tools/scripts/manage_envs.py status              # Show environment status
python tools/scripts/manage_envs.py setup --component docs    # Setup specific component
python tools/scripts/manage_envs.py setup --all              # Setup all components
```

## Continuous Integration

The project uses **Docker-based CI/CD** with GitHub Actions:

- ✅ **Automated builds** on pull requests and releases
- ✅ **Quality checks** (linting, spell checking, prose quality)
- ✅ **Link validation** for internal and external links  
- ✅ **Accessibility testing** with axe-core
- ✅ **GitHub Pages deployment** for releases

### CI/CD Workflow

The GitHub Actions workflow (`.github/workflows/docs-ci.yml`) uses the same Docker container for consistency:

1. **Build Stage**: Creates the documentation container
2. **Quality Checks**: Runs all linting and validation tools
3. **Documentation Build**: Generates static site
4. **Link Testing**: Validates all internal and external links
5. **Deployment**: Publishes to GitHub Pages on releases

## VS Code Integration

The project includes comprehensive VS Code tasks in `.vscode/tasks.json`:

### Local UV Tasks
- **Setup tasks**: Environment initialization
- **Build tasks**: Documentation building with UV
- **Test tasks**: Running tests across components
- **Lint tasks**: Code quality checks with UV

### Docker Tasks
- **Docker: Build Documentation Container**: Build the Docker image
- **Docker: Serve Documentation**: Start containerized dev server
- **Docker: Build Documentation Site**: Build static docs in container
- **Docker: Quality Checks**: Run all quality tools in container

Access via `Ctrl+Shift+P` → "Tasks: Run Task"

## Benefits

### Docker Approach
- ✅ **Consistent environment** across all platforms
- ✅ **All tools pre-installed** (no dependency conflicts)
- ✅ **Isolated from host system** 
- ✅ **Easy CI/CD integration**
- ✅ **Reproducible builds**

### Local UV Approach  
- ✅ **Fast iteration** during development
- ✅ **Direct IDE integration** 
- ✅ **Component isolation** with local .venv directories
- ✅ **Modern tooling** with UV package management

## Privacy-First Documentation

The documentation is configured for privacy compliance:
- ❌ No cookies or tracking
- ❌ No external analytics
- ✅ Local development and static hosting ready
- ✅ GDPR compliant by design

## Troubleshooting

### Docker Issues
```bash
# Rebuild container if changes aren't reflected
./docker-docs.sh clean && ./docker-docs.sh build

# Check Docker status
docker --version
docker info

# View container logs
docker logs <container_id>

# Remove all containers and images (nuclear option)
docker system prune -a
```

### UV Issues
```bash
# Reset local environment
rm -rf .venv && uv sync

# Check UV status  
uv --version
python --version

# Clear UV cache
uv cache clean
```

### GitHub Actions Issues

If you see errors like "gzip: stdin: unexpected end of file" or "tar: Error is not recoverable":

1. **Check Workflow**: Ensure `.github/workflows/docs-ci.yml` uses Docker approach
2. **Vale Installation**: The error usually comes from Vale installation - we now use Docker instead
3. **Container Build**: Make sure the Docker container builds successfully locally first

```bash
# Test locally before pushing
cd docs
docker build -t van-cooldown-docs:test .
docker run --rm van-cooldown-docs:test uv run mkdocs --version
```

### Common Solutions

**Permission Denied (Docker)**:
```bash
# On Linux/macOS, ensure Docker daemon is running
sudo systemctl start docker

# On Windows, ensure Docker Desktop is running
```

**Port Already in Use**:
```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9  # Linux/macOS
netstat -ano | findstr :8000   # Windows
```

**Build Cache Issues**:
```bash
# Force rebuild without cache
docker build --no-cache -t van-cooldown-docs:latest .
```
