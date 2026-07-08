from datetime import date, timedelta
from typing import Optional

from src.task_manager.models import Task, TaskStatus


class TaskManager:
    def __init__(self):
        self._tasks: list[Task] = []

    def add_task(
        self,
        title: str,
        description: str = None,
        due_date: Optional[date] = None,
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
    ) -> Task:
        task = Task(
            title=title,
            description=description,
            due_date=due_date,
            category=category,
            subcategory=subcategory,
        )
        self._tasks.append(task)
        return task

    def get_tasks(
        self,
        status: TaskStatus = None,
        overdue_only: bool = False,
        upcoming_within_days: Optional[int] = None,
        year: Optional[int] = None,
        month: Optional[int] = None,
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
    ) -> list[Task]:
        tasks = self._tasks

        if status is not None:
            tasks = [t for t in tasks if t.status == status]

        if overdue_only:
            tasks = [t for t in tasks if t.is_overdue]

        if upcoming_within_days is not None:
            tasks = [
                t
                for t in tasks
                if t.due_date is not None
                and t.status == TaskStatus.PENDING
                and t.due_date >= date.today()
                and t.due_date <= date.today() + timedelta(days=upcoming_within_days)
            ]

        if year is not None:
            tasks = [t for t in tasks if t.created_at.year == year]

        if month is not None:
            if not 1 <= month <= 12:
                raise ValueError("El mes debe estar entre 1 y 12.")
            tasks = [t for t in tasks if t.created_at.month == month]

        if category is not None:
            if not category.strip():
                raise ValueError("La categoría no puede estar vacía.")
            tasks = [t for t in tasks if t.category == category]

        if subcategory is not None:
            if not subcategory.strip():
                raise ValueError("La subcategoría no puede estar vacía.")
            tasks = [t for t in tasks if t.subcategory == subcategory]

        return tasks

    def complete_task(self, title: str) -> None:
        for task in self._tasks:
            if task.title == title:
                task.complete()
                return
        raise ValueError(f"No se encontró la tarea con título: {title}")
