from . import views
from django .urls import path
urlpatterns =[
    path('newpassword/', views.newpassword_view,name='newpassword_view'),
]