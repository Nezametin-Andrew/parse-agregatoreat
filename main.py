import os
import json
import requests
from pprint import pprint

from config import (
    template_link, headers, body, url
)


class GetResponse:
    def __init__(self) -> None:
        self._ = ...


    def request(self, url, header, body) -> dict:
        try:
            r = requests.post(url=url, headers=header, data=json.dumps(body)).json()
            pprint(r)
        except Exception as e:
            ...


a = GetResponse()
a.request(url, headers, body)