
from django.urls import path
from .views import invent

urlpatterns = [
    path('invent/', invent, name='invent'),
]
