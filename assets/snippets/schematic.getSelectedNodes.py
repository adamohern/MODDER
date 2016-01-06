#python

import modo

def nodes():
    
    """
    Returns the ID's of all currently selected schematic nodes.
    Note: This is a hack that changes selection states in order to build the list. An API equivalent would be better.
    """

    sel = modo.Scene().selected
    nodes = set()

    for i in sel:
        i.select(replace = True)
        nodes.add(lx.eval('schematic.node ?'))

    lx.eval('select.drop item')
    for i in sel:
        i.select()
        
    return list(nodes)