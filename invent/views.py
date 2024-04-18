from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def invent_view(request):
    template = loader.get_template('invent.html')
    return HttpResponse(template.render())