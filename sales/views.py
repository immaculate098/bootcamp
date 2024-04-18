from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def sales_view(request):
    template = loader.get_template('sales.html')
    return HttpResponse(template.render())
