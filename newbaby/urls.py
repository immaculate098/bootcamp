from django.urls import path
from . import views

urlpatterns = [
    path('arrival_form/', views.arrival_form, name='arrival_form'),  
    path('edit_arrival/edit/<int:id>/', views.edit_arrival, name='edit_arrival'),  
    path('delete_arrival/delete/<int:id>/', views.delete_arrival, name='delete_arrival'),  
    path('read_baby_detail/<int:id>/', views.read_baby_detail, name='read_baby_detail'),   
]
