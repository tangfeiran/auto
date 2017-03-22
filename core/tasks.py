#coding:utf8
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from ansibleapi.playbook import PlayBookJob
from core.models import WsExtendCallback

@shared_task
def playbook_test(facility):
    # last msg
    # print("last data: %s" % self.redis_publisher.fetch_message(request, facility=self.facility, audience='any'))
    pl = PlayBookJob(playbooks=['test.yml'],
                     host_list=[
                         '172.16.10.54',
                         '172.16.10.53',
                     ],
                     remote_user='root',
                     group_name="test",
                     forks=20,
                     ext_vars={"cmd": "test"},
                     passwords='123456',
                     )
    pl.callback = WsExtendCallback(facility)
    pl.run()
