from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
