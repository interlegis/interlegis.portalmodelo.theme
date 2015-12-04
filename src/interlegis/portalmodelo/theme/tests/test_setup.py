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
        # Nossos temas + os dois do Plone
        self.assertEqual(len(themes), 19)

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

    def test_tema_idg_amarelo_disponivel(self):
        theme = getTheme('IDG-amarelo')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'IDG-amarelo')
        self.assertEqual(theme.title, 'IDG - Tema Amarelo')
        self.assertEqual(theme.description,
                         'Tema amarelo para o Portal Modelo, baseado na Identidade Digital do Governo')
        self.assertEqual(theme.rules, '/++theme++IDG-amarelo/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++IDG-amarelo')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_idg_azul_disponivel(self):
        theme = getTheme('IDG-azul')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'IDG-azul')
        self.assertEqual(theme.title, 'IDG - Tema Azul')
        self.assertEqual(theme.description,
                         'Tema azul para o Portal Modelo, baseado na Identidade Digital do Governo')
        self.assertEqual(theme.rules, '/++theme++IDG-azul/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++IDG-azul')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_idg_branco_disponivel(self):
        theme = getTheme('IDG-branco')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'IDG-branco')
        self.assertEqual(theme.title, 'IDG - Tema Branco')
        self.assertEqual(theme.description,
                         'Tema branco para o Portal Modelo, baseado na Identidade Digital do Governo')
        self.assertEqual(theme.rules, '/++theme++IDG-branco/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++IDG-branco')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_idg_verde_disponivel(self):
        theme = getTheme('IDG-verde')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'IDG-verde')
        self.assertEqual(theme.title, 'IDG - Tema Verde')
        self.assertEqual(theme.description,
                         'Tema verde para o Portal Modelo, baseado na Identidade Digital do Governo')
        self.assertEqual(theme.rules, '/++theme++IDG-verde/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++IDG-verde')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_idg_rosa_disponivel(self):
        theme = getTheme('IDG-rosa')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'IDG-rosa')
        self.assertEqual(theme.title, 'IDG - Tema Rosa')
        self.assertEqual(theme.description,
                         'Tema outubro rosa para o Portal Modelo, baseado na Identidade Digital do Governo')
        self.assertEqual(theme.rules, '/++theme++IDG-rosa/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++IDG-rosa')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_idg_azul_11_disponivel(self):
        theme = getTheme('IDG-azul-11')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'IDG-azul-11')
        self.assertEqual(theme.title, 'IDG - Tema Novembro Azul')
        self.assertEqual(theme.description,
                         'Tema novembro azul para o Portal Modelo, baseado na Identidade Digital do Governo')
        self.assertEqual(theme.rules, '/++theme++IDG-azul-11/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++IDG-azul-11')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_original_disponivel(self):
        theme = getTheme('Original')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Original')
        self.assertEqual(theme.title, 'Tema Original')
        self.assertEqual(theme.description,
                         'Tema Original do Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Original/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Original')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_apucarana_disponivel(self):
        theme = getTheme('Apucarana')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Apucarana')
        self.assertEqual(theme.title, 'Tema Apucarana')
        self.assertEqual(theme.description,
                         'Tema Apucarana para o Portal Modelo, inspirado pela Câmara Municipal de Apucarana')
        self.assertEqual(theme.rules, '/++theme++Apucarana/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Apucarana')
        self.assertEqual(theme.doctype, "<!DOCTYPE html>")

    def test_tema_interlegis_disponivel(self):
        theme = getTheme('Interlegis')
        self.assertTrue(theme is not None)
        self.assertEqual(theme.__name__, 'Interlegis')
        self.assertEqual(theme.title, 'Tema Interlegis')
        self.assertEqual(theme.description,
                         'Tema Interlegis para o Portal Modelo')
        self.assertEqual(theme.rules, '/++theme++Interlegis/rules.xml')
        self.assertEqual(theme.absolutePrefix, '/++theme++Interlegis')
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

    def test_icon_interlegis(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/images/interlegis.png' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')

    def test_icon_cc(self):
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++portalmodelo.theme/images/cc-by-sa.png' % portal_url)
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

    def test_uninstalled(self):
        self.qi.uninstallProducts(products=[PROJECTNAME])
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))
