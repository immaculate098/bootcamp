from . import views
from django .urls import path
urlpatterns =[
    path('index_view/', views.index_view,name='index_view'),
]