#!/bin/bash
#Author: Piotr Koska
zone=$1
# Change all dot to dash
resources=${zone//./-}
while read line;
do 
    #[ -z "$line" ] && continue 
    terraform import ovh_domain_zone_record.ID-${line}-${resources} ${line}.${1}
done < "${1}.ids"