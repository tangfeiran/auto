from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from models import Log, Task

class LogView(View):

    # def __init__(self, *args, **kwargs):
    #     super(LogView, self).__init__(*args, **kwargs)

    def get(self, request, facility):
        task = Task(id=facility)
        logs = Log.objects.filter(task=task)
        return render_to_response('log/index.html', context={"facility": facility, "logs": logs})

class SqlView(View):

    def get(self, request, facility):
        task = Task(id=facility)
        logs = Log.objects.filter(task=task)
        html_list = []
        for log in logs:
            html_list.append(log.log)
        html = "<br>".join(html_list) + "<br>"
        return HttpResponse(html)