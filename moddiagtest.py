import re
from pprint import pprint
with open("output_filev2.txt") as f:
        s = f.read()


a = "Mod  Online Diag Status"
b = "* this terminal session"

z = (s[s.find(a)+ len(a):s.find(b)])

modstatus = []
for line in z.splitlines():
        modstatus.append(line)

allmods = modstatus[2:14]
for line in allmods:
    pprint("The diag status for each module is  as follows: {}".format(line))

pprint ("------------------------------------------------------")


pprint ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for line in allmods:
    if "Pass" not in line.split():
        pprint("CHECK THE STATUS OF LINECARD: {}".format(line))
pprint ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
