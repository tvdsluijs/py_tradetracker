import logging
import requests
import time
import sys, os

from .tradetracker import TradeTracker

        
class Payments(TradeTracker):
    
    def getPayments(self, billDateFrom=None, billDateTo=None):
        try:
            options = {}
            if billDateFrom is not None:
                options['billDateFrom'] = billDateFrom

            if billDateTo is not None:
                options['billDateTo'] = billDateTo
            
            return self.client.service.getPayments(options)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
            
    def getAttributions(self, conversionTransactionID):
        try:
            return self.client.service.getAttributions(conversionTransactionID)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 
            
            
    def getTouchpoints(self,conversionTransactionID):
        try:
            return self.client.service.getTouchpoints(conversionTransactionID)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 