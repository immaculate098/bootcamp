from django.urls import path
from babyform import views

urlpatterns = [
    path('baby_list/', views.baby_list, name='baby_list'),
    path('baby_detail/<int:pk>/', views.baby_detail, name='baby_detail'),
    path('baby_create/', views.baby_create, name='baby_create'),
    path('baby_edit/<int:pk>/', views.baby_edit, name='baby_edit'),
    path('baby_delete/<int:pk>/', views.baby_delete, name='baby_delete')
]
