from pprint import pprint
from collections import Counter
def readblr01(blr01file):
    with open(blr01file) as f:
        return f.read()


def readblr02(blr02file):
    with open(blr02file) as f:
        return f.read()

devicelistblr1 = []

def find_blr01_devices(blr01):
    for line in blr01.splitlines():
        if "eng" in line.split("."):
            if "blr01" in line.split()[0]:
                continue
            elif "blr02" in line.split()[0]:
                continue
            devicelistblr1.append(line)
    return devicelistblr1


devicelistblr2 = []

def find_blr02_devices(blr02):
    for line in blr02.splitlines():
        if "eng" in line.split("."):
            if "blr01" in line.split()[0]:
                continue
            elif "blr02" in line.split()[0]:
                continue
            devicelistblr2.append(line)
    return devicelistblr2



blr01file = "engblr01-lldp.txt"
blr02file = "engblr02-lldp.txt"
blr01fileread = readblr01(blr01file) 
blr02fileread = readblr02(blr02file)
blr01 = find_blr01_devices(blr01fileread)
blr02 = find_blr02_devices(blr02fileread)
devicelistblr1.sort() 
devicelistblr2.sort()
res1 = list((Counter(devicelistblr1) - Counter(devicelistblr2)).elements())
res2 = list((Counter(devicelistblr2) - Counter(devicelistblr1)).elements())

if len(res1) == 0 or  len(res2) == 0:
    print ("BLR01 neighbors match BLR02 neighbors")
elif len(res1) != 0 or len(res2) != 0:
    print("The lldp neighbors in BLRO1 but not in BLR02 are: {}".format(res1))
    print ("The lldp neighbors in BLRO2 but not in BLR01 are: {}".format(res2))





