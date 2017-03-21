from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.IntegerField()
    stat = models.CharField(max_length=16)

class Log(models.Model):
    task_id = models.ForeignKey(Task)
    log = models.TextField()