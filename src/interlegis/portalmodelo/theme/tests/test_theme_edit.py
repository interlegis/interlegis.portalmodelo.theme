# -*- coding: utf-8 -*-

from interlegis.portalmodelo.theme.interfaces import IBrowserLayer
from interlegis.portalmodelo.theme.testing import INTEGRATION_TESTING, FUNCTIONAL_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID, SITE_OWNER_NAME, SITE_OWNER_PASSWORD
from plone.testing.z2 import Browser
from zope.interface.declarations import directlyProvides

import unittest

PROJECTNAME = 'interlegis.portalmodelo.theme'


class ThemeEditTestCase(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.qi = self.portal['portal_quickinstaller']
        directlyProvides(self.request, IBrowserLayer)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_site_controlpanel(self):
        controlpanel = self.portal.restrictedTraverse('@@site-controlpanel')
        controlpanel.setUpWidgets()
        self.assertIsNotNone(controlpanel.widgets.get('image'))
        self.assertIsNotNone(controlpanel.widgets.get('background'))


class SiteControlpanelTestCase(unittest.TestCase):

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']

    def test_adding(self):
        browser = Browser(self.app)
        browser.open(self.portal.absolute_url() + '/login_form')
        browser.getControl(name='__ac_name').value = SITE_OWNER_NAME
        browser.getControl(name='__ac_password').value = SITE_OWNER_PASSWORD
        browser.getControl(name='submit').click()
        browser.open(self.portal.absolute_url() + '/@@site-controlpanel')
        self.assertTrue('Site settings' in browser.contents)
        browser.getControl('Save').click()
        self.assertTrue('Site settings' in browser.contents)
        self.assertTrue('Changes saved' in browser.contents)
