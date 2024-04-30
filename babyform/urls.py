from django.urls import path
from babyform import views

urlpatterns = [
    path('babyform', views.baby_list, name='baby_list'),
    path('baby_detail/<int:pk>/', views.baby_detail, name='baby_detail'),
    path('baby_list/new/', views.baby_create, name='baby_create'),
    path('baby_form/<int:pk>/edit/', views.baby_edit, name='baby_edit'),
    path('baby_delete/<int:pk>/delete/', views.baby_delete, name='baby_delete'),
]
