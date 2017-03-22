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
    #
    # def v2_runner_on_failed(self, result, ignore_errors=False):
    #     print "v2_runner_on_failed"
    #
    # def v2_runner_on_ok(self, result):
    #     print "v2_runner_on_ok"
    #
    # def v2_runner_on_skipped(self, result):
    #     print "v2_runner_on_skipped"
    #
    # def v2_runner_on_unreachable(self, result):
    #     print "v2_runner_on_unreachable"
    #
    # def v2_playbook_on_no_hosts_matched(self):
    #     print "v2_playbook_on_no_hosts_matched"
    #
    # def v2_playbook_on_no_hosts_remaining(self):
    #     print "v2_playbook_on_no_hosts_remaining"
    #
    # def v2_playbook_on_task_start(self, task, is_conditional):
    #     print "v2_playbook_on_task_start"
    #
    # def _print_task_banner(self, task):
    #     print "_print_task_banner"
    #
    # def v2_playbook_on_cleanup_task_start(self, task):
    #     print "v2_playbook_on_cleanup_task_start"
    #
    # def v2_playbook_on_handler_task_start(self, task):
    #     print "v2_playbook_on_handler_task_start"
    #
    # def v2_playbook_on_play_start(self, play):
    #     print "v2_playbook_on_play_start"
    #
    # def v2_on_file_diff(self, result):
    #     print "v2_playbook_on_play_start"
    #
    # def v2_runner_item_on_ok(self, result):
    #     print "v2_runner_item_on_ok"
    #
    # def v2_runner_item_on_failed(self, result):
    #     print "v2_runner_item_on_failed"
    #
    # def v2_runner_item_on_skipped(self, result):
    #     print "v2_runner_item_on_skipped"
    #
    # def v2_playbook_on_include(self, included_file):
    #     print "v2_playbook_on_include"
    #
    # def v2_playbook_on_stats(self, stats):
    #     print "v2_playbook_on_stats"
    #
    # def v2_playbook_on_start(self, playbook):
    #     print "v2_playbook_on_start"
    #
    # def v2_runner_retry(self, result):
    #     print "v2_runner_retry"




