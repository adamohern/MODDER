import modo

ignore = [
modo.Scene().renderItem,
modo.Scene().sceneItem
]

for i in modo.Scene().iterItems():
	if i in ignore or i.selected:
		continue
	modo.Scene().removeItems(i)
