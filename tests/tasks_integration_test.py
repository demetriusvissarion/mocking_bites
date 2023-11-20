from lib.task import Task
from lib.task_list import TaskList
from lib.task_formatter import TaskFormatter


def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]


def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True


"""
Given an instance of the task class with title and completed
#format Returns the task formatted as a string.
"""
def test_if_returns_formated_string_for_complete():
    task = Task('Walk the dog')
    task.complete = True
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == '[X] Walk the dog'


"""
Given an instance of the task class with title and not complete
#format Returns the task formatted as a string.
"""
def test_if_returns_formated_string_for_not_complete():
    task = Task('Walk the dog')
    task.complete = False
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == '[ ] Walk the dog'