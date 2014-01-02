# -*- coding: utf-8 -*-

"""Test Setup of theming.toolkit.javascript"""

# python imports
import unittest2 as unittest

# zope imports
from Products.CMFCore.utils import getToolByName

from theming.toolkit.javascript.testing import TOOLKIT_JAVASCRIPT_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):
    """Setup Test Case for theming.toolkit.javascript."""
    layer = TOOLKIT_JAVASCRIPT_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """Test that the product is installed."""
        self.assertTrue(self.qi_tool.isProductInstalled(
            'theming.toolkit.javascript'))

