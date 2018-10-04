# -*- coding: utf-8 -*-

from five import grok
from interlegis.portalmodelo.theme.interfaces import IStream
from plone.dexterity.content import Item


class Stream(Item):
    """A stream (audio and video)."""
    grok.implements(IStream)
