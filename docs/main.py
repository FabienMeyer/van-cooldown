"""
Macros for MkDocs to provide git information
"""

import subprocess
from datetime import datetime

def define_env(env):
    """
    This is the hook for defining custom macros, variables and filters for mkdocs-macros
    """
    
    def get_git_info():
        """Get various git information"""
        try:
            # Get current commit hash
            commit_hash = subprocess.check_output(
                ['git', 'rev-parse', 'HEAD'], 
                cwd=env.project_dir,
                text=True
            ).strip()
            
            # Get short commit hash
            short_hash = subprocess.check_output(
                ['git', 'rev-parse', '--short', 'HEAD'], 
                cwd=env.project_dir,
                text=True
            ).strip()
            
            # Get commit date
            commit_date = subprocess.check_output(
                ['git', 'log', '-1', '--format=%ci'], 
                cwd=env.project_dir,
                text=True
            ).strip()
            
            # Get current branch
            branch = subprocess.check_output(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'], 
                cwd=env.project_dir,
                text=True
            ).strip()
            
            # Get tag (if exists)
            try:
                tag = subprocess.check_output(
                    ['git', 'describe', '--tags', '--exact-match'], 
                    cwd=env.project_dir,
                    text=True,
                    stderr=subprocess.DEVNULL
                ).strip()
            except subprocess.CalledProcessError:
                tag = None
            
            # Get total commits count
            commit_count = subprocess.check_output(
                ['git', 'rev-list', '--count', 'HEAD'], 
                cwd=env.project_dir,
                text=True
            ).strip()
            
            return {
                'hash': commit_hash,
                'short_hash': short_hash,
                'date': commit_date,
                'branch': branch,
                'tag': tag,
                'commit_count': commit_count
            }
        except subprocess.CalledProcessError:
            return {
                'hash': 'unknown',
                'short_hash': 'unknown',
                'date': 'unknown',
                'branch': 'unknown',
                'tag': None,
                'commit_count': 'unknown'
            }
    
    # Make git info available as variables
    git_info = get_git_info()
    env.variables['git_commit_hash'] = git_info['hash']
    env.variables['git_short_hash'] = git_info['short_hash']
    env.variables['git_commit_date'] = git_info['date']
    env.variables['git_branch'] = git_info['branch']
    env.variables['git_tag'] = git_info['tag']
    env.variables['git_commit_count'] = git_info['commit_count']
    env.variables['build_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    # Make git_info function available in templates
    env.macro(get_git_info, 'git_info')
