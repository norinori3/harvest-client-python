#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from ConfigParser import SafeConfigParser

filename = 'conf.ini'
parser = SafeConfigParser()
parser.read(filename)

API_URL = 'https://api.harvestapp.com/api/v2/%s'
API_ACCESS_TOKEN = parser.get('user', 'api_access_token')
API_ACCOUNT_ID = parser.get('user', 'api_account_id')

class Harvest(object):
    def __init__(self):
        self.__headers = {
            'Authorization': 'Bearer ' + API_ACCESS_TOKEN,
            'Harvest-Account-ID': API_ACCOUNT_ID,
            'User-Agent': 'MyApp (hoge)'
        }

    def __get(self, path):
        return requests.get(url = API_URL % path, headers=self.__headers).json()

    def me(self):
        return self.__get(path = 'users/me')

    def get_user_by(self, user_id):
        path = 'users/%s' % user_id
        return self.__get(path = path)

    def get_project_assignments_by(self, user_id):
        path = 'users/%s/project_assignments' % user_id
        return self.__get(path = path)

    def get_task_assignments_by(self, project_id):
        path = 'projects/%s/task_assignments' % project_id
        return self.__get(path = path)
