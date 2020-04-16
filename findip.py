from collections import Counter
from pprint import pprint
with open("shiproute-before") as f:
    fileread1 = f.read()

with open("shiproute-after") as f:
    fileread2 = f.read()

before31 = set()
for line in fileread1.splitlines():
    if "ubest" in line:
        before31.add(line.split()[0])
#    elif "7" in line.split("."):
#        before31.add(line)

after31 = set()
for line in fileread2.splitlines():
    if "ubest" in line:
        after31.add(line.split()[0])
#    elif "7" in line.split("."):        
#        after31.add(line)

delta = before31.difference(after31)


print("The difference in routing table is: {}".format(delta))
