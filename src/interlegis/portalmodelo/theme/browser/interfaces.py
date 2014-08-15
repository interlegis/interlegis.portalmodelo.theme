# -*- coding: utf-8 -*-
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from zope.interface import Interface


class IPortalModeloView(Interface):
    """
    """

    def getColumnsClass():
        """Return the CSS class for column content based on columns presence.
        """

    def getColumnsClasses():
        """Return all CSS classes based on columns presence.
        """


class IPortalModeloSiteMapStrategy(INavtreeStrategy):
    """
    """
