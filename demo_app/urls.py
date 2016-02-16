# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^seasons/', views.SeasonListView, name='season-list'),
]
