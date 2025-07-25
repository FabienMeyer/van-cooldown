# Version Information

This page provides detailed information about the current version and build of this documentation.

## Git Information

| Property | Value |
|----------|-------|
| **Commit Hash** | `{{ git_commit_hash }}` |
| **Short Hash** | `{{ git_short_hash }}` |
| **Branch** | `{{ git_branch }}` |
| **Last Commit Date** | {{ git_commit_date }} |
| **Total Commits** | {{ git_commit_count }} |
{% if git_tag %}| **Tag** | `{{ git_tag }}` |{% endif %}
| **Documentation Built** | {{ build_date }} |

## Repository Information

- **Repository**: [{{ config.repo_name }}]({{ config.repo_url }})
- **Documentation Source**: [docs/src/]({{ config.repo_url }}/tree/{{ git_branch }}/docs/src)
- **Issue Tracker**: [GitHub Issues]({{ config.repo_url }}/issues)

## Quick Links

- [Latest Commit]({{ config.repo_url }}/commit/{{ git_commit_hash }})
- [Branch History]({{ config.repo_url }}/commits/{{ git_branch }})
- [Release Tags]({{ config.repo_url }}/tags)

---

!!! info "Auto-generated Information"
    This information is automatically generated during the documentation build process using git metadata.
