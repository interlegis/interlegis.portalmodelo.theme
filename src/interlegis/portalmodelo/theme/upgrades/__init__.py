# -*- coding: utf-8 -*-

from plone import api


def cook_css_resources(context):  # pragma: no cover
    """Cook CSS resources."""
    css_tool = api.portal.get_tool('portal_css')
    css_tool.cookResources()
    


def cook_javascript_resources(context):  # pragma: no cover
    """Cook JavaScript resources."""
    js_tool = api.portal.get_tool('portal_javascripts')
    js_tool.cookResources()
    
