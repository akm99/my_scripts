from pprint import pprint
with open("shipintbrief.txt") as f:
    fileread = f.read()

ip = input("Enter the ip address you are looking for: ")
if ip in fileread:
    print("ip found")
else:
    print("ip not found")
