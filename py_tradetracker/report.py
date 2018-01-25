import logging
import requests
import time
import sys, os

from .tradetracker import TradeTracker

        
class Report(TradeTracker):
    
    def getReportAffiliateSite(self, affiliateSiteID=None, dateFrom=None, dateTo=None):
        try:
            options = {}
            if dateFrom is not None:
                options['dateFrom'] = dateFrom
            if dateTo is not None:
                options['dateTo'] = dateTo                
            
            
            return self.client.service.getReportAffiliateSite(affiliateSiteID, options)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
    def getReportCampaign(self, affiliateSiteID=None, campaignID=None, dateFrom=None, dateTo=None):
        try:
            options = {}
            if campaignID is not None:
                options['campaignID'] = campaignID
            if dateFrom is not None:
                options['dateFrom'] = dateFrom
            if dateTo is not None:
                options['dateTo'] = dateTo                
            
            return self.client.service.getReportCampaign(affiliateSiteID, options)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
    def getReportReference(self, affiliateSiteID=None, reference=None, campaignID=None, dateFrom=None, dateTo=None):
        try:
            options = {}
            if reference is not None:
                options['reference'] = reference
            if campaignID is not None:
                options['campaignID'] = campaignID
            if dateFrom is not None:
                options['dateFrom'] = dateFrom
            if dateTo is not None:
                options['dateTo'] = dateTo 
            
            return self.client.service.getReportReference(affiliateSiteID, options)
            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 