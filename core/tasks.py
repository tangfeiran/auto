# coding:utf8
from __future__ import absolute_import, unicode_literals

from ansibleapi.playbook import PlayBookJob
from celery import shared_task

from core.models import WsExtendCallback


@shared_task
def playbook_test(facility, playbook):
    # last msg
    # print("last data: %s" % self.redis_publisher.fetch_message(request, facility=self.facility, audience='any'))
    pl = PlayBookJob(playbooks=["playbooks/%s" % playbook],
                     host_list=[
                         '172.16.10.54',
                         '172.16.10.53',
                     ],
                     remote_user='root',
                     group_name="test",
                     forks=20,
                     ext_vars=None,
                     passwords='123456',
                     )
    pl.callback = WsExtendCallback(facility)
    pl.run()
