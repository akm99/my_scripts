from pprint import pprint
int_rate = {"eth1": "200kb","eth2":"300kb","eth3":"400kb"}
int_rate["eth1"] = "500kb"
int_rate.update({"eth4":"700kb"})


#pprint (int_rate)


#for k,v in int_rate.items():
#    if k == "eth4":
#       print (k,v)


int_rate2 = {"speed" : 10}
new_dict = {"int7" : "1mb", "speed":25}
int_rate.update(int_rate2)


lst = []
lst.append(int_rate)
lst.append(new_dict)
#pprint(lst)

print (sorted(lst, key = lambda i: i['speed']))
