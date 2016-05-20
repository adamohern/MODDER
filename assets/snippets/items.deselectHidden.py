#python

import modo

for i in modo.Scene().selected:
    if i.channel('visible').get() not in ['on', 'default']:
        i.deselect()
