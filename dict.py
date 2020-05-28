from pprint import pprint
routers = {
    "rtr1" : {
                "bgp_peers" : ["10.1.1.1", "20.1.1.1"],
                "device_type" : ["juniper_junos"]},
    "rtr2" : {
                "bgp_peers" : ["30.1.1.1","40.1.1.1"],
                "device_type" : ["juniper_junos"]},
    "rtr3" : {
                "bgp_peers" : ["50.1.1.1","60.1.1.1"],
                "device_type" : ["juniper_junos"]}
}
#pprint (routers.keys())
#pprint (routers["rtr1"])
#pprint (routers["rtr1"].keys())
#pprint ("The bgp peers for rtr1 are: {}".format(routers["rtr1"]["bgp_peers"])
#for item in routers.items():
   # print(item)
#routers["rtr1"]["hostname"] = "pdx.rtr1"
#for loop to get k,v from a dictionary inside a dictionary 
#for k,v in routers.items():
#   for k1,v1 in v.items():
#        print(k1,v1)


#Using the dictionary update method to add another key inside the three keys rtr1,rtr2,rtr3
for k,v in routers.items():
        v.update({"eigrp_peer" : "na"})

#Changing value of all dictionaries inside main dictionary, here we changed device_type from juniper to cisco
for k,v in routers.items():
    v.update({"eigrp_peer" : "comeslater"})


#Add another value to existing key/value by using list append(the original value must be created as a list to begin with)
for k,v in routers.items():
     v["device_type"].append("arista")
#    for k1,v1 in v.items():
       # v["device_type"].append("arista")        
        #break


#Method to update the value in nested dictionary for particular value, two methods below
routers["rtr1"]["eigrp_peer"] = "100.1.1.1"
routers["rtr2"].update({"eigrp_peer":"200.1.1.1"})
routers["rtr3"].update({"eigrp_peer":"300.1.1.1"})

#printing the key value inside nested key with better presentation
for k,v in routers.items():
    print("The router is: {}".format(k))
    for k1 in v:
        print(k1 + " The values are: {}".format(v[k1]))

#printing a single key inside the nested key
for k,v in routers.items():
    print(k + " BGP peers are: {}".format(v["bgp_peers"]))



for k,v in routers.items():
    print(k,v)
    for k1 in v:
        print(v[k1])
