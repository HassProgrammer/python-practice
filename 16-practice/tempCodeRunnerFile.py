import re

# creating a pattern 222
mobile_pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# check with number
Khan = mobile_pattern.match("325-235-3255")

print(bool(Khan))