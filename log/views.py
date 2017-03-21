from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.shortcuts import render_to_response

class LogView(View):

    # def __init__(self, *args, **kwargs):
    #     super(LogView, self).__init__(*args, **kwargs)

    def get(self, request, facility):
        return render_to_response('log/index.html', context={"facility": facility})