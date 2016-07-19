# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Agent(models.Model):

    name = models.CharField(
        max_length=80,
        verbose_name=(_(u"Name User")),
        blank=True,
        null=True
    )
    zipcode = models.IntegerField(
        verbose_name=(_(u"Zip Code")),
        blank=True,
        null=True
    )

    def __unicode__(self):

        return '%s' % self.name

    class Meta:
        verbose_name = (_("Agent"))
        verbose_name_plural = (_("Agents"))
        db_table = 'agent'