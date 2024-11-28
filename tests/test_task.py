import pytest
from task import Task


def test_task_creation():
    """Тест создания задачи с корректными данными."""
    task = Task(
        title="Написать тесты",
        description="Написать тесты для класса Task",
        category="Работа",
        due_date="2024-12-01",
        priority="Высокий"
    )
    assert task.title == "Написать тесты"
    assert task.description == "Написать тесты для класса Task"
    assert task.category == "Работа"
    assert task.due_date == "2024-12-01"
    assert task.priority == "Высокий"
    assert task.status == "Не выполнена"


def test_task_invalid_date():
    """Тест обработки некорректной даты."""
    with pytest.raises(ValueError, match="Неверный формат даты. Используйте формат ГГГГ-ММ-ДД."):
        Task(
            title="Некорректная дата",
            description="Тест с неправильной датой",
            category="Работа",
            due_date="01-12-2024",  
            priority="Средний"
        )


def test_task_mark_completed():
    """Тест изменения статуса задачи на выполненную."""
    task = Task(
        title="Закончить проект",
        description="Довести проект до конца",
        category="Личное",
        due_date="2024-11-30",
        priority="Средний"
    )
    task.mark_completed()
    assert task.status == "Выполнена"


def test_task_to_dict():
    """Тест сериализации задачи в словарь."""
    task = Task(
        title="Научиться pytest",
        description="Пройти курс по тестированию",
        category="Обучение",
        due_date="2024-12-15",
        priority="Высокий"
    )
    task.id = 1  
    expected_dict = {
        "id": 1,
        "title": "Научиться pytest",
        "description": "Пройти курс по тестированию",
        "category": "Обучение",
        "due_date": "2024-12-15",
        "priority": "Высокий",
        "status": "Не выполнена"
    }
    assert task.to_dict() == expected_dict


def test_task_from_dict():
    """Тест создания задачи из словаря."""
    task_data = {
        "id": 2,
        "title": "Прочитать книгу",
        "description": "Прочитать 'Чистый код'",
        "category": "Личное",
        "due_date": "2024-12-20",
        "priority": "Низкий",
        "status": "Не выполнена"
    }
    task = Task.from_dict(task_data)
    assert task.id == 2
    assert task.title == "Прочитать книгу"
    assert task.description == "Прочитать 'Чистый код'"
    assert task.category == "Личное"
    assert task.due_date == "2024-12-20"
    assert task.priority == "Низкий"
    assert task.status == "Не выполнена"
