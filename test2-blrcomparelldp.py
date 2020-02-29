from pprint import pprint
from collections import Counter
with open("lldptestfile1") as f:
    blr01lldpread = f.read()

with open("lldptestfile2") as f:
    blr02lldpread = f.read()

blr01lldp = []
for line in blr01lldpread.splitlines():
    if "eng" in line.split("."):
        if "blr01" in line.split()[0]:
            continue
        elif "blr02" in line.split()[0]:
            continue
        blr01lldp.append(line)


blr02lldp = []
for line in blr02lldpread.splitlines():
    if "eng" in line.split("."):
        if "blr01" in line.split()[0]:
            continue
        elif "blr02" in line.split()[0]:
            continue
        blr02lldp.append(line)
    

blr01lldp.sort() 
blr02lldp.sort() 
res1 = list((Counter(blr01lldp) - Counter(blr02lldp)).elements())
res2 = list((Counter(blr02lldp) - Counter(blr01lldp)).elements())
#print("\n")
#print("*************************************************************")
#print("The lldp neighbors in BLRO1 but not in BLR02 are: {}".format(res1))
#print("\n")
#print("*************************************************************")
#print("The lldp neighbors in BLRO2 but not in BLR01 are: {}".format(res2))


compare = (set(blr01lldp) ^ set(blr02lldp))


if len(compare) == 0:
    print ("The LLDP neighbors are the same")
else:
    print("The items are: {} ".format(compare))



