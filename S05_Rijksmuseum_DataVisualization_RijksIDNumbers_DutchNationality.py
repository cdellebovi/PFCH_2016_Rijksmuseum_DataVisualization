import json

with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists1PT.json', 'r') as json_data_1:
    with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists1NT.json', 'r') as json_data_2:
        with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists2PT.json', 'r') as json_data_3:
            with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists2NT.json', 'r') as json_data_4:
                with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists3PT.json', 'r') as json_data_5:
                    with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists3NTTEST.json', 'r') as json_data_6:

                        with open('S04_Rijksmuseum_DataVisualization_RijksIDNumbers_DutchArtists_CorrectionPass1B.json', 'r') as json_data_7:

                            getty_ulan_dutch_artists1_PT = json.load(json_data_1)
                            getty_ulan_dutch_artists1_NT = json.load(json_data_2)
                            getty_ulan_dutch_artists2_PT = json.load(json_data_3)
                            getty_ulan_dutch_artists2_NT = json.load(json_data_4)
                            getty_ulan_dutch_artists3_PT = json.load(json_data_5)
                            getty_ulan_dutch_artists3_NT = json.load(json_data_6)

                            dutch_rijksmuseum_artists = json.load(json_data_7)
                            
                            getty_ulan_dutch_artists_list = []
                            dutch_artist_id_number_list = []

                            for x in getty_ulan_dutch_artists1_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        getty_ulan_dutch_artists_list.append(y['preferred_term_text'])
                            for x in getty_ulan_dutch_artists1_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        getty_ulan_dutch_artists_list.append(y['non_preferred_term_text'])
                            for x in getty_ulan_dutch_artists2_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        getty_ulan_dutch_artists_list.append(y['preferred_term_text'])
                            for x in getty_ulan_dutch_artists2_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        getty_ulan_dutch_artists_list.append(y['non_preferred_term_text'])
                            for x in getty_ulan_dutch_artists3_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        getty_ulan_dutch_artists_list.append(y['preferred_term_text'])
                            for x in getty_ulan_dutch_artists3_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        getty_ulan_dutch_artists_list.append(y['non_preferred_term_text'])

                            for x in getty_ulan_dutch_artists_list:
                                for y in dutch_rijksmuseum_artists:
                                    if (x).upper() == (y['principalOrFirstMaker']).upper(): 
                                        dutch_artist_id_number_list.append(y['objectNumber'])

sorted_dutch_artist_id_number_list = sorted(set(dutch_artist_id_number_list))

with open('S05_Rijksmuseum_DataVisualization_RijksIDNumbers_DutchNationality.json', 'w') as outfile:
    json.dump(sorted_dutch_artist_id_number_list, outfile, indent=2)
