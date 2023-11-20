import pytest
from lib.task_formatter import *
from unittest.mock import Mock

"""
Given an instance of the task class with title and completed
#format Returns the task formatted as a string.
"""
def test_if_returns_formated_string_for_complete():
    task = Mock()
    task.title = 'Walk the dog'
    task.complete = True
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == '[X] Walk the dog'


"""
Given an instance of the task class with title and not complete
#format Returns the task formatted as a string.
"""
def test_if_returns_formated_string_for_not_complete():
    task = Mock()
    task.title = 'Walk the dog'
    task.complete = False
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == '[ ] Walk the dog'