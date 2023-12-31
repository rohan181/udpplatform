from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# from servicename.views import ServiceViewSet
router = routers.DefaultRouter()
# router.register(r'Service', ServiceViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
