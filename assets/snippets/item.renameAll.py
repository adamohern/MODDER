#python

import modo, re

for i in modo.Scene().items():
    i.name = re.sub('abc','123',i.name)