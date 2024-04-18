from . import views
from django .urls import path
urlpatterns =[
    path('sitterForm/', views.sitterform_view,name='sitterform_view'),
]
