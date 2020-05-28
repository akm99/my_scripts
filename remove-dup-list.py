list1 = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3] 


def rem_dup(lst):
    new_l = []
    for i in lst:
        if i not in new_l:
            new_l.append(i)
        else:
            continue
    lst = new_l
    return lst



print(rem_dup(list1))
