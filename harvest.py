import requests

API_URL = 'https://api.harvestapp.com/api/v2/%s'
API_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
API_ACCOUNT_ID = 'YOUR_ACCOUNT_ID'

class Harvest(object):
    def __init__(self):
        self.__headers = {
            'Authorization': 'Bearer ' + API_ACCESS_TOKEN,
            'Harvest-Account-ID': API_ACCOUNT_ID,
            'User-Agent': 'MyApp (hoge)'
        }

    def me(self):
        return requests.get(url = API_URL % 'users/me', headers=self.__headers).json()

    def get_user_by(self, user_id):
        path = 'users/%s' % user_id
        return requests.get(url=API_URL % path, headers=self.__headers).json()

    def get_project_assignments_by(self, user_id):
        path = 'users/%s/project_assignments' % user_id
        return requests.get(url=API_URL % path, headers=self.__headers).json()

    def get_task_assignments_by(self, project_id):
        path = 'projects/%s/task_assignments' % project_id
        return requests.get(url = API_URL % path, headers=self.__headers).json()
