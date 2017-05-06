from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.rest_index, name='rest_index'),
    url(r'^new/$', views.rest_new, name='rest_new'),
    url(r'^(?P<id>\d+)/edit/$', views.rest_edit, name='rest_edit'),
    url(r'^(?P<id>\d+)/delete/$', views.rest_delete, name='rest_delete'),
]
