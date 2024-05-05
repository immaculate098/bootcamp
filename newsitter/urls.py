from django.urls import path
from .views import *


urlpatterns = [
    path('payment/', payment_form, name='payment_form'),
    path('payment_success/<str:baby_name>/<str:amount_paid>/<str:date_paid>/<str:payment_type>/<str:change_received>/', payment_success, name='payment_success'),
]
