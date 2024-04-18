from . import views
from django .urls import path
urlpatterns =[
    path('resetpassword/', views.resetpassword_view,name='resetpassword_view'),
]