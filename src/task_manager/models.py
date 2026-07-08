from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Optional


class TaskStatus(Enum):
    PENDING = "Pendiente"
    COMPLETED = "Completada"


@dataclass
class Task:
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    due_date: Optional[date] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("El título de la tarea no puede estar vacío.")

        if len(self.title.strip()) > 50:
            raise ValueError("El título de la tarea no puede superar los 50 caracteres.")

        if self.due_date is not None and not isinstance(self.due_date, date):
            raise ValueError("La fecha de vencimiento debe ser una fecha válida.")

        if self.due_date is not None and self.due_date < date(1950, 1, 1):
            raise ValueError("La fecha de vencimiento no puede ser anterior a 1950-01-01.")

        if self.category is not None and not self.category.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if self.subcategory is not None and not self.subcategory.strip():
            raise ValueError("La subcategoría no puede estar vacía.")

    @property
    def is_overdue(self) -> bool:
        return (
            self.status == TaskStatus.PENDING
            and self.due_date is not None
            and self.due_date < date.today()
        )

    def complete(self):
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()
