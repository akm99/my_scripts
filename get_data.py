from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
cisco1 = {
    "host": "blr01.net.az.lab.pdx.wd",
    "username": "labadmin",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

net_connect = Netmiko(**cisco1)
cmd1 = "show mod | no-more"
cmd2 = "show run | no-more"
cmd3 = "show int status | no-more"
cmd4 = "sh ip interface brief | ex unas | no-more"
cmd5 = "show logging | no-more"
cmd6 = "show ip ospf nei | no-more"
cmd7 = "show ip route summary"
cmd8 = "show ip route | no-more"
cmd9 = "sh ip bgp sum | no-more"
cmd10 = "sh ip bgp | no-more"
cmd11 = "sh cdp nei | no-more"
cmd12 = "sh lldp nei | no-more"
cmd13 = "sh vrf"
cmd14 = "sh ip bgp sum vrf pci"
cmd15 = "sh ip ospf nei vrf app"
cmd16 = "sh ip route vrf pci | no-more"
cmd17 = "sh ip route vrf app | no-more"
cmd18 = "show env power | no-more"
cmd19 = "show env temp | no-more"

print()
#print(net_connect.find_prompt())
o1 = net_connect.send_command(cmd1)
o2 = net_connect.send_command(cmd2)
o3 = net_connect.send_command(cmd3)
o4 = net_connect.send_command(cmd4)
o5 = net_connect.send_command(cmd5)
o6 = net_connect.send_command(cmd6)
o7 = net_connect.send_command(cmd7)
o8 = net_connect.send_command(cmd8)
o9 = net_connect.send_command(cmd9)
o10 = net_connect.send_command(cmd10)
o11 = net_connect.send_command(cmd11)
o12 = net_connect.send_command(cmd12)
o13 = net_connect.send_command(cmd13)
o14 = net_connect.send_command(cmd14)
o15 = net_connect.send_command(cmd15)
o16 = net_connect.send_command(cmd16)
o17 = net_connect.send_command(cmd17)
o18 = net_connect.send_command(cmd18)
o19 = net_connect.send_command(cmd19)
net_connect.disconnect()
f= open("my_output.txt","w+")
f.write(o1)
f.write(o2)
f.write(o3)
f.write(o4)
f.write(o5)
f.write(o6)
f.write(o7)
f.write(o8)
f.write(o9)
f.write(o10)
f.write(o11)
f.write(o12)
f.write(o13)
f.write(o14)
f.write(o15)
f.write(o16)
f.write(o17)
f.write(o18)
f.write(o19)
f.close()

#pprint (o1)
#pprint (o2)
#pprint (o3)
#pprint (o4)
#pprint (o5)
#pprint (o6)
#pprint (o7)
#pprint (o8)
#pprint (o9)
#pprint (o10)
#pprint (o11)
#pprint (o12)
#pprint (o13)
#pprint (o14)
#pprint (o15)
#pprint (o16)
#pprint (o17)
#pprint (o18)
#pprint (o19)
print()
