#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from ansibleapi.callback import ExtendCallback
# from ansible.executor.task_result import TaskResult
from ansibleapi.display import MyDisplay
from log.models import Task, Log

class CallbackLog(object):

    def __init__(self, facility, audience, save_sql=True):
        '''
        初始化，实例RedisPublisher对象
        :param facility:
        :param audience:
        '''
        self.save_sql = save_sql
        if self.save_sql:
            self.task = Task(id=facility)
        self.redis_publisher = RedisPublisher(facility=facility, **audience)


    def ws(self, msg):
        message = RedisMessage(msg.encode('utf-8'))
        self.redis_publisher.publish_message(message)

    def save(self, msg):
        if self.save_sql:
            log = Log(task=self.task, log=msg.encode('utf-8'))
            log.save()

    def all(self, msg):
        self.ws(msg)
        self.save(msg)

class WsExtendCallback(ExtendCallback):

    def __init__(self, facility='default', audience={'broadcast': True}):

        super(WsExtendCallback, self).__init__()
        self.log = CallbackLog(facility=facility, audience=audience)
        self._display = MyDisplay(self.log.all)