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


pprint (routers.keys())
pprint (routers["rtr1"])
pprint (routers["rtr1"].keys())
pprint ("The bgp peers for rtr1 are: {}".format(routers["rtr1"]["bgp_peers"]))


