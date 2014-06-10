# -*- coding: utf-8 -*-
'''
Created on 28/11/2013

@author: jpg
'''
from interlegis.portalmodelo.theme.browser.imagewidget import ImageWidget
from plone.app.controlpanel.site import ISiteSchema as IBaseSiteSchema
from plone.app.controlpanel.site import SiteControlPanel as BaseSiteControlPanel
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.CMFDefault.formlib.schema import SchemaAdapterBase,\
    ProxyFieldProperty
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope.component import adapts
from zope.interface import implements
from zope.formlib import form
from zope.schema import Bool
from zope.schema import Bytes
from zope.component.hooks import getSite


class ISiteSchema(IBaseSiteSchema):

    show_header_text = Bool(title=_(u'Display text in Header'),
                            description=_(u'Displays site title and description on every site pages.'),
                            required=False,
                            default=True)

    image = Bytes(title=_(u'Imagem do Logo'),
                  description=_(u'Insira nesse campo o logo do tema local'),
                  required=False)

    show_header_logo = Bool(title=_(u'Display logo in Header'),
                            description=_(u''),
                            required=False,
                            default=True)

    background = Bytes(title=_(u'Header background image'),
                       description=_(u''),
                       required=False)


class SiteControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(ISiteSchema)

    def __init__(self, context):
        super(SiteControlPanelAdapter, self).__init__(context)
        self.portal = getSite()
        pprop = getToolByName(self.portal, 'portal_properties')
        self.context = pprop.site_properties
        self.encoding = pprop.site_properties.default_charset

    def get_site_title(self):
        title = getattr(self.portal, 'title', u'')
        return safe_unicode(title)

    def set_site_title(self, value):
        self.portal.title = value.encode(self.encoding)

    def get_site_description(self):
        description = getattr(self.portal, 'description', u'')
        return safe_unicode(description)

    def set_site_description(self, value):
        if value is not None:
            self.portal.description = value.encode(self.encoding)
        else:
            self.portal.description = ''

    def get_webstats_js(self):
        description = getattr(self.context, 'webstats_js', u'')
        return safe_unicode(description)

    def set_webstats_js(self, value):
        if value is not None:
            self.context.webstats_js = value.encode(self.encoding)
        else:
            self.context.webstats_js = ''

    def get_image(self):
        return self.portal.get('logo.png')

    def set_image(self, image):
        if not image:
            return True
        if image == 'remove':
            self.portal.manage_delObjects(['logo.png'])
            return True
        # verifica se a imagem existe
        conteudo = [i.getId() for i in self.portal.objectValues()]
        if 'logo.png' not in conteudo:
            self.portal.manage_addImage('logo.png', image, 'logo.png')
            return True
        else:
            img = self.portal.get('logo.png')
            img.update_data(image)
            return True
        return False

    def get_background(self):
        return self.portal.get('background.png')

    def set_background(self, image):
        if not image:
            return True
        if image == 'remove':
            self.portal.manage_delObjects(['background.png'])
            return True
        # verifica se a imagem existe
        conteudo = [i.getId() for i in self.portal.objectValues()]
        if 'background.png' not in conteudo:
            self.portal.manage_addImage('background.png', image, 'background.png')
            return True
        else:
            img = self.portal.get('background.png')
            img.update_data(image)
            return True
        return False

    site_title = property(get_site_title, set_site_title)
    site_description = property(get_site_description, set_site_description)
    webstats_js = property(get_webstats_js, set_webstats_js)
    image = property(get_image, set_image)
    background = property(get_background, set_background)

    show_header_text = ProxyFieldProperty(ISiteSchema['show_header_text'])
    show_header_logo = ProxyFieldProperty(ISiteSchema['show_header_logo'])
    enable_sitemap = ProxyFieldProperty(ISiteSchema['enable_sitemap'])
    exposeDCMetaTags = ProxyFieldProperty(ISiteSchema['exposeDCMetaTags'])

    def get_display_pub_date_in_byline(self):
        return getattr(self.context.site_properties,
                       'displayPublicationDateInByline', False)

    def set_display_pub_date_in_byline(self, value):
        self.context.site_properties.displayPublicationDateInByline = value

    display_pub_date_in_byline = property(get_display_pub_date_in_byline,
                                          set_display_pub_date_in_byline)


class SiteControlPanel(BaseSiteControlPanel):

    form_fields = form.FormFields(ISiteSchema)
    form_fields['image'].custom_widget = ImageWidget
    form_fields['background'].custom_widget = ImageWidget
