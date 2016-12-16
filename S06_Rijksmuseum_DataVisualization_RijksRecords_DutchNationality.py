import requests, json

with open('S05_Rijksmuseum_DataVisualization_RijksIDNumbers_DutchNationality.json', 'r') as json_data_1:
   with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists_SubjectIDs.json', 'r') as json_data_2:

    dutch_artist_idnumbers = json.load(json_data_1)
    ulan_terms = json.load(json_data_2)

complete_record_list = []
json_item = 0

while json_item <= 420:

    payload = {'format':'json', 'key':'YOUR_KEY_HERE'}
    r = requests.get('https://www.rijksmuseum.nl/api/en/collection/' + str(dutch_artist_idnumbers[json_item]), params=payload)

    data = json.loads(r.text)

    complete_artwork_record = {}

    for x in data:
        try: complete_artwork_record['principalOrFirstMaker']=(data['artObject']['principalOrFirstMaker'])
        except TypeError: pass
        except IndexError: pass        
        try: complete_artwork_record['title']=(data['artObject']['title'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['dateOfProduction']=(data['artObject']['dating']['year'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['physicalMedium']=(data['artObject']['physicalMedium'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['dimensions0Value']=(data['artObject']['dimensions'][0]['value'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['dimensions0Unit']=(data['artObject']['dimensions'][0]['unit'])        
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['dimensions0Type']=(data['artObject']['dimensions'][0]['type'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['dimensions1Value']=(data['artObject']['dimensions'][1]['value'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['dimensions1Unit']=(data['artObject']['dimensions'][1]['unit'])        
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['dimensions1Type']=(data['artObject']['dimensions'][1]['type'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['acquisitionDate']=(data['artObject']['acquisition']['date'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['objectNumber']=(data['artObject']['objectNumber'])
        except TypeError: pass
        except IndexError: pass
        try: complete_artwork_record['webImage']=(data['artObject']['webImage']['url'])
        except TypeError: pass
        except IndexError: pass

    complete_record_list.append(complete_artwork_record)

    json_item = json_item + 1

with open('S06_Rijksmuseum_DataVisualization_RijksRecords_DutchNationality.json', 'w') as outfile:
    json.dump(complete_record_list, outfile, indent=2)

