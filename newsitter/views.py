
from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

def payment_form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            
            if payment.payment_type == 'halfday':
                specified_amount = 10000
            elif payment.payment_type == 'fullday':
                specified_amount = 15000
            else:
                specified_amount = 0  
            
            payment.change_received = max(0, specified_amount - payment.amount_paid)
            payment.save()
            return redirect('payment_success', 
                            baby_name=payment.baby_name,
                            amount_paid=payment.amount_paid,
                            date_paid=payment.date_paid,
                            payment_type=payment.payment_type,
                            change_received=payment.change_received
                            )
            
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})


def payment_success(request, baby_name, amount_paid, date_paid, payment_type, change_received):
    payment = {
        'baby_name': baby_name,
        'amount_paid': amount_paid,
        'date_paid': date_paid,
        'payment_type': payment_type,
        'change_received': change_received,
    }
    return render(request, 'payment_success.html', {'payment': payment})