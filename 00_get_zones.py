# -*- encoding: utf-8 -*-
# Author: Piotr Koska
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
import ovh
import os

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client(
    endpoint=os.environ['OVH_ENDPOINT'],               # Endpoint of API OVH Europe (List of available endpoints)
    application_key=os.environ['OVH_APPLICATION_KEY'],    # Application Key
    application_secret=os.environ['OVH_APPLICATION_SECRET'], # Application Secret
    consumer_key=os.environ['OVH_CONSUMER_KEY'],       # Consumer Key
)

result = client.get('/domain/zone')

zones = json.dumps(result)

# Remove charakter
disallowed_characters = '[]"'

for character in disallowed_characters:
	zones = zones.replace(character, "")

# Change to list
zones = zones.replace(", "," ")
zones_list = zones.split()
zones_list.sort(reverse=False)

# Save zones
with open("00_zones", 'w') as fp:
    for item in zones_list:
        # write each item on a new line
        fp.write("%s\n" % item)