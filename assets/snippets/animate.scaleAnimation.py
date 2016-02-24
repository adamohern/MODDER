#python

import modo

SCALE_FACTOR = 4

scene_out = lx.eval('time.range scene out:?')

lx.eval('time.range scene out:{}'.format(scene_out * SCALE_FACTOR))
lx.eval('time.range current out:{}'.format(scene_out * SCALE_FACTOR))

lx.eval('select.drop item')
lx.eval('select.itemType anim:true')
lx.eval('item.selectChannels anim')

for item in modo.Scene().selected:
    for channel in item.channels():
        lx.eval('select.keyRange item:{} channel:{} inputMin:-99999 inputMax:99999 outputMin:-99999 outputMax:99999 mode:"add"'.format(item.id, channel.index))

    transformItems = [i for i in item.itemGraph('xfrmCore').reverse() if i.type in ('scale', 'rotation', 'translation')]
    for transformItem in transformItems:
        for channel in transformItem.channels():
            lx.eval('select.keyRange item:{} channel:{} inputMin:-99999 inputMax:99999 outputMin:-99999 outputMax:99999 mode:"add"'.format(transformItem.id, channel.index))

lx.eval('key.scale {} start 0.0 input false'.format(SCALE_FACTOR))
lx.eval('select.time 0.0')

lx.eval('select.drop item')
