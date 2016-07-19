# -*- coding: utf-8 -*-
import json as j
from django.utils.translation import ugettext_lazy as _
from json import dumps
from json import JSONEncoder
from django.http import HttpResponse
from django.utils.encoding import force_unicode
from django.utils.functional import Promise
from rest_framework.authentication import SessionAuthentication


NOT_MATCH_EXIST = (_(u"There are none match for the zipcode given, please try with one diferent."))
ERROR = (_(u"Oops something went wrong, try again."))


def errors(form):
    errors = []
    for field in form.fields:
        dictionary = {}
        if form[field].errors:
            dictionary['field'] = field
            try:
                dictionary['message'] = ', '.join(list(form[field].errors))
            except:
                dictionary['message'] = ', '.join((u"%s" % error) for error in form[field].errors)
            errors.append(dictionary)
    return errors


def form_invalid(form):
    context = {
        'hasErrors': True,
        'errors': errors(form),
        'success': False,
    }
    return render_to_json(context)


class LazyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj


def render_to_json(context):
    return HttpResponse(
        content=dumps(context, cls=LazyEncoder, indent=4),
        content_type='application/json'
    )


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return