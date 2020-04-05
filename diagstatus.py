import re
from pprint import pprint
with open("output_filev2.txt") as f:
        readfile = f.read()


for line in readfile.splitlines():
    if "Online Diag Status" in line:
        print (line)

#for line in readfile.splitlines():
match = re.search(r'\w{4}$', readfile)
pprint (match)
pprint (match.group(0))
