from .tradetracker import TradeTracker

import logging
import requests

# from zeep import Client, transports
        
class Affiliates(TradeTracker):

    def getAffiliateSites(self, affiliateSiteCategoryID=None, affiliateSiteTypeID=None,affiliateSiteStatus=None, limit=None, offset=None, sort=None, sortDirection=None, excludeInfo='false'):
        try:
            
            options = {}
            
            return self.client.service.getAffiliateSites(options)
        except Exception as e:
            msg = "def __init__ : " + str(e)
            logging.warning(msg)          
        
        
    def getAffiliateSiteCategories(self):
        try:
            return self.client.service.getAffiliateSiteCategories()
        except Exception as e:
            msg = "def __init__ : " + str(e)
            logging.warning(msg)          


    def getAffiliateSiteTypes(self):
        try:
            return self.client.service.getAffiliateSiteTypes()
        except Exception as e:
            msg = "def __init__ : " + str(e)
            logging.warning(msg)            