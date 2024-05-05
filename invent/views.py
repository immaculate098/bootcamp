# views.py

from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

def invent(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invent')
    else:
        form = PaymentForm()

    payments = Payment.objects.all()
    return render(request, 'invent.html', {'form': form, 'payments': payments})



