data = {"L1": {"f1", "f2", "f4"},
        "L2": {"f2", "f3", "f4", "f5"},
        "L3": {"f5","f2","f4","f6","f7"}}


input_links = {"f7","f5"}

impact = []

for key in data:
    for info in input_links:
        if info in data[key]:
            impact.append(key)
            

impact = set(impact)
print("impact is: {}".format(impact))
