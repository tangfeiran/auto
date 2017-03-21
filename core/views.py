#coding:utf8
from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.views.generic.base import View
from ansibleapi.playbook import PlayBookJob
from models import WsExtendCallback

class MyTypicalView(View):

    def get(self, request):
        # last msg
        # print("last data: %s" % self.redis_publisher.fetch_message(request, facility=self.facility, audience='any'))
        pl = PlayBookJob(playbooks=['test.yml'],
                    host_list=[
                        '172.16.10.54',
                        # '172.16.10.53',
                    ],
                    remote_user='root',
                    group_name="test",
                    forks=20,
                    ext_vars=None,
                    passwords='123456'
                    )
        pl.callback = WsExtendCallback(facility='111111')
        pl.run()
        return HttpResponse('ok')