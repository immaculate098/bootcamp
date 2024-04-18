from . import views
from django .urls import path
urlpatterns =[
    path('', views.invent_view,name='invent_view'),
]