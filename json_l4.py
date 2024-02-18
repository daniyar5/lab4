# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 

import json
file = open("sample-data.json")

data_json = file.read()

a = json.loads(data_json)

print("Interface Status")
print("=" * 80)
print("DN", "\t\t\t\t\t\t", "  Description", "\t\t", " Speed", "   MTU")
print("-" * 50, "-" * 19, "\t", "-------", "  ----")

for x in a["imdata"]:
    print(x["l1PhysIf"]["attributes"]["dn"], "\t\t\t\t" , x["l1PhysIf"]["attributes"]["speed"], " ", x["l1PhysIf"]["attributes"]["mtu"])

        