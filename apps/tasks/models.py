from django.db import models

# Create your models here.
from datetime import datetime


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    days = models.IntegerField(default=3)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = verbose_name
