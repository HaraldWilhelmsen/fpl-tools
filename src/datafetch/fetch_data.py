"""Class used to read data from 'fantasy.premierleague.com', and return or save it """
import json
import requests
import os


class DataFetch:
    def __init__(self) -> None:
        self.web_page = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        self.web_page_fixtures = 'https://fantasy.premierleague.com/api/fixtures/'
        self.local_path = 'fpl.json'
        self.global_path = ''
        self.investigate_path()

    def investigate_path(self):
        path = os.path.dirname(os.path.abspath(__file__))
        
        if not path.split('/')[-1] == "datafetch":
            print('cannot determine path')
            exit(1)
        
        self.global_path = path + '/' + self.local_path

    def save_fpl_info(self) -> None:
        r = requests.get(self.web_page)
        jsonResponse = r.json()
        with open(self.global_path, 'w') as outfile:
            json.dump(jsonResponse, outfile)
        
    def get_saved_fpl_info(self) -> dict:
        with open(self.global_path) as json_data:
            fpl_data = json.load(json_data)
        return fpl_data
    
    def get_current_fpl_info(self) -> dict:
        r = requests.get(self.web_page)
        jsonResponse = r.json()
        return jsonResponse

    def get_current_fixtures(self) -> dict:
        r = requests.get(self.web_page_fixtures)
        jsonResponse = r.json()
        return jsonResponse


if __name__ == '__main__':
    a = DataFetch()
    a.save_fpl_info()
    b = a.get_saved_fpl_info()
    print(b)
