from collections import Counter
from pprint import pprint
with open("blr01amssip") as f:
    fileread1 = f.read()

with open("blr02amssip") as f:
    fileread2 = f.read()

before31 = set()
for line in fileread1.splitlines():
    if "/32" in line:#/32 routes hidden for interface ips on each blr/vlan int ip, but not ideal since it hides all /31s
        continue
    elif "ubest" in line:
        before31.add(line.split()[0])
#    elif "7" in line.split("."):
#        before31.add(line)

after31 = set()
for line in fileread2.splitlines():
    if "/32" in line:#/32 routes hidden for interface ips on each blr/vlan int ip, but not ideal since it hides all /31s
        continue
    elif "ubest" in line:
        after31.add(line.split()[0])
#    elif "7" in line.split("."):        
#        after31.add(line)

delta1 = before31.difference(after31)
delta2 = after31.difference(before31)

pprint("The routes that are in blr01 but not in blr02 are: {}".format(delta1))
pprint("The routes that are in blr02 but not in blr01 are: {}".format(delta2))
