#python

# usage:
# @sky.quickUserVal.py valueHandle dataType {nice name} defaultValue

args = lx.args()

valHandle = args[0] if len(args) == 1 else 'sky_tmp'
valType = args[1] if len(args) == 2 else 'string'
nicename = args[2] if len(args) == 3 else 'Script Name'
default = args[3] if len(args) == 4 else ''

if lx.eval('query scriptsysservice userValue.isDefined ? %s' % valHandle) == 0:
    lx.eval('user.defNew %s %s' % (valHandle, valType))
try:
    lx.eval('user.def %s username {%s}' % (valHandle, nicename))
    lx.eval('user.def %s type %s' % (valHandle, valType))
    lx.eval('user.value %s {%s}' % (valHandle, default))
    lx.eval('+user.value %s' % valHandle)
    val = lx.eval('user.value %s value:?' % valHandle)
    lx.out(valHandle + " = " + val)
except:
    lx.out('Uh oh.')
