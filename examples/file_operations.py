#!/usr/bin/env python3
"""
File Operations Example
=======================

Demonstrates common file operations that can be automated with OpenClaw:
- Batch file processing
- Content searching and filtering
- File organization
- Report generation

Usage:
    python3 examples/file_operations.py
"""

import os
import re
from pathlib import Path
from datetime import datetime


def find_files_by_extension(directory, extension):
    """Find all files with a specific extension."""
    path = Path(directory)
    return list(path.rglob(f"*.{extension}"))


def search_in_files(files, pattern):
    """Search for a pattern in multiple files."""
    results = []
    regex = re.compile(pattern, re.IGNORECASE)
    
    for file_path in files:
        try:
            content = file_path.read_text()
            matches = regex.findall(content)
            if matches:
                results.append({
                    "file": str(file_path),
                    "matches": len(matches),
                    "preview": matches[:3]  # First 3 matches
                })
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return results


def organize_files_by_date(source_dir, dest_dir):
    """Organize files into subdirectories by modification date."""
    source = Path(source_dir)
    dest = Path(dest_dir)
    dest.mkdir(exist_ok=True)
    
    organized = []
    
    for file_path in source.glob("*"):
        if file_path.is_file():
            # Get modification time
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            year_month = mtime.strftime("%Y-%m")
            
            # Create destination directory
            target_dir = dest / year_month
            target_dir.mkdir(exist_ok=True)
            
            # Move file (for demo, we'll just record the action)
            organized.append({
                "file": file_path.name,
                "destination": str(target_dir)
            })
    
    return organized


def generate_file_report(directory):
    """Generate a report of all files in a directory."""
    path = Path(directory)
    
    report = {
        "directory": str(path),
        "timestamp": datetime.now().isoformat(),
        "files": [],
        "statistics": {
            "total_files": 0,
            "total_size": 0,
            "file_types": {}
        }
    }
    
    for file_path in path.rglob("*"):
        if file_path.is_file():
            stat = file_path.stat()
            ext = file_path.suffix or "no_extension"
            
            report["files"].append({
                "name": file_path.name,
                "size": stat.st_size,
                "extension": ext,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
            })
            
            report["statistics"]["total_files"] += 1
            report["statistics"]["total_size"] += stat.st_size
            report["statistics"]["file_types"][ext] = \
                report["statistics"]["file_types"].get(ext, 0) + 1
    
    return report


def main():
    """Demonstrate file operations."""
    print("🗂️  File Operations Example")
    print("=" * 60)
    
    # Example 1: Find Python files
    print("\n1. Finding Python files...")
    python_files = find_files_by_extension(".", "py")
    print(f"   Found {len(python_files)} Python files")
    for f in python_files[:5]:  # Show first 5
        print(f"   - {f}")
    
    # Example 2: Search for patterns
    print("\n2. Searching for 'OpenClaw' in Python files...")
    if python_files:
        results = search_in_files(python_files, r"OpenClaw")
        print(f"   Found in {len(results)} files")
        for r in results[:3]:
            print(f"   - {r['file']}: {r['matches']} matches")
    
    # Example 3: Generate report
    print("\n3. Generating file report...")
    report = generate_file_report(".")
    print(f"   Total files: {report['statistics']['total_files']}")
    print(f"   Total size: {report['statistics']['total_size']} bytes")
    print(f"   File types: {report['statistics']['file_types']}")
    
    print("\n✅ File operations demonstration complete!")


if __name__ == "__main__":
    main()
