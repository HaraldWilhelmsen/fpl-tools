"""Class used to read data from 'fantasy.premierleague.com', and return or save it """
import __main__
import json
import requests
import os


class DataFetch:
    def __init__(self) -> None:
        self.web_page = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        self.local_path = 'fpl.json'

        self.investigate_path()

    def investigate_path(self):
        main_file = __main__.__file__

        if main_file == 'fetch_data.py':
            self.global_path = self.local_path
        
        elif main_file == 'main.py':
            self.global_path = 'data-fetch/' + self.local_path

        else:
            print('cannot determine path')
            exit(1)

    def save_fpl_info(self) -> None:
        r = requests.get(self.web_page)
        jsonResponse = r.json()
        with open(self.local_path, 'w') as outfile:
            json.dump(jsonResponse, outfile)
        
    def get_saved_fpl_info(self) -> dict:
        with open(self.local_path) as json_data:
            fpl_data = json.load(json_data)
        print(type(fpl_data))
        return fpl_data
    
    def get_current_fpl_info(self) -> dict:
        r = requests.get(self.web_page)
        jsonResponse = r.json()
        return jsonResponse


if __name__ == '__main__':
    a = DataFetch()
    #a.save_fpl_info()
    #b = a.get_saved_fpl_info()
    #print(b)
