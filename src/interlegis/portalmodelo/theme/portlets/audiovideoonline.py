# -*- coding: utf-8 -*-

from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.portlets import base
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

class IAudioVideoPortlet(IPortletDataProvider):
    """A portlet which renders audio/video online
    """
    header = schema.TextLine(
        title=_(u'Título do Portlet'),
        description=_(u'Título que será exibido no portlet.'),
        required=False,
    )

    link = schema.TextLine(
        title=_(u'Link'),
        description=_(u'URL da transmissão.'),
        required=True,
    )

    option = schema.Choice(
        title=_(u'Opções'),
        description=_(u'Escolha se será um portlet de transmissão de áudio ou vídeo.'),
        required=True,
        source=PossibleOptions,
    )

class Assignment(base.Assignment):
    implements(IAudioVideoPortlet)

    header = u''
    link = u''
    option = None

    def __init__(self, header='u', link='u', option='audio'):
        self.header = header
        self.link = link
        self.option = option

    @property
    def title(self):
        return _(u'Audio Video Online portlet')


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('audiovideoonline.pt')

    def link(self):
        link = self.data.link
        return link

    def option(self):
        opt = self.data.option
        return opt

class AddForm(base.AddForm):
    form_fields = form.Fields(IAudioVideoPortlet)
    label = _(u"Adiciona portlet de Áudio e Vídeo")
    description = _(u"Este portlet mostra players de áudio ou vídeo.")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IAudioVideoPortlet)
    label = _(u"Editar Audio Video Portlet")
    description = _(u"Este portlet mostra palyers de áudio ou vídeo.")
