from . import views
from django .urls import path
urlpatterns =[
    path('', views.supply_view,name='supply_view'),
]