#python

import lx, layers, ptags

def mode():
    """Returns the current selection mode as any of the following strings:
    vertex;edge;polygon;item;pivot;center;ptag
    """
    
    modes = 'vertex;edge;polygon;item;pivot;center;ptag'
    for mode in modes.split(';'):
        if lx.eval('select.typeFrom %s;%s ?' % (mode, modes)): 
            return mode
    return False

def poly_expand_by_ptag(i_POLYTAG=lx.symbol.i_POLYTAG_MATERIAL):
    """Expands a polygon selection to include all polys with matching tags in currently active layer(s).
    Useful for expanding a selection to include all polys with a given material or part tag, for example.
    """

    tags = ptags.from_polys(i_POLYTAG)

    for tag in tags:
        lx.eval('select.polygon add part face %s' % tag)