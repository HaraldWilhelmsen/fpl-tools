import numpy as np
import pandas as pd
import json
import requests
from pandas.io.json import json_normalize

def get_json():
    r = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    jsonResponse = r.json()
    with open('fpl.json', 'w') as outfile:
        #pass
        json.dump(jsonResponse, outfile)


def read_premierleague_data():
    with open('fpl.json') as json_data:
        d = json.load(json_data)
    print(list(d.keys()))


get_json()
read_premierleague_data()
