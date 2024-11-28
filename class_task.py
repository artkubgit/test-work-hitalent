import json
from typing import List, Optional
from task import Task

class TaskManager:
    def __init__(self, data_file: str = "data.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self._load_tasks()

    def _load_tasks(self):
        """Загрузка задач из файла"""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def _save_tasks(self):
        """Сохранение задач в файл"""
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

    def add_task(self, task: Task):
        """Добавление новой задачи"""
        task.id = len(self.tasks) + 1
        self.tasks.append(task)
        self._save_tasks()

    def delete_task(self, task_id: int):
        """Удаление задачи по ID"""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self._save_tasks()

    def search_tasks(self, keyword: Optional[str] = None, category: Optional[str] = None, status: Optional[str] = None) -> List[Task]:
        """Поиск задач по ключевому слову, категории или статусу"""
        results = self.tasks
        if keyword:
            results = [task for task in results if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        if category:
            results = [task for task in results if task.category == category]
        if status:
            results = [task for task in results if task.status == status]
        return results

    def edit_task(self, task_id: int, **kwargs):
        """Редактирование задачи"""
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            raise ValueError("Задача с указанным ID не найдена.")
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        self._save_tasks()
