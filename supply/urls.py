# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('supply/', views.supply_item, name='supply_item'),
    path('issue/', views.issue_item, name='issue_item'),
    path('add/', views.add_supply, name='add_supply'),
]
