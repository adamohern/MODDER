import modo

ignore = [
modo.Scene().renderItem,
modo.Scene().sceneItem
]

ignoreTypes = [
'translation',
'rotation',
'scale'
]

for i in modo.Scene().items():
	if i in ignore or i.selected or i.type in ignoreTypes:
		continue	
	try:
		modo.Scene().removeItems(i)
	except:
		continue