data = {
    "L1": ["f1", "f2", "f4"],
    "L2": ["f2", "f3", "f4", "f5"],
    "L3": ["f2", "f4", "f6"]
}

input_links = ["f1", "f6"]

# Method 1 = 3 * 2 * total_links = n iteration
impacted_logical_links = []
for each_map in data:
    for each_bad_link in input_links:
        if each_bad_link in data[each_map]:
            impacted_logical_links.append(each_map)

print(impacted_logical_links)


