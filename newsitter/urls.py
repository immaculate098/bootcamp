from django.urls import path
from .views import *


urlpatterns = [
path('paymentform/', paymentform, name='paymentform'),   
path('payment_lists/', payment_lists, name='payment_lists'),
path('edit_payment/<int:id>/',edit_payment, name='edit_payment'),
    
]
