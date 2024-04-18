from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def newbaby_view(request):
    template = loader.get_template('newbaby.html')
    return HttpResponse(template.render())
# Create your views here.

