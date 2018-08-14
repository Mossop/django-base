from django.conf.urls import include, url
from .utils import config

from config.urls import urlpatterns

if config.get("admin", "enabled") == "true":
    from django.contrib import admin
    urlpatterns.append(url(r'^admin/', admin.site.urls))
