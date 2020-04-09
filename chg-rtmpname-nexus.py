#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "host": "blr01.net.az.lab.pdx.wd",
    "username": "labadmin",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

net_connect = Netmiko(**cisco1)
command1 = "sh run"
#print()
#print(net_connect.find_prompt())
#output = net_connect.send_command(command)
#net_connect.disconnect()
#print(output)

catch = ""
output = net_connect.send_command(command1)
for line in output.splitlines():
    for word in line.split():
        if "724459" in word:
            catch += word



repword = (catch.replace("724459" , "9001011"))
command3 = "route-map " + repword
command4 = "no route-map " + catch
cfg_commands = [command3, command4]
output3 = net_connect.send_config_set(cfg_commands)
net_connect.disconnect()

