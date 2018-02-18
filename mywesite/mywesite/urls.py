
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tadrebi/', include('tadrebi.urls')),
    url(r'^regiser/', include('reqesterAndLogin.urls')),
]

urlpatterns += staticfiles_urlpatterns()