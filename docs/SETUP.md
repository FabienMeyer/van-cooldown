# Documentation Environment Setup Guide

This guide helps you set up the virtual environment for the Van Cooldown documentation.

## ✅ **Your Current Status**

✅ **Virtual Environment**: Created successfully  
✅ **Dependencies**: All MkDocs packages installed  
✅ **Tools**: PySpelling, Proselint, Linkchecker ready  

## 🚀 **Quick Commands**

### Check Environment Status
```bash
cd c:\Users\fabie\Documents\projets\van-cooldown
python tools\scripts\manage_envs.py status
```

### Build Documentation
```bash
cd docs
uv run mkdocs build
```

### Serve Documentation Locally
```bash
cd docs
uv run mkdocs serve
```

### Run Quality Checks
```bash
# Spell checking
cd docs
uv run pyspelling

# Prose linting
cd docs  
uv run proselint src/

# Link checking (after serving docs)
cd docs
uv run linkchecker http://localhost:8000
```

## 📦 **Installed Packages**

Your documentation environment includes:

### 📚 **Core Documentation**
- **mkdocs** (1.6.1) - Static site generator
- **mkdocs-material** (9.6.15) - Material theme

### 🔌 **Plugins**
- **mkdocs-mermaid2-plugin** - Diagram support
- **mkdocs-git-revision-date-localized-plugin** - Git dates
- **mkdocs-minify-plugin** - HTML/CSS/JS minification
- **mkdocs-macros-plugin** - Macros and variables
- **mkdocs-awesome-pages-plugin** - Page organization
- **mkdocs-redirects** - URL redirects
- **mkdocstrings** - API documentation from docstrings

### 🔍 **Quality Tools**
- **pyspelling** - Spell checking with Aspell
- **proselint** - Prose linting
- **linkchecker** - Link validation

## 🎯 **VS Code Integration**

Your VS Code tasks are now configured:

- **Ctrl+Shift+P** → "Tasks: Run Task" → Choose from:
  - `Setup: Documentation Environment`
  - `Docs: Build Documentation`
  - `Docs: Serve Documentation`
  - `Docs: Spell Check`
  - `Environment: Show Status`

## 🔧 **Virtual Environment Details**

- **Location**: `C:\Users\fabie\Documents\projets\van-cooldown\.venv`
- **Python Version**: 3.13.3
- **Package Manager**: UV (fast, modern replacement for pip/poetry)
- **Total Packages**: 67 packages installed

## 🎉 **What You Can Do Now**

1. **Start the documentation server**:
   ```bash
   cd docs
   uv run mkdocs serve
   ```
   Then open http://localhost:8000

2. **Edit documentation** in `docs/src/` 

3. **Add new pages** by updating `docs/mkdocs.yml`

4. **Run quality checks** before committing

## 🆘 **Troubleshooting**

### If something doesn't work:

1. **Re-sync environment**:
   ```bash
   cd docs
   uv sync
   ```

2. **Check UV is working**:
   ```bash
   uv --version
   ```

3. **Verify Python environment**:
   ```bash
   cd docs
   uv run python --version
   ```

### Need to reinstall everything?
```bash
# Delete the virtual environment
rmdir /s C:\Users\fabie\Documents\projets\van-cooldown\.venv

# Recreate it
cd docs
uv sync
```

## 📞 **Getting Help**

- **UV Documentation**: https://docs.astral.sh/uv/
- **MkDocs Documentation**: https://www.mkdocs.org/
- **Material Theme**: https://squidfunk.github.io/mkdocs-material/

Your documentation environment is ready to use! 🎉
