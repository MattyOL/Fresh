from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('review/<int:product_id>/', views.product_review, name='product_review'),
    path('delete_review/<int:review_id>/<int:product_id>/', views.delete_review, name='delete_review'),
    path('update_review/<int:review_id>/<int:product_id>/', views.update_review, name='update_review')
]
