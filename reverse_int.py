def reverse_integer(x):
    x = str(x)
    lst = list(x)  # list('123456789') returns ['1', '2', '3'.. and so on]
    lst.reverse()
    x = "".join(lst)
    x = int(x)
    return x


print(reverse_integer(123456789))

