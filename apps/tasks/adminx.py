import xadmin
from .models import Tasks


class TasksAdmin(object):
    list_display = [
        'title',
        'days',
        'add_time'
    ]


xadmin.site.register(Tasks, TasksAdmin)
