new_list = [1,1,2,3,4,5,6,7,1,2,2]

new_dict = {}

for ind,elem in enumerate(new_list):
    if elem in new_dict:
        new_dict[elem].append(ind)
    else:
        #his method, internet
        #new_dict.update({elem:[ind]})
        new_dict[elem] = [ind]



print(new_dict)
for k,v in new_dict.items():
    if len(v) >= 3:
        print("The Value that apprears 3 more more times is: {}".format(k))
