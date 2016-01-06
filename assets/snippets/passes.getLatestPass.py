#python

"""
Returns the most recently created pass in the active pass group.
"""

group = lx.eval('group.current ? pass')
if group:
    passes = [lx.eval('query sceneservice actionclip.id ? %s' %i)
              for i in xrange(lx.eval('query sceneservice actionclip.N ?'))]

    members = [x
               for x in lx.evalN('query sceneservice group.itemMembers ? {%s}' %group)
               if lx.eval('query sceneservice item.type ? {%s}' %x) == 'actionclip']

    if members:
        members.sort(key=lambda x: passes.index(x))
        lx.eval('layer.active {%s} type:pass' %members[-1])