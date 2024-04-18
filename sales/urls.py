from . import views
from django .urls import path
urlpatterns =[
    path('', views.sales_view,name='sales_view'),
]
