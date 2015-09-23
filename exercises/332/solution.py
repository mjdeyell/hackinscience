# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import json
import folium


def load_json(path):
    with open(path) as jayson:
        out = json.load(jayson)
    return out

Velib = load_json("solution.json")

map_osm = folium.Map(location=[48.8530, 2.3498])


for i in range(len(Velib)):
    L1 = Velib[i]['latitude']
    L2 = Velib[i]['longitude']
    title_text = Velib[i]['name']
    map_osm.simple_marker(location=[L1, L2], popup=title_text)

map_osm.create_map(path='velib.html')
