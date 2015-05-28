#python

import re, os, shutil

def basename(string):
    basename = re.sub('^.*[\/\\\]','',string);
    lx.out('basename: ' + basename);
    return basename;

kit_path  = lx.eval("query platformservice alias ? {kit_mecco_sky_py:}")
proto = os.join(kit_path,'assets','snippets','blank.py')

lx.out('proto: '+proto)

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
		
	lx.out('script path: '+scriptPath)
	
	#Remove .py and add it back again just in case user
	#forgets to include it when typing the name.
	scriptPath = re.sub('\.py','',scriptPath)
	scriptPath = scriptPath + '.py'

	dest = scriptPath

	try:
		lx.eval('select.filepath {%s} set' % proto)
		lx.out('selected proto '+proto)

		try:
			shutil.copyfile(proto,dest)
			lx.out('successfully duplicated \'' + proto + '\' to \'' + dest + '\'')
			
			try:
				if lx.eval("query scriptsysservice userValue.isDefined ? sky_working")==0:
					lx.eval( 'user.defNew sky_working string' );
					lx.eval( 'user.def sky_working username value:{}' );
				
				lx.eval('user.value sky_working {%s}' % scriptPath);
				lx.out("Sky_Py: working file set to " + scriptPath);

				lx.eval('select.attr {sky_py.58367595996:sheet/0} set');
				lx.eval('attr.label {run: %s}' % basename(scriptPath));
				
			except:
				lx.out("sky.newScript.py: user aborted");
			
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
