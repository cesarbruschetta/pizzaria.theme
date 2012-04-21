# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from Products.CMFCore.interfaces import ISiteRoot

from zope.app.component.hooks import getSite

class HomePageView(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('home-page')
    

