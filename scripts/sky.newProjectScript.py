#python

import lx, re, sky, shutil
from os.path import join
from os.path import dirname

DEFAULT_SCRIPT_NAME = ""
USER_VAL_NICENAME = "Script Name"
USER_VAL_HANDLE = "sky.scriptName"
KIT_PATH  = lx.eval("query platformservice alias ? {kit_mecco_sky_py:}")
SCRIPT_TEMPLATE = join(KIT_PATH,'assets','snippets','blank.py')



lx.out('script template: ' + SCRIPT_TEMPLATE)

filepath = lx.eval('query sceneservice scene.file ? current')
path = dirname(filepath)

name = sky.userValue(USER_VAL_HANDLE,'string',USER_VAL_NICENAME,DEFAULT_SCRIPT_NAME)
name = re.sub('\.py$','',name)
name = name + '.py'

dest = join(path,name)
lx.out('script destination: ' + dest)

try:
    lx.eval('select.filepath {%s} set' % SCRIPT_TEMPLATE)
    lx.out('selected SCRIPT_TEMPLATE ' + SCRIPT_TEMPLATE)

    try:
        shutil.copyfile(SCRIPT_TEMPLATE,dest)
        lx.out('successfully duplicated:\n\'' + SCRIPT_TEMPLATE + '\' \nto:\n \'' + dest + '\'')

        try:
            lx.eval('file.open {%s}' % dest)
        except:
            lx.out('could not open \'' + dest + '\'')

    except:
        lx.out('could not duplicate:\n \'' + SCRIPT_TEMPLATE + '\' \nto:\n \'' + dest + '\'')

except:
    lx.out('could  not select SCRIPT_TEMPLATE ' + SCRIPT_TEMPLATE)
