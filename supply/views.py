from django.shortcuts import render, redirect
from .models import *
from .forms import SupplyForm, IssuingForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def supply_item(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supply_item')
    else:
        form = SupplyForm()
    supplies = Supply.objects.all()
    return render(request, 'supply.html', {'form': form, 'supplies': supplies})

@login_required
def issue_item(request):
    if request.method == 'POST':
        form = IssuingForm(request.POST)
        if form.is_valid():
            issuing = form.save(commit=False)
            issuing.save()
            
            
            item_id = form.cleaned_data['item'].id
            quantity_issued = form.cleaned_data['quantity']
            supply = Supply.objects.get(item_id=item_id)
            supply.quantity -= quantity_issued
            supply.save()

            return redirect('issue_item')
    else:
        form = IssuingForm()
    issuings = Issuing.objects.all()
    return render(request, 'issue.html', {'form': form, 'issuings': issuings})



@login_required
def add_supply(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']
            
            existing_supply = Supply.objects.filter(item=item).first()
            if existing_supply:
                existing_supply.quantity += quantity
                existing_supply.save()
            else:
                Supply.objects.create(item=item, quantity=quantity)

    
            return redirect('supply_item')
    else:
        form = SupplyForm()
    return render(request, 'add_supply.html', {'form': form})
