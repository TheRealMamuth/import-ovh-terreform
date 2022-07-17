# import-ovh-terreform
This repository contain code to get Zone ID from ovh and generate tf file for import domain to terraform state.
This is for existing zones in OVH without terraform configuration.

## Requirements
 - python3
 - bash(5.1v)

## How to use.

### Export Variable

Set five variables `OVH_ZONE`, `OVH_CONSUMER_KEY`, `OVH_APPLICATION_SECRET`, `OVH_APPLICATION_KEY`, `OVH_ENDPOINT` contain api key for OVH API. Read only permissions needed.

```bash
export OVH_ZONE="example.com"
export OVH_CONSUMER_KEY='xxxxxxxxxxx'
export OVH_APPLICATION_SECRET='xxxxx'
export OVH_APPLICATION_KEY='xxxxxxxx'
export OVH_ENDPOINT='ovh-eu'
```

### Run scripts

First run `python3 ./00_get_zones.py` to grep all zone from your OVH account. This create 00_zones file with your all zone in ovh.

Then run `./00_generate_tf.sh` bash script to generate tf configuration file for all zones entries. 

(This runs python script `python3 00_config_tf.py` for generate configuration file for each zone in separate file. This script `00_import_tf_state.sh` run terraform import command based on previously generated files `your-zone.com.tf` and `your-zone.com.ids` )

If you do not want to start the import, comment out the line below in file `./00_generate_tf.sh`

```bash
./00_import_tf_state.sh "$OVH_ZONE"
```