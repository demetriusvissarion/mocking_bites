from unittest.mock import Mock
from lib.task_list import TaskList


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour
def test_adds_tasks_to_list():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    fake_task_1.title = "Walk the dog"
    fake_task_2.title = "Walk the cat"
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    assert task_list.tasks == [fake_task_1, fake_task_2]


def test_marks_tasks_as_complete():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    fake_task_1.title = "Walk the dog"
    fake_task_2.title = "Walk the cat"
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    fake_task_1.is_complete.return_value = True
    fake_task_2.is_complete.return_value = True
    assert task_list.all_complete() == True