#python

import re, os;

if lx.eval("query scriptsysservice userValue.isDefined ? komodo_working")==0:
    lx.eval( 'user.defNew komodo_working string' );
    lx.eval( 'user.def komodo_working username value:{}' );

lx.eval("dialog.setup fileOpenMulti");
lx.eval("dialog.title [Sky_Py: select working script]");
lx.eval("dialog.fileTypeCustom format:[sml] username:[komodo_working_seldialog] loadPattern:[*.py;*.lxm;*.pl;*.lua] saveExtension:[lxo]");
lx.eval("dialog.open");

try:
    fileSelection = lx.eval("dialog.result ?");

    lx.eval('user.value komodo_working {%s}' % fileSelection);
    lx.out("Sky_Py: working file set to " + fileSelection);

    lx.eval('select.attr {komodo.58367595996:sheet/0} set');
    lx.eval('attr.label {run: %s}' % os.path.basename(fileSelection));
except:
    lx.out("komodo.setWorkingFile.py: user aborted");
