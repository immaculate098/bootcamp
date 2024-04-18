from . import views
from django .urls import path
urlpatterns =[
    path('', views.babycheck_view,name='babycheck_view'),
]