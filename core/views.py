# coding:utf8
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from log.models import Task
from tasks import playbook_test

PLAYBOOK_CHOICES = (
    ("test.yml", "test.yml"),
    ("test2.yml", "test2.yml"),
    ("test3.yml", "test3.yml"),
)


class MyForm(forms.Form):
    playbook = forms.ChoiceField(choices=PLAYBOOK_CHOICES, label='选择playbook')


class MyTaskView(View):
    def get(self, request):
        form = MyForm()
        return render(request, "log/mytask.html", {'form': form})

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            playbook = form.cleaned_data['playbook']
            task = Task(stat=u'任务已创建')
            task.save()
            facility = task.id
            playbook_test.delay(facility=facility, playbook=playbook)
            return HttpResponseRedirect('log/%s' % facility)
        else:
            form = MyForm()
            return render(request, "log/mytask.html", {'form': form})
