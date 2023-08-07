from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('send_email_with_discount/', views.send_email_with_discount, name='send_email_with_discount'),
    path('send_discount_email/', views.my_view, name='send_discount_email'),
    
]

