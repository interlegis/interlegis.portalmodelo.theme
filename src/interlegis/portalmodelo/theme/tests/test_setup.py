# -*- coding: utf-8 -*-
from interlegis.portalmodelo.theme.testing import INTEGRATION_TESTING
from plone.app.theming.utils import getAvailableThemes
from plone.app.theming.utils import getTheme
from plone.testing.z2 import Browser

import unittest

PROJECTNAME = 'interlegis.portalmodelo.theme'

DEPENDENCIES = [
    'plone.app.theming',
]


class InstallTestCase(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    profile = 'interlegis.portalmodelo.theme:default'

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.st = self.portal['portal_setup']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        for i in DEPENDENCIES:
            self.assertTrue(
                self.qi.isProductInstalled(i), u'{0} not installed'.format(i))

    def test_version(self):
        self.assertEqual(
            self.st.getLastVersionForProfile(self.profile),
            (u'1000',)
        )

    def test_temas_disponiveis(self):
        themes = getAvailableThemes()
        # Nosso tema + os dois do Plone
        self.assertEqual(len(themes), 10)

    def test_tema_Areia_disponivel(self):
        theme = getTheme('Areia')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Areia')
        self.assertEqual(theme.title, 'Tema Areia')
        self.assertEqual(theme.description,
                         'Tema Areia para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Areia/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Areia')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_Azul_disponivel(self):
        theme = getTheme('Azul')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Azul')
        self.assertEqual(theme.title, 'Tema Azul')
        self.assertEqual(theme.description,
                         'Tema Azul para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Azul/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Azul')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_Clean_disponivel(self):
        theme = getTheme('Clean')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Clean')
        self.assertEqual(theme.title, 'Tema Clean')
        self.assertEqual(theme.description,
                         'Tema Clean para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Clean/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Clean')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_Concreto_disponivel(self):
        theme = getTheme('Concreto')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Concreto')
        self.assertEqual(theme.title, 'Tema Concreto')
        self.assertEqual(theme.description,
                         'Tema Concreto para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Concreto/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Concreto')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_Gelo_disponivel(self):
        theme = getTheme('Gelo')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Gelo')
        self.assertEqual(theme.title, 'Tema Gelo')
        self.assertEqual(theme.description,
                         'Tema Gelo para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Gelo/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Gelo')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_Kiwi_disponivel(self):
        theme = getTheme('Kiwi')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Kiwi')
        self.assertEqual(theme.title, 'Tema Kiwi')
        self.assertEqual(theme.description,
                         'Tema Kiwi para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Kiwi/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Kiwi')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_Moderno_disponivel(self):
        theme = getTheme('Moderno')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Moderno')
        self.assertEqual(theme.title, 'Tema Moderno')
        self.assertEqual(theme.description,
                         'Tema Moderno para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Moderno/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Moderno')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_Vermelho_disponivel(self):
        theme = getTheme('Vermelho')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Vermelho')
        self.assertEqual(theme.title, 'Tema Vermelho')
        self.assertEqual(theme.description,
                         'Tema Vermelho para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Vermelho/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Vermelho')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_normalize_css_registered(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertIn(
            '++resource++portalmodelo.theme/styles/normalize.css',
            stylesheets_ids
        )

    def test_temabase_css_registered(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertIn(
            '++resource++portalmodelo.theme/styles/temabase.css',
            stylesheets_ids
        )

    def test_reset_css_registered(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertIn(
            '++resource++portalmodelo.theme/styles/reset.css',
            stylesheets_ids
        )


class StaticResourcesTestCase(unittest.TestCase):
    """Ensure static resources are available to our themes."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.st = self.portal['portal_setup']

    def test_static_resource(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')

    def test_icon_camara(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/images/icon_camara.gif' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')

    def test_icon_senado(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/images/icon_senado.gif' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')

    def test_logo(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/images/logo.png' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')

    def test_styles_normalize(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/styles/normalize.css' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')

    def test_styles_reset(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/styles/reset.css' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')

    def test_styles_temabase(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/styles/temabase.css' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')


class UninstallTestCase(unittest.TestCase):
    """Ensure product is properly uninstalled."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))
