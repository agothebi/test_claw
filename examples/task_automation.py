#!/usr/bin/env python3
"""
Task Automation Example
=======================

Demonstrates common automation tasks using OpenClaw patterns:
- Data collection and processing
- Report generation
- Scheduled tasks simulation
- Notification workflows

Usage:
    python3 examples/task_automation.py
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path


class TaskAutomation:
    """Simulates common automation tasks."""
    
    def __init__(self):
        self.output_dir = Path("automation_output")
        self.output_dir.mkdir(exist_ok=True)
    
    def task_daily_report(self):
        """Simulate generating a daily summary report."""
        print("\n📊 Task: Daily Report Generation")
        
        # Simulate collecting data
        data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "metrics": {
                "files_processed": 127,
                "tasks_completed": 15,
                "errors_encountered": 2,
                "uptime_hours": 23.5
            },
            "highlights": [
                "All scheduled backups completed successfully",
                "System performance within normal parameters",
                "2 minor errors resolved automatically"
            ]
        }
        
        # Generate report
        report_file = self.output_dir / f"daily_report_{data['date']}.json"
        report_file.write_text(json.dumps(data, indent=2))
        
        print(f"   ✓ Generated report: {report_file}")
        print(f"   ✓ Tasks completed: {data['metrics']['tasks_completed']}")
        
        return data
    
    def task_file_cleanup(self):
        """Simulate cleaning up old temporary files."""
        print("\n🧹 Task: File Cleanup")
        
        # Simulate finding old files
        cutoff_date = datetime.now() - timedelta(days=30)
        
        cleanup_log = {
            "timestamp": datetime.now().isoformat(),
            "cutoff_date": cutoff_date.isoformat(),
            "files_removed": [
                "temp_20260214.log",
                "cache_old.dat",
                "backup_20260201.tmp"
            ],
            "space_freed_mb": 245
        }
        
        log_file = self.output_dir / "cleanup_log.json"
        log_file.write_text(json.dumps(cleanup_log, indent=2))
        
        print(f"   ✓ Cleaned up {len(cleanup_log['files_removed'])} files")
        print(f"   ✓ Freed {cleanup_log['space_freed_mb']} MB")
        
        return cleanup_log
    
    def task_backup_verification(self):
        """Simulate verifying backup integrity."""
        print("\n💾 Task: Backup Verification")
        
        # Simulate checking backups
        backups = [
            {"name": "database_backup.sql", "status": "verified", "size_mb": 1024},
            {"name": "files_backup.tar.gz", "status": "verified", "size_mb": 2048},
            {"name": "config_backup.zip", "status": "verified", "size_mb": 5}
        ]
        
        verification = {
            "timestamp": datetime.now().isoformat(),
            "total_backups": len(backups),
            "verified": sum(1 for b in backups if b["status"] == "verified"),
            "total_size_mb": sum(b["size_mb"] for b in backups),
            "details": backups
        }
        
        verify_file = self.output_dir / "backup_verification.json"
        verify_file.write_text(json.dumps(verification, indent=2))
        
        print(f"   ✓ Verified {verification['verified']}/{verification['total_backups']} backups")
        print(f"   ✓ Total size: {verification['total_size_mb']} MB")
        
        return verification
    
    def task_system_health_check(self):
        """Simulate a system health check."""
        print("\n🏥 Task: System Health Check")
        
        # Simulate checking various system components
        health_status = {
            "timestamp": datetime.now().isoformat(),
            "components": {
                "disk_usage": {"status": "healthy", "usage_percent": 65},
                "memory": {"status": "healthy", "usage_percent": 72},
                "cpu": {"status": "healthy", "load_avg": 1.5},
                "network": {"status": "healthy", "latency_ms": 15}
            },
            "alerts": [],
            "overall_status": "healthy"
        }
        
        health_file = self.output_dir / "health_check.json"
        health_file.write_text(json.dumps(health_status, indent=2))
        
        print(f"   ✓ System status: {health_status['overall_status'].upper()}")
        print(f"   ✓ All components operational")
        
        return health_status
    
    def task_notification_workflow(self):
        """Simulate a notification workflow."""
        print("\n📬 Task: Notification Workflow")
        
        # Simulate checking conditions and generating notifications
        notifications = []
        
        # Check various conditions
        conditions = [
            {"check": "Backup completion", "notify": True, "priority": "low"},
            {"check": "High disk usage", "notify": False, "priority": "medium"},
            {"check": "Security updates", "notify": True, "priority": "high"}
        ]
        
        for cond in conditions:
            if cond["notify"]:
                notifications.append({
                    "message": f"{cond['check']} requires attention",
                    "priority": cond["priority"],
                    "timestamp": datetime.now().isoformat()
                })
        
        notify_file = self.output_dir / "notifications.json"
        notify_file.write_text(json.dumps(notifications, indent=2))
        
        print(f"   ✓ Generated {len(notifications)} notifications")
        for notif in notifications:
            print(f"   - [{notif['priority'].upper()}] {notif['message']}")
        
        return notifications
    
    def run_all_tasks(self):
        """Execute all automation tasks."""
        print("🤖 Task Automation Suite")
        print("=" * 60)
        
        tasks = [
            self.task_daily_report,
            self.task_file_cleanup,
            self.task_backup_verification,
            self.task_system_health_check,
            self.task_notification_workflow
        ]
        
        results = {}
        
        for task in tasks:
            try:
                result = task()
                results[task.__name__] = "success"
                time.sleep(0.5)  # Simulate processing time
            except Exception as e:
                print(f"   ❌ Task failed: {e}")
                results[task.__name__] = f"failed: {e}"
        
        # Summary
        print("\n" + "=" * 60)
        print("✅ Automation Suite Complete")
        print(f"   Output directory: {self.output_dir}")
        print(f"   Tasks executed: {len(results)}")
        print(f"   Success rate: {sum(1 for r in results.values() if r == 'success')}/{len(results)}")


def main():
    """Run the task automation demonstration."""
    automation = TaskAutomation()
    automation.run_all_tasks()


if __name__ == "__main__":
    main()
