#if number occurs 3 or more times, print number
lst1 = [50,50,3,5,50,1,2,3,6,6,6,6]
lst_dict = {}


#Function to build the dict and a for loop outside to print the result

#def build_dict(list1):
#   for i in list1:
#       count = 0
#       if i in lst_dict:
#           lst_dict[i]  += 1
#       else:
#            lst_dict[i] = 1

#build_dict(lst1)


#for k,v in lst_dict.items():
#    if v >= 3:
#        print("The value that apprears more that or equal to 3 is: {}".format(k))


#single function below but it has to open another empty dict to store values because it loops only once in lst_dict if returned after the for loop  

def more_than_3(list1):
    final_dict = {}
    for i in list1:
        if i in lst_dict:
            lst_dict[i]  += 1
        else:
            lst_dict[i] = 1
    for k,v in lst_dict.items():
        if v >= 3:
            final_dict[k] = v
    return ("The item more than or equal to 3 times is {}".format(final_dict))


print(more_than_3(lst1))




