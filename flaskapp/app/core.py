from app.models import Task


def count_priority(task):
    assert isinstance(task, Task)
    score = task.importance + task.urgency - task.complexity
    return score
