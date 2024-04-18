from . import views
from django .urls import path
urlpatterns =[
    path('home/', views.index_view,name='index_view'),
]