from pprint import pprint
d = {
    "rtr1" : {
                "bgp_peers" : ["10.1.1.1","10.1.1.3"],
                "device_type" : "juniper_junos"},
    "rtr2" : {
                "bgp_peers" : ["10.2.1.1","10.2.1.3"],
                "device_type" : "juniper_junos"},
    "rtr3" : {
                "bgp_peers" : ["10.3.1.1","10.3.1.3"],
                "device_type" : "juniper_junos"}
}


#pprint (routers.keys())
#pprint (routers["rtr1"])
#pprint (routers["rtr1"].keys())
#pprint ("The bgp peers for rtr1 are: {}".format(routers["rtr1"]["bgp_peers"]))

for key,value in d.items():
    pprint((key,value))

for key,value in d.items():
    s = {k: d[k] for k in sorted(d, key=d.get)}
    pprint(s)
