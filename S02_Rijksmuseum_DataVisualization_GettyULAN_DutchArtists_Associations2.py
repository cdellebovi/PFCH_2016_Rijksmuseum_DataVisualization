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

                                    for associative_relationships in subject.findall('xmlns:Associative_Relationships', ns):
                                        asc_relationships = []
                                        for associative_relationship in associative_relationships.findall('xmlns:Associative_Relationship', ns):
                                            asc = {}
                                            
                                            for relationship_type in associative_relationship.findall('xmlns:Relationship_Type', ns):
                                                asc['relationship_type'] = (relationship_type.text)
                                                for related_subject_id in associative_relationship.findall('xmlns:Related_Subject_ID', ns):
                                                    for vp_subject_id in related_subject_id.findall('xmlns:VP_Subject_ID', ns): 
                                                        asc['vp_subject_id'] = (vp_subject_id.text)
                                                        asc_relationships.append(asc)

                                            artist_dictionary['associations'] = asc_relationships

                                    artist_list.append(artist_dictionary)
        
with open('S02_Rijksmuseum_DataVisualization_GettyULAN_DutchArtists_Associations2.json', 'w') as outfile:
    json.dump(artist_list, outfile, indent=2)
