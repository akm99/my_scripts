from pprint import pprint

data = [
{ "age": 10},
{ "age": 5},
{ "age": 7}
]

print (sorted(data, key = lambda i: i['age']))
