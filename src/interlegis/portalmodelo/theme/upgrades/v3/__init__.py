# -*- coding: utf-8 -*-
from plone.app.upgrade.utils import loadMigrationProfile
from plone import api


JS = 'http://htmlshiv.googlecode.com/svn/trunk/html5.js'
JS_NEW = 'https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js'


def deprecate_resource_registries(setup_tool):
    """Deprecate resource registries."""
    js_tool = api.portal.get_tool('portal_javascripts')
    if JS in js_tool.getResourceIds():
        js_tool.unregisterResource(id=JS)
    assert JS not in js_tool.getResourceIds()  # nosec    

def new_resource_registries(setup_tool):
    """Deprecate resource registries."""
    js_tool = api.portal.get_tool('portal_javascripts')
    if JS_NEW not in js_tool.getResourceIds():
        js_tool.registerResource(id=JS_NEW, expression='', enabled=1)
    assert JS_NEW in js_tool.getResourceIds()  # nosec    

   
    
