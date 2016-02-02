import modo, os.path

# Note that backslashes for Windows path names have to be escaped (\\). Mac/Linux paths should be fine as normal (/).
OUTPUT = 'X:\\path\\to\\destination\\filename'
PATTERN = '_<output>_<FFFF>'
PASS_GROUP = 'shots'

scene = modo.Scene()
group = scene.item(PASS_GROUP)

restorePat = scene.renderItem.channel('outPat').get()
scene.renderItem.channel('outPat').set(PATTERN)

outputs = [i for i in scene.iterItems() if i.type == 'renderOutput']

for action in [i for i in group.itemGraph('itemGroups').forward() if i.type == lx.symbol.a_ACTIONCLIP and i.enabled]:
    print '\n\nActivate %s...' % (action.name)
    action.actionClip.SetActive(1)

    print '\tSetting output paths:'
    restoreOut = []
    for output in outputs:
        restoreOut.append(output.channel('filename').get())
        output.channel('filename').set(OUTPUT + '_' + action.name)

    path = lx.eval('query sceneservice scene.file ? current')
    splitpath = os.path.splitext(path)
    path = '%s_%s%s' % (splitpath[0], action.name, splitpath[1])

    print '\tExporting "%s"...' % path
    lx.eval('scene.saveAs {%s} $LXOB true' % path )

    print '\tRestoring output paths...'
    for i, output in enumerate(outputs):
        output.channel('filename').set(restoreOut[i])

    print '\tSuccess.'
    print '\t++++'

scene.renderItem.channel('outPat').set(restorePat)
