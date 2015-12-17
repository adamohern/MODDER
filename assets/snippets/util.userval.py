#python

def quickUserValue(valHandle,valType='string',nicename='',default=''):
	if lx.eval( 'query scriptsysservice userValue.isDefined ? %s' % valHandle)==0:
		lx.eval( 'user.defNew %s %s' % (valHandle,valType) )
	
	try:
		lx.eval( 'user.def %s username {%s}' % (valHandle,nicename) )
		lx.out('user.def %s type %s' % (valHandle,valType))
		lx.eval( 'user.def %s type %s' % (valHandle,valType) )
		lx.eval( 'user.value %s {%s}' % (valHandle,default) )
		lx.eval( 'user.value %s' % valHandle )
		return lx.eval('user.value %s value:?' % valHandle)
	except:
		return False
		
lx.out(quickUserValue('Something fun.'))