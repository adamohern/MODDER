#python

import modo, re

for i in modo.Scene().selected:
    i.name = re.sub('abc','123',i.name)