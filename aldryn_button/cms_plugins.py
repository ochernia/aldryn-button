# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ButtonPlugin


class ButtonCMSPlugin(CMSPluginBase):
    model = ButtonPlugin
    name = _("Button")
    render_template = 'aldryn_button/plugins/button.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ButtonCMSPlugin)
