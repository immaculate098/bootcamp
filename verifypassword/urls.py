from . import views
from django .urls import path
urlpatterns =[
    path('verifypassword/', views.verifypassword_view,name='verifypassword_view'),
]