# -*- coding: utf-8 -*-

from interlegis.portalmodelo.theme.interfaces import IStream
from plone import api
from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.portlets import base
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.formlib import form
from zope.interface import alsoProvides
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def PossibleOptions(context):
    values = [(SimpleTerm(value='audio', title=_(u'Áudio'))), (SimpleTerm(value='video', title=_(u'Vídeo')))]

    return SimpleVocabulary(values)

alsoProvides(PossibleOptions, IContextSourceBinder)

def PossibleStreams(context):
    ct = api.portal.get_tool(name='portal_catalog')
    results = ct.searchResults(portal_type='Stream', sort_on='created', sort_order='reverse', sort_limit=15)
    streams = []
    for i in results:
        streams.append(SimpleTerm(value=i.getId, title=i.Title.decode('utf-8')))

    return SimpleVocabulary(streams)

alsoProvides(PossibleStreams, IContextSourceBinder)



class IStreamPortlet(IPortletDataProvider):
    """A portlet which renders audio/video online
    """
    header = schema.TextLine(
        title=_(u'Título do Portlet'),
        description=_(u'Título que será exibido no portlet.'),
        required=False,
    )

    option = schema.Choice(
        title=_(u'Opções'),
        description=_(u'Escolha se será um portlet de transmissão de áudio ou vídeo.'),
        required=True,
        source=PossibleOptions,
    )

    stream = schema.Choice(
            title=_(u'Streamings'),
            description=_(u'Escolha o áudio ou vídeo para aparecer no portlet'),
            required=True,
            source=PossibleStreams,
    )

class Assignment(base.Assignment):
    implements(IStreamPortlet)

    header = u''
    option = None
    stream = None

    def __init__(self, header='u', option='audio', stream=None):
        self.header = header
        self.option = option
        self.stream = stream

    @property
    def title(self):
        return _(u'Audio Video Online portlet')


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('stream.pt')

    def stream(self):
        stream = self.data.stream
        ct = api.portal.get_tool(name='portal_catalog')
        result = ct.searchResults(portal_type='Stream', id=stream)
        return [i.link for i in result]

    def option(self):
        opt = self.data.option
        return opt

class AddForm(base.AddForm):
    form_fields = form.Fields(IStreamPortlet)
    label = _(u"Adiciona portlet de Áudio e Vídeo")
    description = _(u"Este portlet mostra players de áudio ou vídeo.")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IStreamPortlet)
    label = _(u"Editar Audio Video Portlet")
    description = _(u"Este portlet mostra palyers de áudio ou vídeo.")
