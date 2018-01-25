import logging
import requests
import time
import sys, os

from zeep import Client, transports

class TradeTracker:
    def __init__(self, instance=None, clientid=None, secretkey=None, sandbox="false", locale="nl_NL", demo="false"):
        try:
            if clientid is None:
                raise Exception("No client id provided")
                
            self.clientid = clientid
            
            if secretkey is None:
                raise Exception("No secret key provided")
            
            self.secretkey = secretkey

            self.sandbox = sandbox
            self.locale = locale
            self.demo = demo

            self.instance = instance
            self.session = requests.Session()
            self.transport = transports.Transport(session=self.session)

            wsdl_url = 'http://ws.tradetracker.com/soap/affiliate?wsdl'
        
            self.client = Client(wsdl_url, transport=self.transport)
            self.client.service.authenticate(self.clientid, self.secretkey, self.sandbox, self.locale, self.demo);

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) + " | " + str(fname) + " | " + str(exc_tb.tb_lineno)) 