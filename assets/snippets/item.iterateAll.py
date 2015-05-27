#python

itemCount = lx.eval("query sceneservice item.n ? all")
lx.out('renaming %s items in scene...' % itemCount)

for i in range(itemCount):
	id = lx.eval('query sceneservice item.id ? %s' % i)
	type = lx.eval('query sceneservice item.type ? %s' % i)
	name = lx.eval('query sceneservice item.name ? %s' % i)
	
	lx.out('renaming %s item "%s" with "%s"...' % (type,name,id))
	try:
		lx.eval('select.item {%s}' % id)
		lx.eval('item.name {%s} {%s}' % (id,type))
		lx.out('(success)')
	except:
		lx.out('--FAILURE--')