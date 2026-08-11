from datetime import date, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.task import Task


class AnalyticsService:
    def project_status_summary(self, db: Session):
    
        result = (
            db.query(
                Project.status,
                func.count(Project.id)
            )
            .group_by(Project.status)
            .all()
        )

        return {
            status: count
            for status, count in result
        }
    def task_status_summary(self, db: Session):
    
        result = (
            db.query(
                Task.status,
                func.count(Task.id)
            )
            .group_by(Task.status)
            .all()
        )

        return {
            status: count
            for status, count in result
        }
    def task_priority_summary(self, db: Session):
    
        result = (
            db.query(
                Task.priority,
                func.count(Task.id)
            )
            .group_by(Task.priority)
            .all()
        )

        return {
            priority: count
            for priority, count in result
        }
    def upcoming_deadlines(self, db: Session):
        
      today = date.today()
      next_week = today + timedelta(days=7)

      tasks = (
        db.query(Task)
        .filter(
            Task.due_date >= today,
            Task.due_date <= next_week
        )
        .order_by(Task.due_date)
        .all()
      )

      return [
        {
            "task_id": task.id,
            "task_name": task.task_name,
            "due_date": task.due_date,
            "priority": task.priority,
            "status": task.status
        }
        for task in tasks
      ]
    def overdue_tasks(self, db: Session):
    
      today = date.today()

      tasks = (
        db.query(Task)
        .filter(
            Task.due_date < today,
            Task.status != "Completed"
        )
        .order_by(Task.due_date)
        .all()
      )

      return [
        {
            "task_id": task.id,
            "task_name": task.task_name,
            "due_date": task.due_date,
            "priority": task.priority,
            "status": task.status
        }
        for task in tasks
      ]
    def dashboard_summary(self, db: Session):
    
      total_projects = db.query(Project).count()

      active_projects = (
        db.query(Project)
        .filter(Project.status == "Active")
        .count()
      )

      completed_projects = (
        db.query(Project)
        .filter(Project.status == "Completed")
        .count()
      )

      total_tasks = db.query(Task).count()

      pending_tasks = (
        db.query(Task)
        .filter(Task.status == "Pending")
        .count()
      )

      completed_tasks = (
        db.query(Task)
        .filter(Task.status == "Completed")
        .count()
      )

      high_priority_tasks = (
        db.query(Task)
        .filter(Task.priority == "High")
        .count()
      )

      overdue_tasks = (
        db.query(Task)
        .filter(
            Task.due_date < date.today(),
            Task.status != "Completed"
        )
        .count()
      )

      return {
        "total_projects": total_projects,
        "active_projects": active_projects,
        "completed_projects": completed_projects,
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
        "high_priority_tasks": high_priority_tasks,
        "overdue_tasks": overdue_tasks
      }
analytics_service = AnalyticsService()
