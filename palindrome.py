def fun(string):
    s = string[::-1]
    if(string == s):
    	return True
    else:
        return False

print("The result for madam is: {}".format(fun("madam")))
print("The result for akash is: {}".format(fun("akash")))
