from pprint import pprint
with open("shipintbrief.txt") as f:
    fileread = f.read()

ip = input("Enter the ip address you are looking for: ")
ip_list = {}
for line in fileread.splitlines():
	if ip in line.split():
	    ip_list.update({line.split()[0]:line.split()[1]})

if len(ip_list) == 0:
    print("ip not found")
else:
    print("The ip/interface found are: {}".format(ip_list))
