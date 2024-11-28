import pytest
from class_task import TaskManager
from task import Task

@pytest.fixture
def setup_manager():
    manager = TaskManager(data_file="test_data.json")
    manager.tasks = []
    return manager

def test_add_task(setup_manager):
    task = Task("Test", "Description", "Work", "2024-12-01", "High")
    setup_manager.add_task(task)
    assert len(setup_manager.tasks) == 1

def test_delete_task(setup_manager):
    task = Task("Test", "Description", "Work", "2024-12-01", "High")
    setup_manager.add_task(task)
    setup_manager.delete_task(1)
    assert len(setup_manager.tasks) == 0



