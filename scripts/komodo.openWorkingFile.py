#python

if (lx.eval("query scriptsysservice userValue.isDefined ? komodo_working")==0 or 
	lx.eval('user.value komodo_working ?')=='' or 
	lx.eval('user.value komodo_working ?')=='None'):
		
    lx.eval("@{kit_KOMODO:scripts/komodo.setWorkingFile.py}");
    
try: 
    theFile = lx.eval('user.value komodo_working ?');
    lx.eval('file.open {%s}' % theFile);
except:
    lx.eval("dialog.setup style:warning")
    lx.eval("dialog.title {komodo: something went wrong}")
    lx.eval("dialog.msg {For some reason we couldn't open the working file.}")
    lx.eval("dialog.open")
    lx.eval('user.value komodo_working');