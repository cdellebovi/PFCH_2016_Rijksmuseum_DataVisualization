import json

with open('S03_Rijksmuseum_DataVisualization_RijksIDNumbers_DutchArtistVerificationPass1.json', 'r') as json_data_1:

    verification_pass1_data = json.load(json_data_1)
    
    correction_list = []
    
    for old_name in verification_pass1_data:

        correction_dictionary = {}
        
        correction_dictionary['old_name'] = old_name
        correction_dictionary['new_name'] = ''

        correction_list.append(correction_dictionary)

with open('S04_Rijksmuseum_DataVisualization_RijksIDNumbers_DutchArtists_CorrectionPass1A.json', 'w') as outfile:
    json.dump(correction_list, outfile, indent=2)
