#python

import re, os, shutil

KIT_PATH  = lx.eval("query platformservice alias ? {kit_mecco_sky_py:}")
PYTHON_TEMPLATE = os.join(KIT_PATH,'assets','snippets','blank.py')

lx.out('PYTHON_TEMPLATE: ' + PYTHON_TEMPLATE)

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

	dest = os.path.dirname(PYTHON_TEMPLATE) + snippetName

	try:
		lx.eval('select.filepath {%s} set' % PYTHON_TEMPLATE)
		lx.out('selected PYTHON_TEMPLATE ' + PYTHON_TEMPLATE)

		try:
			shutil.copyfile(PYTHON_TEMPLATE,dest)
			lx.out('successfully duplicated \'' + PYTHON_TEMPLATE + '\' to \'' + dest + '\'')

			try:
				lx.eval('file.open {%s}' % dest)
			except:
				lx.out('could not open \'' + dest + '\'')

		except:
			lx.out('could not duplicate prototype:\n \'' + PYTHON_TEMPLATE + '\' \nto:\n \'' + dest + '\'')
		
	except:
		lx.out('could  not select PYTHON_TEMPLATE ' + PYTHON_TEMPLATE)
	
except:
	lx.out('user abort')
