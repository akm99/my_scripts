from pprint import pprint
from collections import Counter


with open("lldp-nei-before") as f:
    fileread = f.read()
with open("lldp-nei-after") as f:
    filereadaft = f.read()

device_lldp_before = {}
device_lldp_after = {}
lst1 = {}
lst2 = ""

for line in fileread.splitlines():
    if "blr01" in line:
        continue
    elif "ams" in line:
        lst1[line] = None 
#device_lldp_before = dict(zip(lst1,lst2))


pprint(lst1)
pprint(lst2)
device_lldp_after = []
for line in filereadaft.splitlines():
    if  "ams" in line or "Eth" in line:
        device_lldp_after.append(line) 

#pprint(device_lldp_before)
#pprint(device_lldp_after)


def list_diff(list1, list2):
    out = []
    for ele in list1:
        if not ele in list2:
            out.append(ele)
    return out
#pprint(list_diff(device_lldp_before, device_lldp_after))



