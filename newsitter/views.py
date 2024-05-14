from django.shortcuts import render,redirect,get_object_or_404
from django. http import HttpResponse, HttpResponseRedirect
from.forms import*
from. models import*
from . filters import *

def payment_lists(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            print("test")
            return redirect('paymentform')
    else:
        form = PaymentForm()
    

    return render(request, 'payment_lists.html', {'form': form})



def paymentform(request):
  payment_list=Payment.objects.all().order_by('id')
  payment_filter=payment_Filter(request.GET,queryset=payment_list)
  payment_list=payment_filter.qs
  return render(request,'paymentform.html',{'payment_list':payment_list, 'payment_filter':payment_filter})


 

def edit_payment(request,id):
    payment=get_object_or_404(Payment,id=id)
    if request.method == 'POST':  
       form=PaymentForm(request.POST,instance=payment)
       if form.is_valid():
           form.save()
           return redirect('paymentform')
    else:
            form=PaymentForm(instance=payment) 
    return render(request,'edit_payments.html',{'form':form,'payment':payment})