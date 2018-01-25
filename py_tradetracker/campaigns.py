import logging
import requests
import time
import sys, os

from .tradetracker import TradeTracker

        
class Campaigns(TradeTracker):
    
    def getCampaigns(self,affiliateSiteID, options):
        try:
            return self.client.service.getCampaigns(affiliateSiteID, options)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
    def getCampaignCategories(self):
        try:
            return self.client.service.getCampaignCategories()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
    def getCampaignCommissionExtended(self):
        try:
            return self.client.service.getCampaignCommissionExtended()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
    def changeCampaignSubscription(self):
        try:
            return self.client.service.changeCampaignSubscription()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
    def getCampaignNewsItems(self):
        try:
            return self.client.service.getCampaignNewsItems()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
