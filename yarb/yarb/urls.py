from.import views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from users import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', user_views.user,name="home"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^users/', include('users.urls')),
]

urlpatterns += staticfiles_urlpatterns ()
