import requests, json

id_number_list = []
page = 1

while page <= 2217:

    payload = {'type':'painting', 'f.dating.period': 17, 'p': page, 'ps': 1, 'format':'json', 'key':'uoXe9R9Y'}
    r = requests.get('https://www.rijksmuseum.nl/api/en/collection/', params=payload)

    data = json.loads(r.text)

    id_artist_coupling = {}
    
    for x in (data['artObjects']):
        id_artist_coupling['objectNumber']=x['objectNumber']
        id_artist_coupling['principalOrFirstMaker']=x['principalOrFirstMaker']   

    id_number_list.append(id_artist_coupling)
    
    page = page + 1

with open('S01_Rijksmuseum_DataVisualization_RijksIDNumbers.json', 'w') as outfile:
    json.dump(id_number_list, outfile, indent=2)
