from . import views
from django .urls import path

urlpatterns =[
    path('login_view/', views.login_view,name='login_view'),
    
]