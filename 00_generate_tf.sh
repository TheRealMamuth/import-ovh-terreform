#!/bin/bash
# Author: Piotr Koska
while read line;
do 
    #[ -z "$line" ] && continue
    OVH_ZONE=${line}
    echo "Generate file for $OVH_ZONE"
    python3 00_config_tf.py
    # if do not want import to tf state comment out line below
    ./00_import_tf_state.sh "$OVH_ZONE"
done < 00_zones.txt