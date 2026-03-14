#!/usr/bin/env python3
"""
OpenClaw Demonstration Script
==============================

This script demonstrates core OpenClaw capabilities through practical examples.
It showcases file operations, command execution, and automation patterns.

Requirements:
    - Python 3.8+
    - OpenClaw installed and running (npm install -g openclaw)

Usage:
    python3 openclaw_demo.py
"""

import os
import json
import datetime
from pathlib import Path


class OpenClawDemo:
    """Demonstrates OpenClaw capabilities through practical examples."""
    
    def __init__(self, workspace_path="."):
        self.workspace = Path(workspace_path)
        self.demo_dir = self.workspace / "openclaw_demo_output"
        self.demo_dir.mkdir(exist_ok=True)
        
    def demo_file_operations(self):
        """Demonstrate file creation, reading, and manipulation."""
        print("\n" + "="*60)
        print("DEMO 1: File Operations")
        print("="*60)
        
        # Create sample files
        sample_file = self.demo_dir / "sample.txt"
        sample_file.write_text("OpenClaw makes automation easy!\n")
        print(f"✓ Created: {sample_file}")
        
        # Create JSON data
        data = {
            "agent": "OpenClaw",
            "capabilities": ["file_ops", "commands", "web_search", "memory"],
            "timestamp": datetime.datetime.now().isoformat()
        }
        json_file = self.demo_dir / "data.json"
        json_file.write_text(json.dumps(data, indent=2))
        print(f"✓ Created: {json_file}")
        
        # Read and display
        content = sample_file.read_text()
        print(f"✓ Read sample.txt: {content.strip()}")
        
        return True
    
    def demo_directory_organization(self):
        """Demonstrate directory creation and file organization."""
        print("\n" + "="*60)
        print("DEMO 2: Directory Organization")
        print("="*60)
        
        # Create organized structure
        categories = ["documents", "code", "data", "logs"]
        for category in categories:
            cat_dir = self.demo_dir / category
            cat_dir.mkdir(exist_ok=True)
            
            # Create sample file in each category
            sample = cat_dir / f"{category}_sample.txt"
            sample.write_text(f"Sample file in {category} category")
            print(f"✓ Created: {cat_dir}/")
        
        return True
    
    def demo_data_processing(self):
        """Demonstrate data processing and transformation."""
        print("\n" + "="*60)
        print("DEMO 3: Data Processing")
        print("="*60)
        
        # Create sample log data
        log_entries = [
            {"level": "INFO", "message": "Application started", "timestamp": "2026-03-14T08:00:00"},
            {"level": "ERROR", "message": "Connection failed", "timestamp": "2026-03-14T08:15:00"},
            {"level": "INFO", "message": "Retrying connection", "timestamp": "2026-03-14T08:15:30"},
            {"level": "ERROR", "message": "Timeout occurred", "timestamp": "2026-03-14T08:16:00"},
            {"level": "INFO", "message": "Connection established", "timestamp": "2026-03-14T08:17:00"},
        ]
        
        # Write logs
        logs_dir = self.demo_dir / "logs"
        logs_dir.mkdir(exist_ok=True)
        log_file = logs_dir / "app.log"
        
        with log_file.open("w") as f:
            for entry in log_entries:
                f.write(f"[{entry['timestamp']}] {entry['level']}: {entry['message']}\n")
        
        print(f"✓ Created log file: {log_file}")
        
        # Process: Extract errors
        errors = [e for e in log_entries if e["level"] == "ERROR"]
        error_report = logs_dir / "error_report.txt"
        
        with error_report.open("w") as f:
            f.write("ERROR REPORT\n")
            f.write("=" * 40 + "\n\n")
            for error in errors:
                f.write(f"Time: {error['timestamp']}\n")
                f.write(f"Message: {error['message']}\n\n")
        
        print(f"✓ Created error report: {error_report}")
        print(f"  Found {len(errors)} errors")
        
        return True
    
    def demo_automation_task(self):
        """Demonstrate a complete automation workflow."""
        print("\n" + "="*60)
        print("DEMO 4: Automation Workflow")
        print("="*60)
        
        # Simulate a multi-step automation task
        tasks = [
            "Initialize workspace",
            "Gather data from sources",
            "Process and transform data",
            "Generate reports",
            "Archive results"
        ]
        
        status_file = self.demo_dir / "automation_status.txt"
        
        with status_file.open("w") as f:
            f.write("AUTOMATION TASK LOG\n")
            f.write("=" * 40 + "\n\n")
            
            for i, task in enumerate(tasks, 1):
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                status = f"[{timestamp}] Step {i}/{len(tasks)}: {task} ✓\n"
                f.write(status)
                print(f"  {status.strip()}")
        
        print(f"\n✓ Automation complete! Log: {status_file}")
        
        return True
    
    def demo_summary(self):
        """Generate a summary of all demonstrations."""
        print("\n" + "="*60)
        print("DEMO SUMMARY")
        print("="*60)
        
        # Count created files
        file_count = len(list(self.demo_dir.rglob("*")))
        dir_count = len([d for d in self.demo_dir.rglob("*") if d.is_dir()])
        
        summary = {
            "workspace": str(self.demo_dir),
            "files_created": file_count,
            "directories_created": dir_count,
            "demos_completed": 4,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        summary_file = self.demo_dir / "demo_summary.json"
        summary_file.write_text(json.dumps(summary, indent=2))
        
        print(f"\nWorkspace: {self.demo_dir}")
        print(f"Files created: {file_count}")
        print(f"Directories: {dir_count}")
        print(f"Summary saved: {summary_file}")
        
        return True
    
    def run_all_demos(self):
        """Run all demonstration examples."""
        print("\n🦞 OpenClaw Demonstration Suite")
        print("Showcasing AI-powered automation capabilities\n")
        
        demos = [
            self.demo_file_operations,
            self.demo_directory_organization,
            self.demo_data_processing,
            self.demo_automation_task,
        ]
        
        for demo in demos:
            try:
                demo()
            except Exception as e:
                print(f"❌ Demo failed: {e}")
                return False
        
        self.demo_summary()
        
        print("\n" + "="*60)
        print("✨ All demonstrations completed successfully!")
        print("="*60)
        print(f"\nOutput directory: {self.demo_dir}")
        print("Explore the created files to see OpenClaw's capabilities.\n")
        
        return True


def main():
    """Main entry point for the demonstration."""
    demo = OpenClawDemo()
    
    try:
        success = demo.run_all_demos()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
        exit(1)
    except Exception as e:
        print(f"\n❌ Error running demo: {e}")
        exit(1)


if __name__ == "__main__":
    main()
