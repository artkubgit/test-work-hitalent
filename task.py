from typing import Optional
from datetime import datetime

class Task:
    def __init__(self, title: str, description: str, category: str, due_date: str, priority: str):
        self.id = None  # Уникальный идентификатор (назначается при добавлении в TaskManager)
        self.title = title
        self.description = description
        self.category = category
        self.due_date = self._validate_date(due_date)
        self.priority = priority
        self.status = "Не выполнена"  # Статус по умолчанию
    
    def _validate_date(self, date_str: str) -> str:
        """Проверка формата даты"""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте формат ГГГГ-ММ-ДД.")
    
    def mark_completed(self):
        """Отметить задачу как выполненную"""
        self.status = "Выполнена"
    
    def to_dict(self) -> dict:
        """Сериализация задачи в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        """Десериализация задачи из словаря"""
        task = Task(
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"]
        )
        task.id = data["id"]
        task.status = data["status"]
        return task
