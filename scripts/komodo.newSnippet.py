#python

import modo, lx, os, traceback

KIT_ALIAS = 'kit_MODDER:assets/snippets'

def quickUserValue(valHandle,valType='string',nicename='',default=''):
    if lx.eval( 'query scriptsysservice userValue.isDefined ? %s' % valHandle)==0:
        lx.eval( 'user.defNew %s %s' % (valHandle,valType) )

    try:
        lx.eval( 'user.def %s username {%s}' % (valHandle,nicename) )
        lx.eval( 'user.def %s type %s' % (valHandle,valType) )
        lx.eval( 'user.value %s {%s}' % (valHandle,default) )
        lx.eval( 'user.value %s' % valHandle )
        return lx.eval('user.value %s value:?' % valHandle)
    except:
        return False

name = quickUserValue('tmp','string','Script Name','my_great_snippet')
if not os.path.splitext(name) == '.py':
    name = '.'.join((name,'py'))

target = lx.eval("query platformservice alias ? {%s}" % KIT_ALIAS)

try:
    lx.out("creating %s" % os.path.join(target,name))
    thefile = open(os.path.join(target,name),'w')
    thefile.write('#python\n\n')
    thefile.close()
    lx.eval('file.open {%s}' % os.path.join(target,name))
except:
    traceback.print_exc()
