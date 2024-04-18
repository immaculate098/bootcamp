from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def newsitter_view(request):
    template = loader.get_template('newsitter.html')
    return HttpResponse(template.render())
# Create your views here.

