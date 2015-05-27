#python

import lx,lxu
import os.path

def lxuObject():
	interrogate = ['','utils']

	text = '<html>\n<body>\n'
	text += '<head><link rel="stylesheet" type="text/css" href="style.css"></head>'

	for k in interrogate:

		#lx.out(k)

		text += '<h1>dir(%s)</h1>\n\n' % k

		text += '<ul>\n'

		if k == '':
			kids = dir(lxu)
		else:
			kids = dir(getattr(lxu,k))

		for i in kids:
			text += '\t<li>%s</li>\n' % i
		text += '</ul>\n\n'

	
	text += '</body>\n</html>\n'
		
	kit_path  = lx.eval("query platformservice alias ? {kit_mecco_sky_py:}")
	f = open(os.path.join(kit_path,'ref','lxuObject.html'),'w')
	fpath = os.path.abspath(f.name)
	
	try:
		f.write(text)
		lx.out('saved to %s' % fpath)
	except:
		lx.out('could not save to %s' % fpath)
		
	lx.eval('file.open {%s}' % fpath)