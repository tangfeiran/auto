#coding:utf8
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from log.models import Task
from tasks import playbook_test


class MyTypicalView(View):

    def get(self, request):
        # pass
        task = Task(stat=u'任务已创建')
        task.save()
        facility = task.id
        # 用celery 部分callback不执行，不知为啥， 已改为子进程模式
        playbook_test.delay(facility=facility)
        # playbook_test(facility=facility)
        return HttpResponseRedirect('log/%s' % facility)