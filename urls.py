from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from config.urls import app_url_patterns

from .utils import CONFIG
from .settings import DEBUG, STATIC_URL, STATIC_ROOT

urlpatterns = []

if CONFIG.get("admin", "enabled") == "true":
    urlpatterns += [path('admin/', admin.site.urls)]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

urlpatterns.extend(app_url_patterns)
