import json

with open('S04_Rijksmuseum_DataVisualization_RijksIDNumbers_DutchArtists_CorrectionPass1A_Corrected.json', 'r') as json_data_1:
    with open('S01_Rijksmuseum_DataVisualization_RijksIDNumbers.json', 'r') as json_data_2:

        corrected_pass_data = json.load(json_data_1)
        rijksmuseum_artists = json.load(json_data_2)

        corrected_idnumber_list = []

        for x in rijksmuseum_artists:
            for y in corrected_pass_data:
                if (x['principalOrFirstMaker']) == (y['old_name']):

                    edited_artwork_record = {}

                    edited_artwork_record['principalOrFirstMaker']=(y['new_name'])
                    edited_artwork_record['objectNumber']=(x['objectNumber'])

                    corrected_idnumber_list.append(edited_artwork_record)

                    if (x['principalOrFirstMaker']) != (y['old_name']):

                        unedited_artwork_record = {}

                        unedited_artwork_record['principalOrFirstMaker']=(x['principalOrFirstMaker'])
                        unedited_artwork_record['objectNumber']=(x['objectNumber'])
                                    
                        corrected_idnumber_list.append(unedited_artwork_record)

final_corrected_idnumber_list = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in corrected_idnumber_list)]

with open('S04_Rijksmuseum_DataVisualization_RijksIDNumbers_DutchArtists_CorrectionPass1B.json', 'w') as outfile:
    json.dump(final_corrected_idnumber_list, outfile, indent=2)
