import re
from pprint import pprint
with open("output_filev2.txt") as f:
        readfile = f.read()


for line in readfile.splitlines():
    if "Online Diag Status" in line:
        print (line)

match = re.search(r'\d\d', readfile)
pprint (match.group())
