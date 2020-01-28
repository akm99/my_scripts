with open("my_output.txt") as f:
    file_open = f.read()

count = 0
for line in file_open.splitlines():
	if "N9K-PAC-3000W-B" in line:
		count = count+1

print ("\nThe total power supplies installed are: {}\n".format(count))


for line in file_open.splitlines():
    if 'N9K-PAC-3000W-B' in line and "Ok" in line:
        print("The following power supplies are in Ok status: Power Supply: {}".format(line[0]))
    elif 'N9K-PAC-3000W-B' in line and 'Ok' not in line:
        print("!!!!The following power supplies needs to be CHECKED!!!!: Power Supply: {}".format(line[0]))
