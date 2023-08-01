from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/templates/wishlist/wishlist.html', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]