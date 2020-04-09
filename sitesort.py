from pprint import pprint
with open("devicelist.txt") as f:
    readfile = f.read()

sites = []
for line in readfile.splitlines():
    id = line.split(".")[0]
    sites.append(id)

site_id = (set(sites))

sorting = {}
for line in readfile.splitlines():
    for site in site_id:
        if site in line:
            sorting[line] = site


pprint(sorting)

