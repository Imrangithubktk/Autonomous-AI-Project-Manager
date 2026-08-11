from datetime import date

from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.task import Task


class RecommendationEngine:

    def generate_recommendations(self, db: Session):

        recommendations = []

        # -----------------------------
        # Pending Tasks
        # -----------------------------
        pending_tasks = (
            db.query(Task)
            .filter(Task.status == "Pending")
            .count()
        )

        if pending_tasks > 5:
            recommendations.append({
                "priority": "High",
                "category": "Workload",
                "message": "There are many pending tasks. Consider assigning more developers."
            })

        # -----------------------------
        # High Priority Tasks
        # -----------------------------
        high_priority = (
            db.query(Task)
            .filter(
                Task.priority == "High",
                Task.status != "Completed"
            )
            .count()
        )

        if high_priority > 0:
            recommendations.append({
                "priority": "High",
                "category": "Task Management",
                "message": "Complete high-priority tasks as soon as possible."
            })

        # -----------------------------
        # Overdue Tasks
        # -----------------------------
        overdue = (
            db.query(Task)
            .filter(
                Task.due_date < date.today(),
                Task.status != "Completed"
            )
            .count()
        )

        if overdue > 0:
            recommendations.append({
                "priority": "Critical",
                "category": "Deadline",
                "message": "There are overdue tasks. Immediate attention is required."
            })

        # -----------------------------
        # Completed Projects
        # -----------------------------
        completed_projects = (
            db.query(Project)
            .filter(Project.status == "Completed")
            .count()
        )

        if completed_projects == 0:
            recommendations.append({
                "priority": "Medium",
                "category": "Project Progress",
                "message": "No completed projects yet. Focus on finishing ongoing work."
            })

        # -----------------------------
        # Everything Looks Good
        # -----------------------------
        if len(recommendations) == 0:
            recommendations.append({
                "priority": "Info",
                "category": "Project Health",
                "message": "Everything looks good. Keep monitoring project progress."
            })

        return recommendations
    def calculate_health_score(self, db: Session):
    
      score = 100

      pending_tasks = (
        db.query(Task)
        .filter(Task.status == "Pending")
        .count()
      )

      if pending_tasks > 5:
        score -= 20

      high_priority = (
        db.query(Task)
        .filter(
            Task.priority == "High",
            Task.status != "Completed"
        )
        .count()
      )

      if high_priority > 0:
        score -= 15

      overdue = (
        db.query(Task)
        .filter(
            Task.due_date < date.today(),
            Task.status != "Completed"
        )
        .count()
      )

      if overdue > 0:
        score -= 25

      completed_projects = (
        db.query(Project)
        .filter(Project.status == "Completed")
        .count()
      )

      if completed_projects == 0:
        score -= 10

      score = max(0, min(score, 100))

      if score >= 80:
        status = "Excellent"
      elif score >= 60:
        status = "Good"
      elif score >= 40:
        status = "Average"
      else:
        status = "Critical"

      return {
        "health_score": score,
        "status": status
      }

recommendation_engine = RecommendationEngine()