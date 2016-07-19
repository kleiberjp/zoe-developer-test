# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.WebSiteViewClass.as_view(),
        name='website'
        ),
    url(r'^v1.0/agents-match$',
        views.AgentsMatchViewClass.as_view(),
        name='match'),
    url(r'^v1.0/load-contacts$',
        views.ContactLoadCSVViewClass.as_view(),
        name='load-csv'),
)