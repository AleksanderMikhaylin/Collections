import json
import time

import requests
from tqdm import tqdm
from datetime import datetime


def create_folder(access_token_YD, folder_name):
    params = {
        'path': folder_name
    }

    yd = YD(access_token_YD)

    response = requests.put(yd.base_url + '/v1/disk/resources', headers=yd.headers, params=params)
    return response.status_code


def check_folder(access_token_YD, folder_name):
    params = {
        'path': folder_name
    }

    yd = YD(access_token_YD)

    response = requests.get(yd.base_url + '/v1/disk/resources/', headers=yd.headers, params=params)
    return response.status_code

class YD:

    def __init__(self, access_token):
        self.base_url = 'https://cloud-api.yandex.net'
        self.headers = {
            'Authorization': access_token
        }

if __name__ == '__main__':

    access_token_YD = '???'

    status_code = create_folder(access_token_YD, 'test_folder')
    print(status_code)
    status_code = check_folder(access_token_YD, 'test_folder')
    print(status_code)



