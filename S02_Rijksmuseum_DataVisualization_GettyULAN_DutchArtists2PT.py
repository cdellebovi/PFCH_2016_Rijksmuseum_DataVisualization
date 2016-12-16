import xml.etree.ElementTree as ET, json

artist_list = []

tree = ET.parse('ULAN2.xml')
root = tree.getroot()
ns = {'xmlns':"http://localhost/namespace"}

for subject in root.findall('xmlns:Subject', ns):
    
    artist_dictionary = {}
    artist_dictionary = (subject.attrib)

    for nationalities in subject.findall('xmlns:Nationalities', ns):
        for preferred_nationality in nationalities.findall('xmlns:Preferred_Nationality', ns):
            for nationality_code in preferred_nationality.findall('xmlns:Nationality_Code', ns):
                if nationality_code.text == '905020/Dutch':
                    artist_dictionary['nationality_code'] = (nationality_code.text)
     
                    for roles in subject.findall('xmlns:Roles', ns):
                        for preferred_role in roles.findall('xmlns:Preferred_Role', ns):
                            for preferred_role_id in preferred_role.findall('xmlns:Role_ID', ns):
                                if preferred_role_id.text == '31100/artist':
                                    artist_dictionary['preferred_role_id'] = (preferred_role_id.text)

                                    for terms in subject.findall('xmlns:Terms', ns):
                                        prf_terms = []
                                        for preferred_term in terms.findall('xmlns:Preferred_Term', ns):
                                            prf = {}

                                            for preferred_term_text in preferred_term.findall('xmlns:Term_Text', ns):
                                                prf['preferred_term_text'] = (preferred_term_text.text)
                                                for term_id in preferred_term.findall('xmlns:Term_ID', ns):
                                                    prf['term_id'] = (term_id.text)
                                                for display_name in preferred_term.findall('xmlns:Display_Name', ns):
                                                    prf['display_name'] = (display_name.text)
                                                    prf_terms.append(prf)

                                            artist_dictionary['preferred terms'] = prf_terms

##                                        for terms in subject.findall('xmlns:Terms', ns):
##                                            non_terms = []
##                                            for non_preferred_term in terms.findall('xmlns:Non-Preferred_Term', ns):
##                                                non = {}
##
##                                                for non_preferred_term_text in non_preferred_term.findall('xmlns:Term_Text', ns):
##                                                    non['non_preferred_term_text'] = (non_preferred_term_text.text)
##                                                    for term_id in non_preferred_term.findall('xmlns:Term_ID', ns):
##                                                        non['term_id'] = (term_id.text)
##                                                    for display_name in non_preferred_term.findall('xmlns:Display_Name', ns):
##                                                        non['display_name'] = (display_name.text)
##                                                        non_terms.append(non)
##
##                                                artist_dictionary['non_preferred terms'] = non_terms  

                                    artist_list.append(artist_dictionary)
        
with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists2PT.json', 'w') as outfile:
    json.dump(artist_list, outfile, indent=2)
