from . import views
from django .urls import path
urlpatterns =[
    path('forgot/', views.forgot_view,name='forgot_view'),
]