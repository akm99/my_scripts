from pprint import pprint
with open("devicelist.txt") as f:
        readfile = f.read()


sort_by_site = [ ]
site_dict = {}
sites = []

for line in readfile.splitlines():
    z = line.split(".")[0]
    sites.append(z)


sites = list(set(sites)) 


for site in sites:
   for line in readfile.splitlines():
        if site in line.split(".")[0]:
            sort_by_site.append(line)
            site_dict[line] = site


#pprint (sort_by_site)
pprint (site_dict)
        
