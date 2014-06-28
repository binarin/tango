# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about')
)
