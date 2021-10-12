from logging import Manager
import re
import json
import requests
from pprint import pprint

from config import (
    template_link, headers, body, url
)
from utils import log
from models import Purchase, KeyWord, db


test = {
    'error': True,
    'items': []
}


class DataManager:
    
    DB = db
    def __init__(self, model: object) -> None:
        self.__model = model

    def __get_id_purchase(self) -> list:
        try:
             return [_id.id for _id in self.__model.select()]
        except Exception as e:
            self.DB.rollback()
            return []

    def added_purchase(self, _id: str) -> None:
        try:
            self._model.create(id=_id)
        except Exception as e:
            self.DB.rollback()

    def __get_key_word(self) -> list:
        try:
            return [_w.word for _w in self.__model]
        except Exception as e:
            self.DB.rollback()
            return []

    def getattr(self):
        if isinstance(self.__model, Purchase): 
            return self.__get_id_purchase()


class SortData:

    def __init__(self) -> None:
        self.manager_data = DataManager(Purchase())
        self.__id_list = self.manager_data.getattr()

    def sort_id(self, _id: str) -> bool:
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


class Request(Validator):
    
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
        self.incoming_data = data
        self.output_data = []
        self.id_for_db = []
        self.sort = SortData()

    def __id_useful(self, title: str) -> bool: 
        ...

    def parse_data(self) -> None:
        for item in self.in_data['items']:
            if self.__id_useful(item['subject']):
                ...

            if self.sort.sort_id(item['id']):
                self.id_for_db.append(item['id'])


