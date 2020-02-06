from pprint import pprint
with open("output_filev2.txt") as f:
        readfile = f.read()

for line in readfile.splitlines():
    if  "N9K-X97160YC-EX" in line and "48x10/25G" in line:
        pprint ("The status of card {} is {}".format(line.split()[0],line.split()[-1]))
    elif  "N9K-X9736C-FX" in line and "36x40/100G" in line:
        pprint ("The status of card {} is {}".format(line.split()[0],line.split()[-1]))
    elif "N9K-C9504-FM-E" in line and "4-slot Fabric Module" in line:
        pprint ("The status of card {} is {}".format(line.split()[0],line.split()[-1]))
    elif "logging" in line:
        break
print ("\n")
for line in readfile.splitlines():
    if "Online Diag Status" in line or "Pass" in line:
        print (line)
    elif "logging" in line:
        break

