# -*- coding:utf-8 -*-
from plone.app.upgrade.utils import loadMigrationProfile

import logging

PROJECTNAME = 'interlegis.portalmodelo.theme'


def apply_profile(context):
    """Atualiza perfil para versao 2."""
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-interlegis.portalmodelo.theme.upgrades.v2:default'
    loadMigrationProfile(context, profile)
    logger.info('Atualizado para versao 2')
