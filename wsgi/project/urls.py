# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [

    url(r'^admin', include(admin.site.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'', include('apps.base.urls')),
]

if settings.DEBUG:
    from django.views.static import serve

    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                serve, {
                                    'document_root': settings.STATIC_ROOT,
                                    'show_indexes': True
                                }
                                ),
                            url(r'^media/(?P<path>.*)$',
                                serve, {
                                    'document_root': settings.MEDIA_ROOT,
                                    'show_indexes': True
                                }
                                ),
                            )



