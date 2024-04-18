from . import views
from django .urls import path
urlpatterns =[
    path('', views.newsitter_view,name='newsitter_view'),
]