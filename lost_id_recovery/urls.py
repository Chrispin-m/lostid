from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('0703175863/admin/', admin.site.urls),
    path('api/ids/', include('ids.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
