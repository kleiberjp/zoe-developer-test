# -*- coding: utf-8 -*-
from django.conf import settings


def context_vars(request):
    context = {
        'STATIC_URL': settings.STATIC_URL,
    }
    return context
