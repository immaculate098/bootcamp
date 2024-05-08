from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from django.contrib.auth.decorators import login_required

@login_required
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



