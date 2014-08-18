# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from interlegis.portalmodelo.theme.browser.interfaces import IPortalModeloSiteMapStrategy
from plone.app.layout.navigation.navtree import buildFolderTree
from Products.CMFPlone.browser.interfaces import ISiteMap
from Products.CMFPlone.browser.navtree import SitemapNavtreeStrategy
from Products.CMFPlone.browser.navtree import SitemapQueryBuilder
from Products.Five import BrowserView
from zope.component import getMultiAdapter
from zope.interface import implements


class InterlegisSitemapNavtreeStrategy(SitemapNavtreeStrategy):
    """An updated navtree strategy that lists also all folder on root level
    even if they are hidden from naviagation. used only for sitemap construction
    """
    implements(IPortalModeloSiteMapStrategy)

    def nodeFilter(self, node):
        item = node['item']
        depth = node.get('depth', 0)
        is_folder = True if getattr(item, 'portal_type', '') == 'Folder' else False
        if getattr(item, 'getId', None) in self.excludedIds:
            return False
        elif getattr(item, 'exclude_from_nav', False) and depth > 1 and not is_folder:
            # We want to display folder contents on root level
            return False
        else:
            return True


class CatalogSiteMap(BrowserView):
    implements(ISiteMap)

    def siteMap(self):
        context = aq_inner(self.context)
        queryBuilder = SitemapQueryBuilder(context)
        query = queryBuilder()
        strategy = getMultiAdapter((context, self), IPortalModeloSiteMapStrategy)
        return buildFolderTree(context, obj=context, query=query, strategy=strategy)
