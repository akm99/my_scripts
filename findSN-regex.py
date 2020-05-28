import re

with open("show-version") as f:
    output = f.read()
#str = "cat:isco Nexus9000 C9504 (4 Slot) Chassis (Supervisor Module)  Intel(R) Xeon(R) CPU E5-2403 0 @ 1.80GHz with 16400780 kB of memory. Processor Board ID SAL1814PQ4K testing"

newpatt = 'Processor\s+Board\s+ID.*'
pattern = r"[A-Z]{3}[0-9]{4}[A-Z0-9]{4}"
patt = r"\b/[A-Z]{3}[0-9]{4}[A-Z0-9]{4}\b/"
word = r"\w\w\w\w\w\w\w\w\w\w\w"
ser = r"[A-Z]{3}[0-9]{4}[A-Z0-9]{4}"

#The 'r' in front tells Python the expression is a raw string. In a raw string, escape sequences are not parsed. For example, '\n' is a single newline character. But, r'\n' would be two characters: a backslash and an 'n'.


match = re.search(ser , output)

if match:
    print("The serial number is: {}".format(match.group()))

