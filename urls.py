from django.conf.urls import patterns, include, url
from utils import config

urlpatterns = patterns('',
    url(r'^', include('website.urls'))
)

if config.get("admin", "enabled") == "true":
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += patterns('',
        (r'^admin/', include(admin.site.urls)),
    )
