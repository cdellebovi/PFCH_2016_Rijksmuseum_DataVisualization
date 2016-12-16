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

                            gu_list1_PT = []
                            gu_list1_NT = []
                            gu_list2_PT = []
                            gu_list2_NT = []
                            gu_list3_PT = []
                            gu_list3_NT = []

                            for x in getty_ulan_dutch_artists1_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        gu_dict1_PT = {}
                                        gu_dict1_PT['ULAN_Term']=(y['preferred_term_text'])
                                        gu_dict1_PT['Subject_ID']=(x['Subject_ID'])
                                        gu_list1_PT.append(gu_dict1_PT)

                            for x in getty_ulan_dutch_artists1_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        gu_dict1_NT = {}
                                        gu_dict1_NT['ULAN_Term']=(y['non_preferred_term_text'])
                                        gu_dict1_NT['Subject_ID']=(x['Subject_ID'])
                                        gu_list1_NT.append(gu_dict1_NT)

                            for x in getty_ulan_dutch_artists2_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        gu_dict2_PT = {}
                                        gu_dict2_PT['ULAN_Term']=(y['preferred_term_text'])
                                        gu_dict2_PT['Subject_ID']=(x['Subject_ID'])
                                        gu_list2_PT.append(gu_dict2_PT)

                            for x in getty_ulan_dutch_artists2_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        gu_dict2_NT = {}
                                        gu_dict2_NT['ULAN_Term']=(y['non_preferred_term_text'])
                                        gu_dict2_NT['Subject_ID']=(x['Subject_ID'])
                                        gu_list2_NT.append(gu_dict2_NT)

                            for x in getty_ulan_dutch_artists3_PT:
                                if 'preferred terms' in x:
                                    for y in (x['preferred terms']):
                                        gu_dict3_PT = {}
                                        gu_dict3_PT['ULAN_Term']=(y['preferred_term_text'])
                                        gu_dict3_PT['Subject_ID']=(x['Subject_ID'])
                                        gu_list3_PT.append(gu_dict3_PT)

                            for x in getty_ulan_dutch_artists3_NT:
                                if 'non_preferred terms' in x:
                                    for y in (x['non_preferred terms']):
                                        gu_dict3_NT = {}
                                        gu_dict3_NT['ULAN_Term']=(y['non_preferred_term_text'])
                                        gu_dict3_NT['Subject_ID']=(x['Subject_ID'])
                                        gu_list3_NT.append(gu_dict3_NT)

with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists_SubjectIDs.json', 'w') as outfile:
    json.dump(gu_list1_NT, outfile, indent=2)
