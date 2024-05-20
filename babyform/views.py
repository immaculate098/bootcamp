from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import BabyForm
from sitterduty.models import Sitter


def baby_list(request):
    babies = Baby.objects.all()
    return render(request, 'baby_list.html', {'babies': babies})

def baby_detail(request, pk):
    baby = get_object_or_404(Baby, pk=pk)
    return render(request, 'baby_detail.html', {'baby': baby})

def baby_create(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            baby = form.save()
            return redirect('baby_list')  
    else:
        form = BabyForm()
    
    sitters = Sitter.objects.all()
    return render(request, 'baby_form.html', {'form': form, 'sitters': sitters})

def baby_edit(request, pk):
    baby = get_object_or_404(Baby, pk=pk)
    if request.method == 'POST':
        form = BabyForm(request.POST, instance=baby)
        if form.is_valid():
            baby = form.save()
            return redirect('baby_list')  
    else:
        form = BabyForm(instance=baby)
    
    sitters = Sitter.objects.all()
    return render(request, 'baby_form.html', {'form': form, 'sitters': sitters})


def baby_delete(request, pk):
    baby = get_object_or_404(Baby, pk=pk)
    baby.delete()
    return redirect('baby_list')
