# -*- coding: utf-8 -*-

"""Test Layer theming.toolkit.javascript"""

# zope imports
from plone.app.testing import (
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)

from zope.configuration import xmlconfig


class ToolkitJavascript(PloneSandboxLayer):
    """Custom Test Layer for theming.toolkit.javascript"""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package       
        import theming.toolkit.javascript 
        xmlconfig.file('configure.zcml',
                       theming.toolkit.javascript,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'theming.toolkit.javascript:default')
        

TOOLKIT_JAVASCRIPT_FIXTURE = ToolkitJavascript()
TOOLKIT_JAVASCRIPT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TOOLKIT_JAVASCRIPT_FIXTURE, ),
    name="ToolkitJavascript:Integration")
