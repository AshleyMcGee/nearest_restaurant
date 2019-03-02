import csv
import requests
from config import gkey
import numpy as np


def find_food(foodType):

    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    
    params = {
        "location": "43.6187102, -116.2146068",
        "nearby": "distance",
        "type": "restaurant",
        "key": gkey,
        "keyword": foodType
    }

    my_json = requests.get(url=base_url, params=params).json()

    return my_json

    try:        
        name = my_json[0]['name']
        address = my_json[0]['vicinity']
        price_level = my_json[0]['price_level']
        rating = my_json[0]['rating']
        
        return {
            'ethnicity': foodType,
            'name': name,
            'address': address,
            'price_level': price_level,
            'rating': rating
            }
        
    except (KeyError, IndexError):
        print("For foodType, {foodType}. Missing field/result... skipping.".format(restr_type=restr_type))
        
        return {
            'ethnicity': foodType,
            'name': np.nan,
            'address': np.nan,
            'price_level': np.nan,
            'rating': np.nan
            }

    result = []
    
    with open('ethnic_resr.csv', 'r') as in_file:
        in_file.readline()
        for line in in_file:
            foodType = line.strip()
            result.append(foodType)

    
