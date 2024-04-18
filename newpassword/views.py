# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader



# def newpassword_view(request):
#     template = loader.get_template('newpassword.html')
#     return HttpResponse(template.render())

from django.shortcuts import render

def newpassword_view(request):
    return render(request, 'newpassword.html')
