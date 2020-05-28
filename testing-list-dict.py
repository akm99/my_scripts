



keys = ['Name','Emp ID','Contact Info']
values = ['Ken','ED445','#########']


res = {} 

for k in keys: 
    for v in values:
        res[k] = v
        values.remove(v)
        break

print(res)
