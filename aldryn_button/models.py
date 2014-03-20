# -*- coding: utf-8 -*-
import re

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PageField
from cms.models.pluginmodel import CMSPlugin

from filer.fields.file import FilerFileField


class ButtonPlugin(CMSPlugin):
    translatable_content_excluded_fields = ['url', 'page_link', 'target', 'mailto', 'phone', 'css_classes', 'css_id']

    name = models.CharField(_('Name'), max_length=256)
    url = models.URLField(_('Link'), blank=True, null=True)
    page_link = PageField(verbose_name=_('Page'), blank=True, null=True,
                          help_text=_('A link to a page has priority over a text link.'))
    target = models.CharField(_('target'), blank=True, max_length=100, choices=((('', _('same window')),
                                                                                 ('_blank', _('new window')),
                                                                                 ('_parent', _('parent window')),
                                                                                 ('_top', _('topmost frame')),
                                                                                )))
    mailto = models.EmailField(_('Mailto'), blank=True, null=True,
                               help_text=_('An email adress has priority over a page link.'))
    phone = models.CharField(_('Phone'), blank=True, null=True, max_length=40,
                             help_text=_('A phone number has priority over a mailto link.'))
    file = FilerFileField(verbose_name=_('File'), null=True, blank=True,
                          help_text=_('A file has priority over a phone number.'))

    css_classes = models.CharField(_('css classes'), blank=True, null=True, max_length=255)
    css_id = models.CharField(_('css id'), blank=True, null=True, max_length=255)

    def __unicode__(self):
        return self.name

    def get_link(self):
        if self.file:
            return self.file.url
        if self.phone:
            return 'tel:%s' % re.sub('[- ]', '', self.phone)
        if self.mailto:
            return 'mailto:%s' % self.mailto
        if self.page_link:
            return self.page_link.get_absolute_url()
        if self.url:
            return self.url
        return '#'
