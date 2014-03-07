# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PageField
from cms.models.pluginmodel import CMSPlugin


class ButtonPlugin(CMSPlugin):
    name = models.CharField(_('Name'), max_length=256)
    url = models.URLField(_('Link'), blank=True, null=True)
    page_link = PageField(verbose_name=_('Page'), blank=True, null=True,
                          help_text=_('A link to a page has priority over a text link.'))
    target = models.CharField(_('target'), blank=True, max_length=100, choices=((('', _('same window')),
                                                                                 ('_blank', _('new window')),
                                                                                 ('_parent', _('parent window')),
                                                                                 ('_top', _('topmost frame')),
                                                                                )))

    css_classes = models.CharField(_('css classes'), blank=True, null=True, max_length=255)
    css_id = models.CharField(_('css id'), blank=True, null=True, max_length=255)

    def __unicode__(self):
        return self.name

    def get_link(self):
        if self.page_link:
            return self.page_link.get_absolute_url()
        if self.url:
            return self.url
        return False
