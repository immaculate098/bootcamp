from django.urls import path
from.import views

urlpatterns = [
path('sitterlist/',views.immy_view, name='immy_view'),
path('<int:id>', views.view_sitter, name='view_sitter'),

]
