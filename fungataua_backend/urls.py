
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import re_path
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/users/', include('users.urls')),
    path('api/client/', include('client.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    re_path(r'^.*\.*',  TemplateView.as_view(template_name="index.html"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)