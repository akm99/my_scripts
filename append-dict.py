from pprint import pprint

dict = {"name" : "akash" , "hobbies" : ["cricket","table tennis"]}
#creating the two values with {} makes it a set and cannot be appended, it works when the 
#values are created as lists
dict["hobbies"].append("khoti")
pprint(dict)
pprint(dict.items())
pprint(dict["hobbies"])

