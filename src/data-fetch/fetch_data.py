"""Class used to read data from 'fantasy.premierleague.com', and return or save it """
import json
import requests


class DataFetch:
    def __init__(self) -> None:
        self.web_page = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        self.local_path = 'fpl.json'

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
    a.save_fpl_info()
    b = a.get_saved_fpl_info()
    #print(b)
