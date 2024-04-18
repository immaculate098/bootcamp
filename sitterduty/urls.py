from . import views
from django .urls import path
urlpatterns =[
    path('', views.sitterduty_view,name='sitterduty_view'),
]