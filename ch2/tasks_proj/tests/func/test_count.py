"""Test the tasks.add() API function."""

import tasks
from tasks import Task


def test_number_of_tasks_is_int():
    """tasks.count() should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)
