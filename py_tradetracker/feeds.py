import logging
import requests
import time
import sys, os

from .tradetracker import TradeTracker

        
class Feeds(TradeTracker):
    
    def getFeeds(self, affiliateSiteID, ID=None, campaignID=None, campaignCategoryID=None, assignmentStatus=None):
        try:
            options = {}
            if ID is not None:
                options['ID'] = ID
                
            if campaignID is not None:
                options['campaignID'] = campaignID
                
            if campaignCategoryID is not None:
                options['campaignCategoryID'] = campaignCategoryID
                
            if assignmentStatus is not None:
                options['assignmentStatus'] = assignmentStatus                
#         Mogelijke waardes: notsignedup, pending, accepted, rejected, onhold and signedout.
            
            return self.client.service.getFeeds(affiliateSiteID, options)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 


    def getFeedProductCategories(self, affiliateSiteID, feedId):
        try:
            return self.client.service.getFeedProductCategories(affiliateSiteID, feedId)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 


    def getFeedProducts(self, affiliateSiteID, feedID=None, feedCategoryName=None, campaignID=None,campaignCategoryID=None, query=None, priceFrom=None, priceTo=None,limit=None, offset=None):
        try:
            options = {}
            
            if feedID is not None:
                options['feedID'] = feedID

            if feedCategoryName is not None:
                options['feedCategoryName'] = feedCategoryName   

            if campaignID is not None:
                options['campaignID'] = campaignID   
                
            if campaignCategoryID is not None:
                options['campaignCategoryID'] = campaignCategoryID   
                
            if priceFrom is not None:
                options['priceFrom'] = priceFrom   
                
            if priceTo is not None:
                options['priceTo'] = priceTo   
                
            if limit is not None:
                options['limit'] = limit                   

            if offset is not None:
                options['offset'] = lioffsetmit 

            return self.client.service.getFeedProducts(affiliateSiteID, options)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
        