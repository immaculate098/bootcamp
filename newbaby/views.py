from django.shortcuts import render, redirect, get_object_or_404
from .models import BabyArrival
from .forms import BabyArrivalForm

def arrival_form(request):
    if request.method == 'POST':
        form = BabyArrivalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('arrival_form')
    else:
        form = BabyArrivalForm()
    
    arrivals = BabyArrival.objects.all()
    return render(request, 'arrival_form.html', {'form': form, 'arrivals': arrivals})


def edit_arrival(request, id):
    arrival = get_object_or_404(BabyArrival, id=id)
    if request.method == 'POST':
        form = BabyArrivalForm(request.POST, instance=arrival)
        if form.is_valid():
            form.save()
            return redirect('arrival_form', id=id) 
    else:
        form = BabyArrivalForm(instance=arrival)
    
    return render(request, 'arrival_edit.html', {'form': form, 'arrival': arrival})


def delete_arrival(request, id):
    arrival = get_object_or_404(BabyArrival, id=id)
    if request.method == 'POST':
        arrival.delete()
        return redirect('arrival_form')
    
    return render(request, 'delete_arrival.html', {'arrival': arrival})

def read_baby_detail(request, id):
    arrival = get_object_or_404(BabyArrival, id=id)
    return render(request, 'read_baby_detail.html', {'arrival': arrival})


