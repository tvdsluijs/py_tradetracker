import requests
import logging
import json
import xmltodict

from urllib.parse import urlparse, parse_qs, parse_qsl

class ProductsFromFeed:
    def __init__(self):
        try:
            # not using yet!
            self.data = ""
        
        except Exception as e:
            msg = "def __init__ : " + str(e)
            logging.warning(msg)   

    def get_url(self, url=None):
        """
        Function to get the url and get the content
        returns decoded utf8 content
        """
        try:
            if url is None:
                raise Exception("No Url")
            
            r = requests.get(url)
            r.encoding = 'utf-8'
            if r.status_code > 200:
                raise Exception("Url " + url + "problem : " + str(r.status_code))
            
            return r.text
        
        except Exception as e:
            msg = "def get_url : " + str(e)
            logging.warning(msg)
            
    
    def getProducts(self,url=None):
        try:
            if url is None:
                raise Exception('No URL')
        
            data = self.get_url(url)
            if data is None:
                raise Exception("No Data")        
        
            # get the type from the url!
            o = urlparse(url)
            query = dict(parse_qsl(o.query))
            utype = query['type']


            if utype == "xml" or utype == "xml-v2":
                data = xmltodict.parse(data, attr_prefix='', cdata_key='text', dict_constructor=dict)
                return data['products']['product']
            elif utype == "json":
                data = json.loads(data)
                return data['products']
            elif utype == "csv":
                print ('Are you nuts? Try using XML or JSON in your feed!')
                raise Exception('Cannot use CSV!')
            elif utype == "rss":
                print ('Are you crazy? Try using XML or JSON in your feed!')
                raise Exception('Cannot use RSS!')
            else:
                raise Exception('What type do you want? I dunno!')

        except Exception as e:
            msg = "def getProducts : " + str(e)
            logging.warning(msg)  