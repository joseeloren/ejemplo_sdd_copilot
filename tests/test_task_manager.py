from datetime import date, timedelta, datetime

import pytest
from src.task_manager.main import TaskManager
from src.task_manager.models import TaskStatus


def test_add_task():
    manager = TaskManager()
    task = manager.add_task(title="Comprar leche", description="Ir al supermercado")

    assert task.title == "Comprar leche"
    assert task.description == "Ir al supermercado"
    assert task.status == TaskStatus.PENDING


def test_add_task_empty_title():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task(title="   ")


def test_add_task_title_too_long():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task(title="x" * 51)


def test_add_task_with_due_date():
    manager = TaskManager()
    due_date = date(2026, 7, 15)

    task = manager.add_task(title="Pagar factura", due_date=due_date)

    assert task.due_date == due_date


def test_add_task_invalid_due_date():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task(title="Pagar factura", due_date="fecha inválida")


def test_pending_task_with_past_due_date_is_overdue():
    manager = TaskManager()
    due_date = date.today() - timedelta(days=1)

    task = manager.add_task(title="Enviar reporte", due_date=due_date)

    assert task.is_overdue is True


def test_get_tasks_can_filter_overdue_tasks():
    manager = TaskManager()
    manager.add_task(title="Tarea vencida", due_date=date.today() - timedelta(days=1))
    manager.add_task(title="Tarea futura", due_date=date.today() + timedelta(days=1))
    manager.add_task(title="Tarea sin fecha")

    overdue_tasks = manager.get_tasks(overdue_only=True)

    assert [task.title for task in overdue_tasks] == ["Tarea vencida"]


def test_get_tasks_can_filter_upcoming_tasks():
    manager = TaskManager()
    manager.add_task(title="Tarea urgente", due_date=date.today() + timedelta(days=2))
    manager.add_task(title="Tarea lejana", due_date=date.today() + timedelta(days=10))
    manager.add_task(title="Tarea sin fecha")

    upcoming_tasks = manager.get_tasks(upcoming_within_days=3)

    assert [task.title for task in upcoming_tasks] == ["Tarea urgente"]


def test_complete_task():
    manager = TaskManager()
    manager.add_task(title="Comprar leche")
    manager.complete_task("Comprar leche")

    tasks = manager.get_tasks()
    assert tasks[0].status == TaskStatus.COMPLETED


def test_complete_task_not_found():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.complete_task("Tarea Inexistente")


def test_get_tasks_filter_by_year():
    manager = TaskManager()
    # Mockear o crear tareas en diferentes años
    task1 = manager.add_task(title="Tarea 2024")
    task1.created_at = datetime(2024, 1, 1)
    
    task2 = manager.add_task(title="Tarea 2026")
    task2.created_at = datetime(2026, 5, 1)
    
    task3 = manager.add_task(title="Otra Tarea 2026")
    task3.created_at = datetime(2026, 8, 1)

    tasks_2026 = manager.get_tasks(year=2026)
    assert len(tasks_2026) == 2
    assert "Tarea 2026" in [t.title for t in tasks_2026]

def test_get_tasks_filter_by_year_empty():
    manager = TaskManager()
    manager.add_task(title="Tarea 2026")
    
    tasks_2024 = manager.get_tasks(year=2024)
    assert len(tasks_2024) == 0


def test_get_tasks_filter_by_month():
    manager = TaskManager()

    task1 = manager.add_task(title="Tarea enero")
    task1.created_at = datetime(2024, 1, 5)

    task2 = manager.add_task(title="Tarea febrero")
    task2.created_at = datetime(2025, 2, 10)

    task3 = manager.add_task(title="Tarea febrero otra")
    task3.created_at = datetime(2026, 2, 15)

    tasks_february = manager.get_tasks(month=2)

    assert [task.title for task in tasks_february] == ["Tarea febrero", "Tarea febrero otra"]


def test_get_tasks_filter_by_month_invalid():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.get_tasks(month=13)


def test_get_tasks_filter_by_month_and_year():
    manager = TaskManager()

    task1 = manager.add_task(title="Tarea enero 2024")
    task1.created_at = datetime(2024, 1, 5)

    task2 = manager.add_task(title="Tarea febrero 2024")
    task2.created_at = datetime(2024, 2, 10)

    task3 = manager.add_task(title="Tarea febrero 2025")
    task3.created_at = datetime(2025, 2, 15)

    tasks = manager.get_tasks(year=2024, month=2)

    assert [task.title for task in tasks] == ["Tarea febrero 2024"]


def test_add_task_due_date_before_1950_is_invalid():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task(title="Tarea antigua", due_date=date(1949, 12, 31))


def test_add_task_with_category():
    manager = TaskManager()

    task = manager.add_task(title="Comprar pan", category="Compras")

    assert task.category == "Compras"


def test_add_task_invalid_category():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task(title="Comprar pan", category="   ")


def test_get_tasks_filter_by_category():
    manager = TaskManager()
    manager.add_task(title="Tarea hogar", category="Hogar")
    manager.add_task(title="Tarea trabajo", category="Trabajo")

    tasks = manager.get_tasks(category="Hogar")

    assert [task.title for task in tasks] == ["Tarea hogar"]


def test_add_task_with_subcategory():
    manager = TaskManager()

    task = manager.add_task(title="Comprar comida", category="Compras", subcategory="Supermercado")

    assert task.category == "Compras"
    assert task.subcategory == "Supermercado"


def test_add_task_invalid_subcategory():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task(title="Comprar comida", category="Compras", subcategory="   ")


def test_get_tasks_filter_by_subcategory():
    manager = TaskManager()
    manager.add_task(title="Tarea hogar", category="Hogar", subcategory="Limpieza")
    manager.add_task(title="Tarea trabajo", category="Trabajo", subcategory="Limpieza")
    manager.add_task(title="Tarea otra", category="Hogar", subcategory="Cocina")

    tasks = manager.get_tasks(subcategory="Limpieza")

    assert [task.title for task in tasks] == ["Tarea hogar", "Tarea trabajo"]
