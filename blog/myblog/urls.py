from django.conf.urls import url
from . import views

app_name = "myblog"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^single/([0-9]+)/$', views.single, name='single'),
    url(r'^category/([0-9]+)/$', views.category, name='category'),
    url(r'^tags/([0-9]+)/$', views.tags, name='tags'),
    url(r'^filetime/(.*?)/(.*?)/$', views.filetime, name='filetime'),
    url(r'^comment/(.*?)/$', views.comment, name='comment'),
]