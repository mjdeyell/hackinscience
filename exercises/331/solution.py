# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import json


def load_json(path):
    with open(path) as jayson:
        out = json.load(jayson)
    return out

Dirty = load_json("velib.json")

for k in range(len(Dirty)):
    address = Dirty[k]['address'].split(' - ')
    if (len(address) == 2):
        city = address[1].split()
        Dirty[k]['zip_code'] = city[0]
        Dirty[k]['city'] = city[1]
        Dirty[k]['address'] = address[0]
    elif (len(address) == 3):
        city = address[2].split()
        Dirty[k]['zip_code'] = city[0]
        Dirty[k]['city'] = city[1]
        Dirty[k]['address'] = address[0] + ' - ' + address[1]
    else:
        try:
            address = Dirty[k]['address'].split('- ')
            city = address[1].split()
            Dirty[k]['zip_code'] = city[0]
            Dirty[k]['city'] = city[1]
            Dirty[k]['address'] = address[0]
        except Exception:
            address = Dirty[k]['address'].split()
            Dirty[k]['zip_code'] = address[len(address)-2]
            Dirty[k]['city'] = address[len(address)-1]
            del address[len(address)-2]
            del address[len(address)-1]
            new_address = ' '.join(address)
            Dirty[k]['address'] = new_address
    station = Dirty[k]['name'].split(' - ')
    Dirty[k]['name'] = station[1]

with open('solution.json', 'w') as outfile:
    json.dump(Dirty, outfile)
