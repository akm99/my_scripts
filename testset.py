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


pprint(set(blr01lldp) ^ set(blr02lldp))
