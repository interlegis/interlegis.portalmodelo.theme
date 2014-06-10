# -*- coding: utf-8 -*-
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import interlegis.portalmodelo.theme
        self.loadZCML(package=interlegis.portalmodelo.theme)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'interlegis.portalmodelo.theme:default')


FIXTURE = Fixture()


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='interlegis.portalmodelo.theme:Integration')

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='interlegis.portalmodelo.theme:Functional')
