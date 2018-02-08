# PY NS API

[![N|Solid](https://www.ns.nl/static/generic/2.19.0/images/nslogo.svg)](https://www.ns.nl/reisinformatie/ns-api)

## What is this repository for?

* This python3 module is for easy usage of the the NS Train API

## How do I get set up?

* Go To [Tradetracker WSDL SIte](https://affiliate.tradetracker.com/webService)
* On the right side you will find your Klant-ID and Toegangssleutel (client ID and access key)
* You will need these two keys (id and key)
* Install this script with:
    * pip3 py_tradetracker --upgrade (or pip py_nsapi --upgrade )
    * or
    * sudo -H pip3 py_tradetracker --upgrade
* ready to use it!

## Repository & Pypi
You can find the Repro at [Bitbucket](https://bitbucket.org/tvdsluijs/py-tradetracker/)

and the install information on [Pypi](https://pypi.python.org/pypi/py-tradetracker)


## API's
The API's return the data in a Dictionary. You can loop through the Dict as any Dict.
'''
from py_tradetracker import

clientid = [your client ID]
secretkey = [your secret key]
sandbox = "true"
locale = "nl_NL"
demo = "false"
See
'''
examples about how to get information.

All api's can write warnings, errors and debug information to log files

Just use

```python3
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
```

More information about [logging](https://docs.python.org/3/howto/logging.html)

'''
from py_tradetracker import

clientid = [your client ID]
secretkey = [your secret key]
sandbox = "true"
locale = "nl_NL"
demo = "false"

'''

###Affiliates
getAffiliateSites
getAffiliateSiteTypes
getAffiliateSiteCategories








# a = Affiliates(None, clientid, secretkey, sandbox, locale, demo)
# data = a.getAffiliateSites()
# data = a.getAffiliateSiteCategories()
# data = a.getAffiliateSiteTypes()


# c = Campaigns(None, clientid, secretkey, sandbox, locale, demo)
# data = c.getCampaigns(affiliateSiteID, options)
# data = c.getCampaignCategories()
# data = c.getCampaignCommissionExtended
# data = c.changeCampaignSubscription
# data = c.getCampaignNewsItems

# m = Material(None, clientid, secretkey, sandbox, locale, demo)
# data = m.getMaterialBannerDimensions
# data = m.getMaterialBannerImageItems
# data = m.getMaterialBannerFlashItems
# data = m.getMaterialTextItems
# data = m.getMaterialHTMLItems
# data = m.getMaterialIncentiveVoucherItems
# data = m.getMaterialIncentiveOfferItems

# t = Transactions(None, clientid, secretkey, sandbox, locale, demo)
# data = t.getClickTransactions
# data = t.getConversionTransactions
# data = t.createConversionTransaction

# r = Report(None, clientid, secretkey, sandbox, locale, demo)
# data = r.getReportAffiliateSite
# data = r.getReportCampaign
# data = r.getReportReference

# f = Feeds(None, clientid, secretkey, sandbox, locale, demo)
# data = f.getFeeds(affiliateSiteID, options)
# data = f.getFeedProductCategories(affiliateSiteID, feedId)
# data = f.getFeedProducts(affiliateSiteID, options)

# o = Other(None, clientid, secretkey, sandbox, locale, demo)
# data = o.getPayments
# data = o.getAttributions
# data = o.getTouchpoints




###Campaigns
getCampaigns
getCampaignCategories
getCampaignCommissionExtended
changeCampaignSubscription
getCampaignNewsItems

###Material
getMaterialBannerDimensions
getMaterialBannerImageItems
getMaterialBannerFlashItems
getMaterialTextItems
getMaterialHTMLItems
getMaterialIncentiveVoucherItems
getMaterialIncentiveOfferItems

###Transactions
getClickTransactions
getConversionTransactions
createConversionTransaction

###Report
getReportAffiliateSite
getReportCampaign
getReportReference

###ProductsFromFeed
getFeeds
getFeedProductCategories
getFeedProducts

###Payments
getPayments
getAttributions
getTouchpoints

### 


#### Fields


#### Example code




## Who do I talk to?

* Theodorus van der Sluijs (friends call me Theo)
* theodorus@vandersluijs.nl

## License
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

### You are free to:

* Share — copy and redistribute the material in any medium or format
* Adapt — remix, transform, and build upon the material

-The licensor cannot revoke these freedoms as long as you follow the license terms.-

### Under the following terms:

* Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial — You may not use the material for commercial purposes.
* ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.