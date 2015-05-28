#python

import lx

if (lx.eval("query scriptsysservice userValue.isDefined ? sky_working")==0 or 
	lx.eval('user.value sky_working ?')=='' or 
	lx.eval('user.value sky_working ?')=='None'):
		
    lx.eval("@{kit_mecco_sky_py:scripts/sky.setWorkingFile.py}");

try: 
    theFile = lx.eval('user.value sky_working value:?');
    lx.eval('@{%s}' % theFile);
except:
    lx.out("sky.runWorkingFile.py: Something went wrong with the working script.");
    lx.out("working script: " + lx.eval('user.value sky_working value:?'));
