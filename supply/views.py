
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def supply_view(request):
    template = loader.get_template('supply.html')
    return HttpResponse(template.render())
# Create your views here.
