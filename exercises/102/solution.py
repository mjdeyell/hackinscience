# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import sys
invar = sys.argv[1]

velib = \
    [{'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE)\
      - 93170 BAGNOLET',
      'zip': '93170-',
      'number': 31705,
      'latitude': 48.8645278209514,
      'city': 'BAGNOLET',
      'name': 'CHAMPEAUX (BAGNOLET)-',
      'longitude': 2.416170724425901
      },
     {'address': "52 RUE D'ENGHIEN / ANGLE RUE DU FAUBOURG POISSONIERE\
      - 75010 PARIS",
      'zip': '75010',
      'number': 10042,
      'latitude': 48.87242006305313,
      'city': 'PARIS-',
      'name': 'ENGHIEN-',
      'longitude': 2.348395236282807
      },
     {'address': '74 BOULEVARD DES BATIGNOLLES - 75008 PARIS-',
      'zip': '75008-',
      'number': 8020,
      'latitude': 48.882148945631904,
      'city': 'PARIS-',
      'name': 'METRO ROME-',
      'longitude': 2.319860054774211
      },
     {'address': '37 RUE CASANOVA - 75001 PARIS-',
      'zip': '75001-',
      'number': 1022,
      'latitude': 48.8682170167744,
      'city': 'PARIS-',
      'name': 'RUE DE LA PAIX-',
      'longitude': 2.330493511399174
      },
     {'address': '139 AVENUE JEAN LOLIVE / MAIL CHARLES DE GAULLE\
      - 93500 PANTIN-',
      'zip': '93500-',
      'number': 35014,
      'latitude': 48.893268664697416,
      'city': 'PANTIN-',
      'name': 'DE GAULLE (PANTIN)-',
      'longitude': 2.412715733388685
      }
     ]

found = 0

for i in range(len(velib)):
    station = dict(velib[i])
    if (station['city'] == invar):
        print(station)
        found = 1

if (found == 0):
    print("Sorry! No station for your city has been found!")
