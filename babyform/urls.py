from . import views
from django .urls import path
urlpatterns =[
    path('', views.babyform_view,name='babyform_view'),
]