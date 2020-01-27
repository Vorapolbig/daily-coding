# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

import re

address = "1.1.1.1"
replace = re.sub(r'[.]','[.]',address)
print(replace)

