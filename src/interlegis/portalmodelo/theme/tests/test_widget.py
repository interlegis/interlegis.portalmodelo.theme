# -*- coding: utf-8 -*-

from interlegis.portalmodelo.theme.browser.imagewidget import ImageWidget
from interlegis.portalmodelo.theme.testing import INTEGRATION_TESTING
from zope.schema import Bytes
from zope.publisher.browser import TestRequest

import unittest

PROJECTNAME = 'interlegis.portalmodelo.theme'
RENDERED = u'\n  <input type="hidden" value="" name="field.foo.used" id="field.foo.used" />\n  \
<div style="padding-top: 1em;">\n    <input type="radio" value="nochange" checked="checked" \
class="noborder" name="field.foo.action" onclick="document.getElementById(\'field.foo\').disabled=true" \
id="field.foo.nochange" />\n    <label for="field.foo.nochange">Keep existing image</label>\n    \
<br />\n    <input type="radio" value="remove" class="noborder" name="field.foo.action" \
onclick="document.getElementById(\'field.foo\').disabled=true" id="field.foo.delete" />   \n    \
<label for="field.foo.replace">Remove existing image</label>\n    <br />\n    \
<input type="radio" value="replace" class="noborder" name="field.foo.action" \
onclick="document.getElementById(\'field.foo\').disabled=false" id="field.foo.replace" />   \n    \
<label for="field.foo.replace">Replace with new image</label>\n  </div>\n  \
<div style="padding-left: 1.5em; padding-top: 0.5em;">\n    \
<input type="file" maxlength="True" class="" size="30" name="field.foo" id="field.foo" />\n    \
<script type="text/javascript">document.getElementById(\'field.foo\').disabled=true;</script>\n  </div>\n\n'


class ImageWidgetTestCase(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_widget(self):
        field = Bytes(__name__='foo',
                      missing_value=None,
                      required=False)
        request = TestRequest(form={'field.foo': u''})
        widget = ImageWidget(field, request)

        self.assertTrue(widget.getInputValue() is None)

        request = TestRequest(form={'field.foo': u'', 'field.foo.action': u'remove'})
        widget = ImageWidget(field, request)

        self.assertTrue(widget.getInputValue() == 'remove')
        self.assertTrue(widget() == RENDERED)
