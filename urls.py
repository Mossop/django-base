from django.urls import path, include
from .utils import config

from config.urls import urlpatterns

if config.get("admin", "enabled") == "true":
    from django.contrib import admin
    urlpatterns.append(path('admin/', admin.site.urls))
