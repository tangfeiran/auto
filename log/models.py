from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    stat = models.CharField(max_length=16)

class Log(models.Model):
    task = models.ForeignKey(Task)
    log = models.TextField()