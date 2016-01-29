#python

import modo

group = modo.Scene().item('shots')
for action in [i for i in group.itemGraph('itemGroups').forward() if i.type == lx.symbol.a_ACTIONCLIP]:
#	action.actionClip.SetActive(0)
	print '%s (%s)' % (action.name,action.enabled)