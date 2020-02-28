from pprint import pprint
from collections import Counter
with open("engblr01-lldp.txt") as f:
    blr01lldpread = f.read()

with open("engblr02-lldp.txt") as f:
    blr02lldpread = f.read()

blr01lldp = []
for line in blr01lldpread.splitlines():
    if "blr02.net.az1.eng.pdx.wd" in line:
        continue
    elif "blr01.net.az1.eng.pdx.wd" in line:
        continue
    elif "eng" in line.split("."):
        blr01lldp.append(line)


blr02lldp = []
for line in blr02lldpread.splitlines():
    if "blr01.net.az1.eng.pdx.wd" in line:
        continue
    elif "blr02.net.az1.eng.pdx.wd" in line:
        continue
    elif "eng" in line.split("."):
        blr02lldp.append(line)


blr01lldp.sort() 
blr02lldp.sort() 
res1 = list((Counter(blr01lldp) - Counter(blr02lldp)).elements())
res2 = list((Counter(blr02lldp) - Counter(blr01lldp)).elements())
#print("\n")
print("*************************************************************")
print("The lldp neighbors in BLRO1 but not in BLR02 are: {}".format(res1))
#print("\n")
print("*************************************************************")
print("The lldp neighbors in BLRO2 but not in BLR01 are: {}".format(res2))
