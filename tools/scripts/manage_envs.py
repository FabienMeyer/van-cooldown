#!/usr/bin/env python3
"""
Cross-platform Multi-environment management script for Van Cooldown monorepo
"""

import subprocess
import sys
import os
from pathlib import Path
import argparse

def run_command(cmd, cwd=None):
    """Run a command and return the result"""
    print(f"➜ {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    return result.returncode == 0

def setup_environment(component):
    """Setup UV environment for a specific component"""
    component_path = Path(component)
    
    if not component_path.exists():
        print(f"❌ Component path {component} does not exist")
        return False
    
    print(f"🔧 Setting up environment for {component}...")
    
    if run_command("uv sync", cwd=component_path):
        print(f"✅ Environment setup complete for {component}")
        return True
    else:
        print(f"❌ Failed to setup environment for {component}")
        return False

def show_status():
    """Show status of all environments"""
    components = ["docs", "software/backend"]
    
    print("Environment Status:")
    print("=" * 60)
    
    for component in components:
        component_path = Path(component)
        
        if not component_path.exists():
            status = "❌ Missing"
        else:
            # Check for local .venv folder
            local_venv = component_path / ".venv"
            if local_venv.exists():
                # Check if we can run python in the environment
                result = subprocess.run(
                    "uv run python --version", 
                    shell=True, 
                    cwd=component_path, 
                    capture_output=True, 
                    text=True
                )
                
                if result.returncode == 0:
                    python_version = result.stdout.strip()
                    status = f"✅ Active (Local .venv, {python_version})"
                else:
                    status = "⚠ Local .venv exists but not working"
            else:
                status = "❌ No local .venv found"
        
        print(f"{component:20} {status}")

def main():
    parser = argparse.ArgumentParser(description="Multi-environment manager for Van Cooldown")
    parser.add_argument("action", choices=["setup", "status"], help="Action to perform")
    parser.add_argument("--component", choices=["docs", "backend", "all"], default="all", help="Component to work on")
    
    args = parser.parse_args()
    
    if args.action == "status":
        show_status()
        return
    
    # Map component names
    component_map = {
        "docs": ["docs"],
        "backend": ["software/backend"],
        "all": ["docs", "software/backend"]
    }
    
    components = component_map[args.component]
    
    for component in components:
        if args.action == "setup":
            setup_environment(component)

if __name__ == "__main__":
    main()
