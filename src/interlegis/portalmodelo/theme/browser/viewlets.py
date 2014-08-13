# -*- coding: utf-8 -*-
from plone.app.layout.viewlets.common import LogoViewlet as BaseLogoViewlet
from plone.app.layout.viewlets.common import PathBarViewlet as BasePathBarViewlet
from plone.memoize import view
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component.hooks import getSite


class LogoViewlet(BaseLogoViewlet):
    index = ViewPageTemplateFile("templates/logo.pt")

    def update(self):
        super(LogoViewlet, self).update()

        portal = self.portal_state.portal()
        bprops = portal.restrictedTraverse('base_properties', None)
        if bprops is not None:
            logoName = bprops.logoName
        else:
            logoName = 'logo.jpg'

        logoTitle = self.portal_state.portal_title()
        self.logo_tag = portal.restrictedTraverse(logoName).tag(title=logoTitle, alt=logoTitle)
        self.navigation_root_title = self.portal_state.navigation_root_title()

        if logoName not in portal:
            self.logo_tag = '<img src="{0}/{1}" alt="{2}" title="{2}" height="80" width="80" />'.format(
                portal.absolute_url(),
                '++resource++portalmodelo.theme/images/logo.png',
                logoTitle
            )


class HeaderViewlet(BaseLogoViewlet):

    def logo_background_style(self):
        portal = getSite()
        if portal.get('background.png'):
            return 'background-image: url(' + portal.absolute_url() + '/background.png)'
        return ''


class PathBarViewlet(BasePathBarViewlet):

    """Override breadcrumbs to avoid displaying them at site root."""

    @view.memoize
    def visible(self):
        """Return True if we are not at site root."""
        return len(self.breadcrumbs) >= 1
