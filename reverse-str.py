#def revstr(a):
#    b = (list(reversed(a))) #using reversed method
#    rev = "".join(b)
#    #b = a[::-1] #using extended slice syntax
#    #return b
#    return rev


def revstr(word):
    reversedword = ""
    lst_word = list(word)
    for i in reversed(lst_word):
        reversedword += i
    return reversedword
print(revstr("akash"))
