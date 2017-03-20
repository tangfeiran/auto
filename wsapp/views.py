#coding:utf8
from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.views.generic.base import View
from wsapp.models import publish_message
from ws4redis.publisher import RedisPublisher
from ansibleapi.playbook import PlayBookJob
from ansibleapi.callback import ExtendCallback

class WsExtendCallback(ExtendCallback):

    def __init__(self, *args, **kwargs):
        super(WsExtendCallback, self).__init__(*args, **kwargs)
        self.facility = 'foobar'
        self.audience = {'broadcast': True}
        self.redis_publisher = RedisPublisher(facility=self.facility, **self.audience)

    def v2_runner_on_ok(self, *args, **kwargs):
        super(WsExtendCallback, self).v2_runner_on_ok(*args, **kwargs)

    # 自定义输出,格式清晰一些
    def zdy_stdout(self,result):
        msg = ''
        if result.get('delta',False):
            msg += u'\t执行时间:%s'%result['delta']
        if result.get('cmd', False):
            msg += u'\n执行命令:%s'%result['cmd']
        if result.get('stderr',False):
            msg += u'\n错误输出:\n%s'%result['stderr']
        if result.get('stdout',False):
            msg += u'\n正确输出:\n%s'%result['stdout']
        if result.get('warnings',False):
            msg += u'\n警告:%s'%result['warnings']
        publish_message(self.redis_publisher).send(msg.encode('utf-8'))
        return msg

class MyTypicalView(View):
    # facility = 'unique-named-facility'
    facility = 'foobar'
    audience = {'broadcast': True}

    def __init__(self, *args, **kwargs):
        super(MyTypicalView, self).__init__(*args, **kwargs)
        self.redis_publisher = RedisPublisher(facility=self.facility, **self.audience)

    def get(self, request):
        # last msg
        # print("last data: %s" % self.redis_publisher.fetch_message(request, facility=self.facility, audience='any'))
        pl = PlayBookJob(playbooks=['test.yml'],
                    host_list=['172.16.10.54', '172.16.10.53'],
                    remote_user='root',
                    group_name="test",
                    forks=20,
                    ext_vars=None,
                    passwords='123456'
                    )
        pl.callback = WsExtendCallback()
        pl.run()
        return HttpResponse('ok')