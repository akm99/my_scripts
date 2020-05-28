from pprint import pprint
with open("shiparp") as f:
    fileread = f.read()

iptable = {}
for line in fileread.splitlines():
    if "10" in line and "Eth" in line:
        iptable[line.split()[0]] = [line.split()[-1]]


ui = input(str("enter ip to check: "))

for k,v in iptable.items():
    if k == ui:
        pprint("IP found, the interface is:{} {} ".format(k,v))
        break
else:
    print("ip not found")
