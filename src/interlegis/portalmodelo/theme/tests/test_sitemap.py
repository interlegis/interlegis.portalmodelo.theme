# -*- coding: utf-8 -*-
from interlegis.portalmodelo.theme.interfaces import IBrowserLayer
from interlegis.portalmodelo.theme.testing import FUNCTIONAL_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing.z2 import Browser
from zope.interface.declarations import directlyProvides

import transaction
import unittest

PROJECTNAME = 'interlegis.portalmodelo.theme'


class SiteMapTestCase(unittest.TestCase):
    """"""

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        directlyProvides(self.request, IBrowserLayer)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.browser = Browser(app)
        self.setup_content()
        transaction.commit()

    def setup_content(self):
        portal = self.portal
        wt = portal.portal_workflow
        wt.setChainForPortalTypes(['Document', 'Folder'], ['simple_publication_workflow'],)
        # Create folder named folder1
        portal.invokeFactory('Folder', id='folder1', title='Visible Folder')
        self.folder1 = portal['folder1']
        wt.doActionFor(self.folder1, 'publish')
        # Create folder named folder2, excluded_from_nav
        portal.invokeFactory('Folder', id='folder2', title='Hidden Folder')
        self.folder2 = portal['folder2']
        self.folder2.setExcludeFromNav(True)
        wt.doActionFor(self.folder2, 'publish')
        # create subfolder on foo named subfolder
        self.folder2.invokeFactory('Folder', id='subfolder', title='Visible Subfolder')
        self.subfolder = self.folder2['subfolder']
        wt.doActionFor(self.subfolder, 'publish')
        # create page document on subfolder excluded_from_nav
        self.subfolder.invokeFactory('Document', id='document', title='Hidden Document')
        self.document = self.subfolder['document']
        self.document.setExcludeFromNav(True)
        wt.doActionFor(self.document, 'publish')

    def test_folder1_listed(self):
        browser = self.browser
        browser.open('%s/sitemap' % self.portal.absolute_url())
        self.assertIn('Visible Folder', browser.contents)

    def test_folder2_listed(self):
        browser = self.browser
        browser.open('%s/sitemap' % self.portal.absolute_url())
        self.assertIn('Hidden Folder', browser.contents)

    def test_subfolder_listed(self):
        browser = self.browser
        browser.open('%s/sitemap' % self.portal.absolute_url())
        self.assertIn('Visible Subfolder', browser.contents)

    def test_document_not_listed(self):
        self.document.setExcludeFromNav(True)
        self.document.reindexObject()
        transaction.commit()
        browser = self.browser
        browser.open('%s/sitemap' % self.portal.absolute_url())
        self.assertNotIn('Hidden Document', browser.contents)

    def test_document_listed(self):
        self.document.setExcludeFromNav(False)
        self.document.reindexObject()
        transaction.commit()
        browser = self.browser
        browser.open('%s/sitemap' % self.portal.absolute_url())
        self.assertIn('Hidden Document', browser.contents)
