from class_task import TaskManager
from task import Task

def main():
    manager = TaskManager()

    while True:
        print("\nМенеджер задач")
        print("1. Просмотр всех задач")
        print("2. Добавить задачу")
        print("3. Редактировать задачу")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            for task in manager.tasks:
                print(task.to_dict())
        elif choice == "2":
            title = input("Название: ")
            description = input("Описание: ")
            category = input("Категория: ")
            due_date = input("Срок выполнения (ГГГГ-ММ-ДД): ")
            priority = input("Приоритет (низкий, средний, высокий): ")
            try:
                task = Task(title, description, category, due_date, priority)
                manager.add_task(task)
                print("Задача добавлена.")
            except ValueError as e:
                print(e)
        elif choice == "3":
            task_id = int(input("ID задачи для редактирования: "))
            print("Оставьте поле пустым, если не хотите изменять.")
            new_title = input("Новое название: ")
            manager.edit_task(task_id, title=new_title)
        elif choice == "4":
            task_id = int(input("ID задачи для удаления: "))
            manager.delete_task(task_id)
            print("Задача удалена.")
        elif choice == "5":
            keyword = input("Ключевое слово для поиска: ")
            for task in manager.search_tasks(keyword=keyword):
                print(task.to_dict())
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
