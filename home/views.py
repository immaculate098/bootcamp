from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home_view(request):
    
    return render(request, 'home.html')



# def home_view(request):
#     template = loader.get_template('home.html')
#     return HttpResponse(template.render())
