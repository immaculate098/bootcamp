from django.urls import path
from.import views

urlpatterns = [
path('sitterlist/',views.immy_view, name='immy_view'),
path('view_student/<int:id>/', views.view_student, name='view_student'),
path('added/', views.added,name='added'),
path('delete/<int:id>/', views.delete_student, name='delete_student'),
path('edit/<int:id>/', views.edit_student, name='edit_student'),
]
