#python

import modo, re

old_sub = r'R:\users\somebody\someplace'
new_sub = r'C:\Users\somebody\Dropbox\someplace'

old_sub = re.escape(old_sub)
new_sub = new_sub.replace('\\',r'\\')

for item in modo.Scene().iterItems('renderOutput'):
    old = item.channel('filename').get()
    new = re.sub(old_sub, new_sub, old)
    print old
    print new + "\n"
    item.channel('filename').set(new)
