import re
import json
import requests
from pprint import pprint

from config import (
    template_link, headers, body, url
)
from utils import log
from models import Purchase, db


test = {
    'error': True,
    'items': []
}


class Data:
    
    DB = db
    def __init__(self, model: object) -> None:
        self.__model = model

    def __get_id_purchase(self) -> list:
        try:
             return [_id.id for _id in self.__model.select()]
        except Exception as e:
            self.DB.rollback()

    def added_purchase(self, _id: str) -> None:
        try:
            self.__model.create(id=_id)
        except Exception as e:
            self.DB.rollback()

    def __getattribute__(self, name: str) -> Any:
        ...


    def __setattr__(self, name: str, value: str):
        ...


class SortData:

    def __init__(self) -> None:
        self.__id_list = Data().get_id_purchase()

    def sort(self, _id: str) -> bool:
        if _id in self.__id_list: return False
        return True


class Validator:

    def __init__(self) -> None:
        self.error = None

    def __is_error(self, r: dict) -> None:
        try:
            if r['errors'] is not None: raise ResourceWarning(f"Error : {self.response['error']}")
        except (KeyError, ValueError) as e:
            self.error = True
            log(e)
        
    def __is_none_data(self, r: dict) -> None:
        try:
            if not r['items']: raise ValueError("Error data is null")
        except (KeyError, ValueError) as e:
            self.error = True
            log(e)

    def is_valid(self, r: dict) -> None:     
        try:
            self.__is_error(r)
            self.__is_none_data(r)
        except (ValueError, ResourceWarning) as e:
            self.error = True
            log(e)


class ExecuteRequest(Validator):
    
    def __init__(self) -> None:
        super().__init__()
        self.response = None

    def request(self, url: str, header: dict, body: dict) -> None:
        try:
            r = requests.post(url=url, headers=header, data=json.dumps(body)).json()
            self.is_valid(r)
            if self.error is None: self.response = r
        except Exception as e:
            print(e)

    def get_count_items(self) -> int:
        if self.response is None: return 0
        count_items = self.response.get('totalCount', 0)
        return int(count_items)


class ParseData:
    def __init__(self, data: list) -> None:
        self.key_word_for_sort = [
                    "subject", "id", "price", "applicationFillingEndDate",
                    [
                    "deliveryInfos", 0, "deliveryAddress", "formattedFullInfo"
                    ],
                ]
        self.in_data = data
        self.out_data = []
        self.id_list_in_db = []

    def __id_useful(self, title: str) -> bool: 
        pass

    def parse_data(self) -> None:
        for item in self.in_data['items']:
            pass


