#python

if (lx.eval("query scriptsysservice userValue.isDefined ? sky_working")==0 or 
	lx.eval('user.value sky_working ?')=='' or 
	lx.eval('user.value sky_working ?')=='None'):
		
    lx.eval("@{kit_mecco_sky_py:scripts/sky.setWorkingFile.py}");
    
try: 
    theFile = lx.eval('user.value sky_working ?');
    lx.eval('file.open {%s}' % theFile);
except:
    lx.eval("dialog.setup style:warning")
    lx.eval("dialog.title {sky_py: something went wrong}")
    lx.eval("dialog.msg {For some reason we couldn't open the working file.}")
    lx.eval("dialog.open")
    lx.eval('user.value sky_working');