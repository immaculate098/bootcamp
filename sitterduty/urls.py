from . import views
from django .urls import path
from .views import DeleteSitterView, UpdateSitterView
urlpatterns =[
    path('sitterduty/', views.sitter_management,name='sitter_management'),
    path('add_sitter/', views.add_sitter, name='add_sitter'),
    path('save_changes/', views.save_changes, name='save_changes'), 
    path('sitter/<int:sitter_id>/delete/', DeleteSitterView.as_view(), name='delete_sitter'),
    path('sitter/<int:sitter_id>/update/', UpdateSitterView.as_view(), name='update_sitter'),

]