from pprint import pprint
my_list = [1,1,9,21,16,51,1]
my_dict = {}
for (ind,elem) in enumerate(my_list):
    if elem in my_dict:
        my_dict[elem].append(ind)
        #print(my_dict)
    else:
        my_dict.update({elem:[ind]})
        print(my_dict)

#print(my_dict)
for key,value in my_dict.items():
    if len(value) > 1:
        print ("key has indices: {} {} ".format(key,value))


