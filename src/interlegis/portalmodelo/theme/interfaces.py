# -*- coding: utf-8 -*-
from interlegis.portalmodelo.theme import _
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides
from zope.interface import Interface
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class IBrowserLayer(Interface):
    """Marker interface that defines a Zope browser layer.
    """

def PossibleOptions(context):
    values = [(SimpleTerm(value='audio1', title=_(u'Áudio'))), (SimpleTerm(value='audio2', title=_(u'Áudio HLS'))), (SimpleTerm(value='video', title=_(u'Vídeo')))]

    return SimpleVocabulary(values)

alsoProvides(PossibleOptions, IContextSourceBinder)

class IStream(model.Schema):
    """Define a stream record."""

    title = schema.TextLine(
        title=_(u'Título'),
        description=_(u''),
        required=True,
    )

    description = schema.Text(
        title=_(u'Descrição'),
        description=_(u''),
        required=False,
    )

    link = schema.TextLine(
        title=_(u'Link'),
        required=True,
    )

    option = schema.Choice(
        title=_(u'Opções'),
        description=_(u'Escolha se será uma transmissão de áudio ou de vídeo.\n A opção Áudio representa um player de transmissão do tipo .mp3, .aac ou .ogg. A opção Áudio HLS representa um player de transmissão do tipo .m3u8. A opção Vídeo representa um player de transmissão do tipo .m3u8'),
        required=True,
        source=PossibleOptions,
    )
