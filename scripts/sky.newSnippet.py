#python

import re, os, shutil

kit_path  = lx.eval("query platformservice alias ? {kit_mecco_sky_py:}")
proto = os.join(kit_path,'assets','snippets','blank.py')

lx.out('proto: '+proto)

def pathname(string):
	pathname = re.findall('^.*[\/\\\]',string)
	try:
		lx.out('pathname: ' + pathname[0])
		return pathname[0]
	except:
		lx.out('no pathname found')
		return false

if lx.eval("query scriptsysservice userValue.isDefined ? sky_newSnippet")==0:
	lx.eval( 'user.defNew sky_newSnippet string' )
	lx.eval( 'user.def sky_newSnippet username value:{}' )

try:
	lx.eval('user.value sky_newSnippet value:{}')
	lx.eval('user.value sky_newSnippet')
	snippetName = lx.eval('user.value sky_newSnippet value:?')
	lx.out('filename: ' + snippetName)

	#Remove .py and add it back again just in case user
	#forgets to include it when typing the name.
	snippetName = re.sub('\.py','',snippetName)
	snippetName = snippetName + '.py'

	dest = pathname(proto) + snippetName

	try:
		lx.eval('select.filepath {%s} set' % proto)
		lx.out('selected proto '+proto)

		try:
			shutil.copyfile(proto,dest)
			lx.out('successfully duplicated \'' + proto + '\' to \'' + dest + '\'')

			try:
				lx.eval('file.open {%s}' % dest)
			except:
				lx.out('could not open \'' + dest + '\'')

		except:
			lx.out('could not duplicate prototype:\n \'' + proto + '\' \nto:\n \'' + dest + '\'')
		
	except:
		lx.out('could  not select proto '+proto)
	
except:
	lx.out('user abort')
