from pprint import pprint
from collections import Counter
with open("engblr01-lldp.txt") as f:
    blr01lldpread = f.read()

with open("engblr02-lldp.txt") as f:
    blr02lldpread = f.read()

blr01lldp = []
for line in blr01lldpread.splitlines():
    if "blr01.net.az1.eng.pdx.wd" in line:
        continue
    elif "blr02.net.az1.eng.pdx.wd" in line:
        continue
    elif "eng" in line:
        blr01lldp.append(line)
blr02lldp = []
for line in blr02lldpread.splitlines():
    if "blr01.net.az1.eng.pdx.wd" in line:
        continue
    elif "blr02.net.az1.eng.pdx.wd" in line:
        continue
    elif "eng" in line:
        blr02lldp.append(line)

#pprint(Counter(blr01lldp))
#blr01lldp.sort() 
#blr02lldp.sort() 



res1 = list((Counter(blr01lldp) - Counter(blr02lldp)).items())
res2 = list((Counter(blr02lldp) - Counter(blr01lldp)).items())
#.elements method returns every element that is different, for example 2xclb links that are different in both blrs are shown as 2xclbs
#.items returns the count, for example 2xclbs links that are different are represented as clb-hostname,2
#print("\n")
print("*************************************************************")
print("The lldp neighbors in BLRO1 but not in BLR02 are: {}".format(res1))
#print("\n")
print("*************************************************************")
print("The lldp neighbors in BLRO2 but not in BLR01 are: {}".format(res2))
