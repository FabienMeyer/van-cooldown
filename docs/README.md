# Van Cooldown Documentation - Docker Setup

## Quick Start

```bash
# Windows PowerShell
.\docker-docs.ps1 build    # Build container
.\docker-docs.ps1 serve    # Start dev server (localhost:8000)

# Linux/macOS
./docker-docs.sh build     # Build container  
./docker-docs.sh serve     # Start dev server (localhost:8000)
```

## Available Commands

| Command | Windows | Linux/macOS | Description |
|---------|---------|-------------|-------------|
| Build Container | `.\docker-docs.ps1 build` | `./docker-docs.sh build` | Build the documentation container |
| Development Server | `.\docker-docs.ps1 serve` | `./docker-docs.sh serve` | Start development server |
| Build Documentation | `.\docker-docs.ps1 docs` | `./docker-docs.sh docs` | Build static documentation |
| Quality Checks | `.\docker-docs.ps1 lint` | `./docker-docs.sh lint` | Run linting and quality checks |
| Link Checking | `.\docker-docs.ps1 linkcheck` | `./docker-docs.sh linkcheck` | Validate documentation links |
| Clean Up | `.\docker-docs.ps1 clean` | `./docker-docs.sh clean` | Remove containers and images |

## VS Code Integration

Use VS Code tasks for integrated development:

1. **Ctrl+Shift+P** → "Tasks: Run Task"
2. Choose from:
   - `Docker: Build Documentation Container`
   - `Docker: Serve Documentation` 
   - `Docker: Build Documentation Site`
   - `Docker: Quality Checks`

## Container Details

- **Base Image**: `python:3.13-alpine`
- **Tools Included**: 
  - MkDocs Material
  - PySpelling (spell checking)
  - Proselint (prose quality)
  - markdownlint-cli (Markdown linting)
  - axe-core (accessibility testing)
- **Security**: Non-root user, minimal attack surface
- **Size**: Optimized with Alpine Linux and layer caching

## Development Workflow

1. **Initial Setup**: `.\docker-docs.ps1 build` (one-time, ~3-4 minutes)
2. **Development**: `.\docker-docs.ps1 serve` (runs on localhost:8000)
3. **Quality Check**: `.\docker-docs.ps1 lint` (before committing)
4. **Build Release**: `.\docker-docs.ps1 docs` (creates `site/` directory)

## Troubleshooting

See the main [Setup Guide](setup-guide.md#troubleshooting) for detailed troubleshooting instructions.

## CI/CD

The same Docker container is used in GitHub Actions for consistent builds across environments.
