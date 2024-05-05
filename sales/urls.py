from django.urls import path
from . import views

urlpatterns = [
    
    path('manage/', views.manage, name='manage'),
    path('issue_item/<int:pk>/', views.issue_item, name='issue_item'),
    path('add_to_stock/<int:pk>/', views.add_to_stock, name='add_to_stock'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt_detail/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('made_sales/', views.made_sales, name='made_sales'),
]
    

