import json

with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists1PT.json', 'r') as json_data_1:
    with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists1NT.json', 'r') as json_data_2:
        with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists2PT.json', 'r') as json_data_3:
            with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists2NT.json', 'r') as json_data_4:
                with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists3PT.json', 'r') as json_data_5:
                    with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists3NTTEST.json', 'r') as json_data_6:

                        with open('S01_Rijksmuseum_DataVisualization_RijksIDNumbers.json', 'r') as json_data_7:
                        
                            getty_ulan_dutch_artists1_PT = json.load(json_data_1)
                            getty_ulan_dutch_artists1_NT = json.load(json_data_2)
                            getty_ulan_dutch_artists2_PT = json.load(json_data_3)
                            getty_ulan_dutch_artists2_NT = json.load(json_data_4)
                            getty_ulan_dutch_artists3_PT = json.load(json_data_5)
                            getty_ulan_dutch_artists3_NT = json.load(json_data_6)
                            rijksmuseum_artists = json.load(json_data_7)

                            gu_list1_PT = []
                            gu_list1_NT = []
                            gu_list2_PT = []
                            gu_list2_NT = []
                            gu_list3_PT = []
                            gu_list3_NT = []
                            rm_list = []
                            not_in_rm_list = []

                            for x in rijksmuseum_artists:
                                rm_list.append(x['principalOrFirstMaker'])

                            for x in getty_ulan_dutch_artists1_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        gu_list1_PT.append(y['preferred_term_text'])

                            for x in getty_ulan_dutch_artists1_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        gu_list1_NT.append(y['non_preferred_term_text'])

                            for x in getty_ulan_dutch_artists2_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        gu_list2_PT.append(y['preferred_term_text'])

                            for x in getty_ulan_dutch_artists2_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        gu_list2_NT.append(y['non_preferred_term_text'])

                            for x in getty_ulan_dutch_artists3_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        gu_list3_PT.append(y['preferred_term_text'])

                            for x in getty_ulan_dutch_artists3_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        gu_list3_NT.append(y['non_preferred_term_text'])

                            for x in rm_list:
                                if x not in gu_list1_PT:
                                    if x not in gu_list1_NT:
                                        if x not in gu_list2_PT:
                                            if x not in gu_list2_NT:
                                                if x not in gu_list3_PT:
                                                    if x not in gu_list3_NT:
                                            
                                                        not_in_rm_list.append(x)
                                    
sorted_not_in_rm_list = sorted(set(not_in_rm_list))

with open('S03_Rijksmuseum_DataVisualization_IDNumbers_DutchArtists_VerificationPass1.json', 'w') as outfile:
    json.dump(sorted_not_in_rm_list, outfile, indent=2)
