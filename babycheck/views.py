from django.shortcuts import render, redirect, get_object_or_404
from .models import BabyDeparture
from .forms import BabyDepartureForm
from django.contrib.auth.decorators import login_required

@login_required

def departure_form(request):
    if request.method == 'POST':
        form = BabyDepartureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('departure_form')
    else:
        form = BabyDepartureForm()
    
    departures = BabyDeparture.objects.all()
    return render(request, 'departure_form.html', {'form': form, 'departures': departures})

@login_required
def edit_departure(request, id):
    departure = get_object_or_404(BabyDeparture, id=id)
    if request.method == 'POST':
        form = BabyDepartureForm(request.POST, request.FILES, instance=departure)
        if form.is_valid():
            form.save()
            return redirect('departure_form')
    else:
        form = BabyDepartureForm(instance=departure)
    
    return render(request, 'edit_departure.html', {'form': form})

@login_required
def delete_departure(request, id):
    departure = get_object_or_404(BabyDeparture, id=id)
    if request.method == 'POST':
        departure.delete()
        return redirect('departure_form')
    
    return render(request, 'delete_departure.html', {'departure': departure})

@login_required
def read_baby_details(request, id):
    departure = get_object_or_404(BabyDeparture, id=id)
    return render(request, 'baby_details.html', {'departure': departure})

