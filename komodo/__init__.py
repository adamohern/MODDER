#python

import lx

def userValue(valHandle='komodo_tmp',valType='string',nicename='String',default=''):
    if lx.eval('query scriptsysservice userValue.isDefined ? %s' % valHandle) == 0:
        lx.eval('user.defNew %s %s' % (valHandle, valType))
    try:
        lx.eval('user.def %s username {%s}' % (valHandle, nicename))
        lx.eval('user.def %s type %s' % (valHandle, valType))
        lx.eval('user.value %s {%s}' % (valHandle, default))
        lx.eval('+user.value %s' % valHandle)
        return lx.eval('user.value %s value:?' % valHandle)
    except:
        return 0