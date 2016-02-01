import modo, os.path

OUTPUT = 'R:\users\adam\output\EXR\studio_01'

group = modo.Scene().item('shots')

modo.Scene().renderItem.channel('outPat').set('_<output>_<FFFF>')

for action in [i for i in group.itemGraph('itemGroups').forward() if i.type == lx.symbol.a_ACTIONCLIP and i.enabled]:
    print 'Activate %s...' % (action.name)
    action.actionClip.SetActive(1)

    print '\tsetting output path/name:'
    for output in [i for i in modo.Scene().iterItems() if i.type == 'renderOutput']:
        output.channel('filename').set(OUTPUT + '_' + action.name)

    path = lx.eval('query sceneservice scene.file ? current')
    splitpath = os.path.splitext(path)
    path = '%s_%s%s' % (splitpath[0], action.name, splitpath[1])

    print '\tExporting "%s"...' % path
    lx.eval('scene.saveAs {%s} $LXOB true' % path )

    print '\tSuccess.'
    print '\t++++'
