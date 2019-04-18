from django.conf.urls import url
from . import  views

app_name = "booktest"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$',views.list, name='list'),
    url(r'^detail/([0-9]+)/$', views.detail, name='detail'),
    url(r'^delete/([0-9]+)/$', views.delete, name='delete'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^addherohandler/$', views.addherohandler, name='addherohandler')
]