# 📋 Version Information

This page provides detailed information about the current version and build of this documentation.

## 🔍 Git Information

<div class="version-info-table">

| Property | Value |
|----------|-------|
| **📝 Commit Hash** | <code class="commit-hash">{{ git_commit_hash }}</code> |
| **🔗 Short Hash** | <code class="commit-hash">{{ git_short_hash }}</code> |
| **🌿 Branch** | <span class="git-branch">{{ git_branch }}</span> |
| **📅 Last Commit Date** | {{ git_commit_date }} |
| **📊 Total Commits** | {{ git_commit_count }} |
{% if git_tag %}| **🏷️ Tag** | <span class="git-tag">{{ git_tag }}</span> |{% endif %}
| **🔨 Documentation Built** | {{ build_date }} |

</div>

## 📦 Repository Information

- **📁 Repository**: [{{ config.repo_name }}]({{ config.repo_url }})
- **📚 Documentation Source**: [docs/src/]({{ config.repo_url }}/tree/{{ git_branch }}/docs/src)
- **🐛 Issue Tracker**: [GitHub Issues]({{ config.repo_url }}/issues)
- **📋 Project Board**: [GitHub Projects]({{ config.repo_url }}/projects)

## 🔗 Quick Links

- [📄 Latest Commit]({{ config.repo_url }}/commit/{{ git_commit_hash }})
- [📈 Branch History]({{ config.repo_url }}/commits/{{ git_branch }})
- [🏷️ Release Tags]({{ config.repo_url }}/tags)
- [🔄 Pull Requests]({{ config.repo_url }}/pulls)
- [📊 Insights]({{ config.repo_url }}/pulse)

## 🛠️ Build Environment

The documentation is built using:

- **MkDocs Material**: {{ config.theme.name }}
- **Python**: {{ macros_info.version }}
- **Git Branch**: {{ git_branch }}
- **Build Date**: {{ build_date }}

---

!!! info "🤖 Auto-generated Information"
    This information is automatically generated during the documentation build process using git metadata and MkDocs macros. The data is refreshed every time the documentation is built.
