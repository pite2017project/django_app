# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<object_id>\d+)/$', views.poll, name='poll'),
    url(r'^addPoll/$', views.create_poll, name='create_poll'),
    url(r'^(?P<object_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<object_id>\d+)/delete/(?P<object_id_2>\d+)$', views.delete_respond, name='delete_respond'),
    url(r'^(?P<object_id>\d+)/delete/$', views.delete_poll, name='delete_poll'),
]