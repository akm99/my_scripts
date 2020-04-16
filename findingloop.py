from pprint import pprint
str = "a,b,1,4,1"

inp = input("Enter the ip address you are looking for: ")

for i in str:
    if inp == i:
       pprint("String found at index: {}".format(str.find(i)))
else:
    pprint("str not found")
