from pprint import pprint

data = [
{ "age": 10},
{ "age": 5},
{ "age": 7}
]

print (sorted(data, key = lambda i: i['age']))

int_traffic_list = [
{ "intid" : "eth1", "traffic" : "200kb"},
{ "intid" : "eth2", "traffic" : "300kb"},
{ "intid" : "eth3", "traffic" : "400kb"}
]

print (sorted(int_traffic_list, key = lambda i: i['traffic']))

int_traffic_dict = { 
                    2:{"intid" : "eth3", "traffic" : 500},
                    1:{"intid" : "eth1", "traffic" : 400},
                    3:{"intid" : "eth2", "traffic" : 2}
}


print(sorted(int_traffic_dict,reverse=True))
