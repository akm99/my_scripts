import re
from pprint import pprint
shakes = "20160502"
test = "(?P<Year>\d{4})(?P<Month>\d{2})(?P<Day>\d{2})"
res = re.match (test, shakes)

pprint("The timestammp in shakes is coverted to: {}:{}:{}".format((res.group(1)),(res.group(2)),(res.group(3))))
