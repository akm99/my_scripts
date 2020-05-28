list1 = [1,2,3,4,6,6,6,6,1,1,4,4]
list2 = [4,6,7,8]


def find_diff_list(l1,l2):
    l1 = set(l1) - set(l2)
    return l1


print(find_diff_list(list1,list2))

