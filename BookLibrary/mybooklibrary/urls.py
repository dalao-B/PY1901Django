from django.conf.urls import url
from . import views

app_name = "mybooklibrary"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^reader_login/$', views.reader_login, name="reader_login"),
    url(r'^reader/$', views.reader, name="reader"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reader_info/$', views.reader_info, name='reader_info'),
    url(r'^reader_modify/$', views.reader_modify, name='reader_modify'),
    url(r'^reader_query/$', views.reader_query, name='reader_query'),
    url(r'^reader_book/(\d+)/$', views.reader_book, name='reader_book'),
    url(r'^reader_histroy/$', views.reader_histroy, name='reader_histroy'),
]