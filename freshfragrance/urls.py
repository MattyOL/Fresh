from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, error404_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('blog/', include('blog.urls')),
    path('inbox/', include('inbox.urls')),
    path('error404_page/', error404_page, name='404'),
    path("accounts/", include("accounts.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'freshfragrance.views.handler404'
