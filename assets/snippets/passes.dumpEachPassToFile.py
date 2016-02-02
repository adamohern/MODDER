import modo
from os.path import splitext

"""
By Adam O'Hern for Mechanical Color

Quick script intended for exporting multi-pass files for render farm use.

Exports a separate file for each active pass in a given pass group. Files are saved
in the same folder as the parent scene file, and the name of the pass is appended
to the file name.

To avoid files overwriting themselves when rendered, the script also manually inserts
the pass name into the output path for each render output. Note that this only applys
to outputs that have a previously defined output path; others are ignored.

The output pattern can be optionally overridden.
"""

# Note that backslashes for Windows path names have to be escaped (\\). Mac/Linux paths should be fine as normal (/).
OUTPUT = 'X:\\path\\to\\destination\\filename'
PATTERN = '_<output>_<FFFF>'
PASS_GROUP = 'shots'

scene = modo.Scene()
group = scene.item(PASS_GROUP)
outputs = [i for i in scene.iterItems() if i.type == 'renderOutput']
passes = [i for i in group.itemGraph('itemGroups').forward() if i.type == lx.symbol.a_ACTIONCLIP and i.enabled]

if PATTERN:
    restorePat = scene.renderItem.channel('outPat').get()
    scene.renderItem.channel('outPat').set(PATTERN)

for pass_ in passes:
    pass_.actionClip.SetActive(1)

    restoreOut = []
    for output in outputs:
        if not output.channel('filename').get(): continue

        restoreOut.append(output.channel('filename').get())
        output.channel('filename').set(OUTPUT + '_' + pass_.name)

    splitpath = splitext(lx.eval('query sceneservice scene.file ? current'))
    lx.eval('scene.saveAs {%s_%s%s} $LXOB true' % (splitpath[0], pass_.name, splitpath[1]) )

    for i, output in enumerate(outputs):
        output.channel('filename').set(restoreOut[i])

if PATTERN:
    scene.renderItem.channel('outPat').set(restorePat)
