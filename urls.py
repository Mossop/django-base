from django.conf.urls import include, url
from .utils import config

urlpatterns = [
    url(r'^', include('website.urls'))
]

if config.get("admin", "enabled") == "true":
    from django.contrib import admin
    urlpatterns.append(url(r'^admin/', admin.site.urls))
