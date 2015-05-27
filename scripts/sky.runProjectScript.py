#python

import os

arg = lx.arg()
filepath = lx.eval('query sceneservice scene.file ? current')

if filepath:
    pass
else:
    lx.eval('scene.save')
    filepath = lx.eval('query sceneservice scene.file ? current')
    
filedir = os.path.dirname(filepath)
scriptpath = os.path.join(filedir,arg)

try:
    lx.eval('@{%s}' % scriptpath)
except:
    lx.out('"%s" not valid.' % scriptpath)