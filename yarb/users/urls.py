from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='users'
urlpatterns = [

    url(r'^$', views.user_profile,name="profile"),
    url(r'^create/$', views.user_create,name="create"),

]
