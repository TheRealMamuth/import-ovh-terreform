# -*- encoding: utf-8 -*-
# Author: Piotr Koska
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
import ovh
import os
import fileinput

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page

client = ovh.Client(
    endpoint=os.environ['OVH_ENDPOINT'],               # Endpoint of API OVH Europe (List of available endpoints)
    application_key=os.environ['OVH_APPLICATION_KEY'],    # Application Key
    application_secret=os.environ['OVH_APPLICATION_SECRET'], # Application Secret
    consumer_key=os.environ['OVH_CONSUMER_KEY'],       # Consumer Key
)

# Taken ID from zone
zone_record = "/domain/zone/"+os.environ['OVH_ZONE']+"/record"
result = client.get(zone_record)

# Dump json
zone_ids = json.dumps(result)

# Remove charakter
disallowed_characters = "[]"

for character in disallowed_characters:
	zone_ids = zone_ids.replace(character, "")

# Change for list
zone_ids = zone_ids.replace(", "," ")
zone_list_ids = zone_ids.split()

# Save ids
with open(os.environ['OVH_ZONE']+".ids", 'w') as fp:
    for item in zone_list_ids:
        # write each item on a new line
        fp.write("%s\n" % item)

# Create resources zone in .tf file
for id in zone_list_ids:
    id_record = zone_record+"/"+id
    id_result = client.get(id_record)

    json_id_result = json.dumps(id_result)
    json_object = json.loads(json_id_result) 

    file_tf = os.environ['OVH_ZONE']+".tf"

    with open(file_tf, 'a') as f: 
        f.write('\nresource "ovh_domain_zone_record" "ID-%s-%s" {\n' % (json_object["id"],os.environ['OVH_ZONE'].replace(".","-")))
        for key, value in json_object.items():
            f.write('\t%s = "%s"\n' % (key.lower().replace("id","#id"), str(value).replace('"','\\"')))
        f.write('}\n')