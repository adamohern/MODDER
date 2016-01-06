#python

import modo

def nodes():
    sel = modo.Scene().selected
    nodes = set()

    for i in sel:
        i.select(replace = True)
        nodes.add(lx.eval('schematic.node ?'))

    lx.eval('select.drop item')
    for i in sel:
        i.select()
        
    return list(nodes)

def align_left(nodes):

    x_list = [lx.eval('schematic.nodePosition %s x:?' % n) for n in nodes]
    y_list = [lx.eval('schematic.nodePosition %s y:?' % n) for n in nodes]

    for i,n in enumerate(nodes):
        lx.eval('schematic.nodePosition %s x:%s y:%s' % ( n, min(x_list), y_list[i]) )
        
def distribute_vertical(nodes):
    
    x_list = [lx.eval('schematic.nodePosition %s x:?' % n) for n in nodes]
    y_list = [lx.eval('schematic.nodePosition %s y:?' % n) for n in nodes]
    
    spread = max(y_list) - min(y_list)
    q = spread / (len(y_list) - 1)
    
    nodes_sorted = [n for (y,n) in sorted(zip(y_list,nodes))]
    x_sorted = [x for (y,x) in sorted(zip(y_list,x_list))]
    y_sorted = sorted(y_list)
    
    y = y_sorted[0]
    for i,n in enumerate(nodes_sorted):
        lx.eval('schematic.nodePosition %s x:%s y:%s' % ( n, x_sorted[i], y_sorted[0] + q * i ))
    
    
align_left(nodes())
distribute_vertical(nodes())