# -*- coding: utf-8 -*-
from django.forms import Form, CharField
from django.core.validators import MinLengthValidator
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _


class AgentsForm(Form):
    zipcode_agent1 = CharField(
        label=(_(u'ZipCode Agent 1')),
        max_length=11,
        validators=[MinLengthValidator(4)],
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': (_(u'Zipcode')),
                'type': 'number',
            }
        ), required=True
    )

    zipcode_agent2 = CharField(
        label=(_(u'ZipCode Agent 2')),
        max_length=11,
        validators=[MinLengthValidator(4)],
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': (_(u'Zipcode')),
                'type': 'number',
            }
        ), required=True
    )