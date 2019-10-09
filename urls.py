from django.urls import path, include
from .utils import config
from .settings import DEBUG, STATIC_URL, STATIC_ROOT

from config.urls import app_url_patterns

urlpatterns = []

if config.get("admin", "enabled") == "true":
    from django.contrib import admin
    urlpatterns += [path('admin/', admin.site.urls)]

if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)

urlpatterns.extend(app_url_patterns)
