from django.urls import path
from . import views

urlpatterns = [
    path('departure_form/', views.departure_form, name='departure_form'),
    path('edit_departure/edit/<int:id>/', views.edit_departure, name='edit_departure'),
    path('delete_departure/delete/<int:id>/', views.delete_departure, name='delete_departure'),
    path('read_baby_details/<int:id>/', views.read_baby_details, name='read_baby_details'),
]

