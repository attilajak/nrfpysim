# NRF Simulator

NRF Simulator in python

Installation
------------

NOTE: This simulator has been tested on Python 3.8.1 but does not preclude working on other python 3.x environments

Install all dependencies using below command:

pip install -r requirements.txt

Note: if couchbase python module or couchbase backend Installation is problematic, you can disable database access and only simulate

Running Simulator
-----------------

python ./Nnrf_NFManagement/\__init__.py

NOTE: Use CTRL-C to kill simulator

Schema Verification Extension
------------------------------

Currently schema verification is supported for Nnrf_NFManagement service only and schema is converted from YAML to JSON (using Swagger). TS29510_Nnrf_NFManagement.json is generated from TS29510_Nnrf_NFManagement.yaml using below command (assuming swagger-codegen is installed from github)

java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i TS29510_Nnrf_NFManagement.yaml -l openapi -o samples/server/nrfopenapi

NOTE: All the schema reference dependencies (additional YAML files) need to be in the same path as source YAML file which is being resolved to JSON.

Resolved JSON schema will be generated in samples/server/nrfopenapi folder with name "openapi.json". This schema should have all schema references resolved and contained in the same document.

For schema verification of additional NRF sub services, (Discovery etc), above procedure can be repeated and necessary python classes need to be added to handle schema verification 

Next Steps
----------------

