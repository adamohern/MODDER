#python

import re, os;

if lx.eval("query scriptsysservice userValue.isDefined ? sky_working")==0:
    lx.eval( 'user.defNew sky_working string' );
    lx.eval( 'user.def sky_working username value:{}' );

lx.eval("dialog.setup fileOpenMulti");
lx.eval("dialog.title [Sky_Py: select working script]");
lx.eval("dialog.fileTypeCustom format:[sml] username:[sky_working_seldialog] loadPattern:[*.py;*.lxm;*.pl;*.lua] saveExtension:[lxo]");
lx.eval("dialog.open");

try:
    fileSelection = lx.eval("dialog.result ?");

    lx.eval('user.value sky_working {%s}' % fileSelection);
    lx.out("Sky_Py: working file set to " + fileSelection);

    lx.eval('select.attr {sky_py.58367595996:sheet/0} set');
    lx.eval('attr.label {run: %s}' % os.path.basename(fileSelection));
except:
    lx.out("sky.setWorkingFile.py: user aborted");
