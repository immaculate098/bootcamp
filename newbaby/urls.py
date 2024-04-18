from . import views
from django .urls import path
urlpatterns =[
    path('', views.newbaby_view,name='newbaby_view'),
]