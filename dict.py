from pprint import pprint
routers = {
    "rtr1" : {
                "bgp_peers" : ["10.1.1.1", "20.1.1.1"],
                "device_type" : "juniper_junos"},
    "rtr2" : {
                "bgp_peers" : ["30.1.1.1","40.1.1.1"],
                "device_type" : "juniper_junos"},
    "rtr3" : {
                "bgp_peers" : ["50.1.1.1","60.1.1.1"],
                "device_type" : "juniper_junos"}
}


#pprint (routers.keys())
#pprint (routers["rtr1"])
#pprint (routers["rtr1"].keys())
#pprint ("The bgp peers for rtr1 are: {}".format(routers["rtr1"]["bgp_peers"]))


#for item in routers.items():
   # print(item)


#routers["rtr1"]["hostname"] = "pdx.rtr1"

#for loop to get k,v from a dictionary inside a dictionary 
#for k,v in routers.items():
#   for k1,v1 in v.items():
#        print(k1,v1)



#Changing value of all dictionaries inside main dictionary, here we changed device_type from juniper to cisco
for k,v in routers.items():
    for k1,v1 in v.items():
        v["device_type"] = "cisco"



for k,v in routers.items():
    for k1,v1 in v.items():
        v["hostname"] = "host"

for item in routers.items():
    print(item)
