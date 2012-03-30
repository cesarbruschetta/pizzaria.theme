# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
#from plone.app.layout.viewlets.interfaces import IAboveContent
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.app.component.hooks import getSite

#from Products.CMFCore.utils import getToolByName


grok.context(Interface) 

# Viewlet for portal logo top
class ListProdViewlet(grok.Viewlet): 
    grok.name('pizzaria.content.listProd') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader) 
    
    
    def getProdutos(self):
               
        ctool = getSite().portal_catalog
        produtos = ctool(portal_type='pizzaria.content.produto',
                         path={'query': '/', 'depth' : 99},
                         sort_on='getObjPositionInParent')
        
        if produtos:
            return produtos
        else:
            return [] 