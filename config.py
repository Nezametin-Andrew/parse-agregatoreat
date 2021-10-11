template_link = "https://agregatoreat.ru/purchases/announcement/{}/dynamics"
template = "\n\n Наименование : {} \n\n Ссылка : {} \n\n Стартовая цена : {} \n\n Местоположение : {} \n\n Время до окончания : {}\n\n\n"
url = "https://tender-cache-api.agregatoreat.ru/api/TradeLot/list-published-trade-lots"
link_send_msg = 'https://api.telegram.org/bot1695602319:AAEfIJt59_l3Pac5KwearN15nU53svyU71A/sendMessage?chat_id={}&text={}'


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    "content-type": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept": "application/json, text/plain, */*"
}

body = {
    "applicationFillingEndDate": None,
    "applicationFillingStartDate": None,
    "contractPriceEnd": None,
    "contractPriceStart": None,
    "contractSignDateEnd": None,
    "contractSignDateStart": None,
    "createDateTime": None,
    "customerInn": None,
    "customerKpp": None,
    "customerNameOrInn": None,
    "deliveryAddress": None,
    "deliveryAddressRegionCodes": [],
    "deliveryDateEnd": None,
    "deliveryDateStart": None,
    "excludeCancelledByCustomer": False,
    "isChangeDealTermsProtocolReceived": False,
    "isCustomerSigningAwaiting": False,
    "isReviewAwaiting": False,
    "isSmpOnly": False,
    "isSupplierSigningAwaiting": False,
    "ktruCodes": [],
    "lotItemEatCodes": [],
    "lotStates": [2],
    "number": None,
    "okpd2Codes": [],
    "page": 1,
    "priceEnd": None,
    "priceStart": None,
    "productCode": None,
    "purchaseMethods":[1],
    "purchaseName": "",
    "purchaseTypeIds": [],
    "searchText": None,
    "size": 2,
    "sort": [{'fieldName': "applicationFillingEndDate", 'direction': 2}],
    "stateDefenseOrderOnly": False,
    "supplierNameOrInn": None,
    "types": []
}


