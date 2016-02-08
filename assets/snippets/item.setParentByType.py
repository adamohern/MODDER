import modo

for i in modo.Scene().iterItems():
    if i.type == 'txtrLocator':
        i.setParent('Texture Group')
