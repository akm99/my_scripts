from pprint import pprint

data = [
{ "age": 10},
{ "age": 5},
{ "age": 7}
]

#print (sorted(data, key = lambda i: i['age']))

int_traffic_list = [
{ "intid" : "eth1", "traffic" : "200kb"},
{ "intid" : "eth2", "traffic" : "300kb"},
{ "intid" : "eth3", "traffic" : "400kb"}
]
#print (sorted(int_traffic_list, key = lambda i: i['traffic']))

int_traffic_dict = { 
                    "a":{"intid" : "eth3", "traffic" : "500kb"},
                    "b":{"intid" : "eth1", "traffic" : "100kb"},
                    "c":{"intid" : "eth2", "traffic" : "400kb"}
}


for k,v in sorted(int_traffic_dict.items()):
    i,j in sorted(k.items())
        print(i,j)
