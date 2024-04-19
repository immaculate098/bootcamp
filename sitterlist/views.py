from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from.models import Student


def immy_view(request):
    return render(request, 'sitterlist.html', {'students':Student.objects.all()})

def view_sitter(request,id):
    student =Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

