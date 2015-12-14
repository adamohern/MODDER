#python

import lx

if (lx.eval("query scriptsysservice userValue.isDefined ? komodo_working")==0 or 
	lx.eval('user.value komodo_working ?')=='' or 
	lx.eval('user.value komodo_working ?')=='None'):
		
    lx.eval("@{kit_KOMODO:scripts/komodo.setWorkingFile.py}");

try: 
    theFile = lx.eval('user.value komodo_working value:?');
    lx.eval('@{%s}' % theFile);
except:
    lx.out("komodo.runWorkingFile.py: Something went wrong with the working script.");
    lx.out("working script: " + lx.eval('user.value komodo_working value:?'));
