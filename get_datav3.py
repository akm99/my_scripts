from getpass import getpass
from pprint import pprint
from netmiko import Netmiko
cisco1 = {
    "host": "blr01.net.az.lab.pdx.wd",
    "username": "labadmin",
    "password": getpass(),
    "device_type": "cisco_nxos",
}


with open("commands.txt") as readcmd:
    cmd_open = readcmd.read().splitlines()


net_connect = Netmiko(**cisco1)
output_file = " "

for command in cmd_open:
    output_file += command
    output_file += "\n"
    output_file +=  net_connect.send_command(command)
net_connect.disconnect()
f= open("output_filev2.txt","w+")
f.write(output_file)
f.close()
