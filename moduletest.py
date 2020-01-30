from pprint import pprint
with open("my_output.txt") as f:
	readfile = f.read()

for line in readfile.splitlines():
    if  "N9K-X97160YC-EX" in line and "48x10/25G" in line and "ok" in line:
        print ("The status of card {} is {}".format(line[:1], line.split()[-1]))
    elif  "N9K-X9736C-FX" in line and "36x40/100G" in line and  "ok" in line:
        print ("The status of card {} is ok".format(line[:2]))
    elif "N9K-C9504-FM-E" in line and "4-slot Fabric Module" in line and "ok" in line:
        print ("The status of card {} is ok".format(line[:2]))
    elif "N9K-X9736C-FX" in line and "36x40/100G" in line and "ok" not in line:
        print ("The status of card {} is {}".format(line[:1], line.split()[-1]))
    elif "N9K-X97160YC-EX" in line or "N9K-X9736C-FX" in line or "N9K-C9504-FM-E" in line and "detected" or "Powered-Up" in line:
        break
