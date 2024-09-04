from .models import To_do


def filter_todo_with_id(todo_id):
    return To_do.objects.filter(id=todo_id)