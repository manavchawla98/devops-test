#!/usr/bin/env python3
import string
import random

all_char=string.ascii_uppercase + string.ascii_lowercase
digits=string.digits
random_string=''

random_string=''.join(random.choice(all_char) for _ in range (10))

random_string+=''.join(random.choice(digits) for _ in range(3))

string_reversed=random_string[::-1]

with open('out.txt','w') as outfile:
	outfile.write(random_string + '\n' + string_reversed)
	outfile.close()
