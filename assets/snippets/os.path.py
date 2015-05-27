#python

import os.path

filepath = lx.eval('query sceneservice scene.file ? current')
if filepath:
	lx.out(os.path.dirname(filepath))
	lx.out(os.path.basename(filepath))
	lx.eval('file.open {%s}' % os.path.dirname(filepath))