#python

import re, os, shutil

KIT_PATH = lx.eval("query platformservice alias ? {kit_mecco_sky_py:}")
PYTHON_TEMPLATE = os.path.join(KIT_PATH, 'assets', 'snippets', 'blank.py')

lx.out('PYTHON_TEMPLATE: ' + PYTHON_TEMPLATE)

try:
	lx.eval("dialog.setup fileSave");
	lx.eval("dialog.title [Sky_Py: new script]");
	lx.eval("dialog.fileTypeCustom format:[sml] username:{Python (.py)} loadPattern:[*.py;*.lxm;*.pl;*.lua] saveExtension:[py]");
	lx.eval("dialog.open");

	try:
		scriptPath = lx.eval("dialog.result ?");
	except:
		lx.out('user abort')
		sys.exit
		
	lx.out('script path: ' + scriptPath)
	
	#Remove .py and add it back again just in case user
	#forgets to include it when typing the name.
	scriptPath = re.sub('\.py', '', scriptPath)
	scriptPath = scriptPath + '.py'

	dest = scriptPath

	try:
		lx.eval('select.filepath {%s} set' % PYTHON_TEMPLATE)
		lx.out('selected PYTHON_TEMPLATE ' + PYTHON_TEMPLATE)

		try:
			shutil.copyfile(PYTHON_TEMPLATE,dest)
			lx.out('successfully duplicated \'' + PYTHON_TEMPLATE + '\' to \'' + dest + '\'')
			
			try:
				if lx.eval("query scriptsysservice userValue.isDefined ? sky_working")==0:
					lx.eval( 'user.defNew sky_working string' );
					lx.eval( 'user.def sky_working username value:{}' );
				
				lx.eval('user.value sky_working {%s}' % scriptPath);
				lx.out("Sky_Py: working file set to " + scriptPath);

				lx.eval('select.attr {sky_py.58367595996:sheet/0} set');
				lx.eval('attr.label {run: %s}' % os.path.basename(scriptPath));
				
			except:
				lx.out("sky.newScript.py: user aborted");
			
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
