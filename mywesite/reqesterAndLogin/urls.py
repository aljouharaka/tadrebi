from django.conf.urls import  url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.req, name='index'),
    #/Student/712/

        #url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
]

urlpatterns += staticfiles_urlpatterns()