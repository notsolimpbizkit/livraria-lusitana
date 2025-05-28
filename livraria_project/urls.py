from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .admin import admin_site
from dashboard.views import dashboard_home

urlpatterns = [
    path('admin/', admin_site.urls),
    path('admin/dashboard/', dashboard_home, name='admin_dashboard'),
    path('', include('home.urls')),
    path('books/', include('books.urls')),
    path('api/', include('api.urls')),
    path('checkout/', include('checkout.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('contato/', include('contact.urls')),
    # We'll add more URLs later
]

# Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)