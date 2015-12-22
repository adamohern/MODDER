#python

import lx, modo, polys

def from_polys(i_POLYTAG = lx.symbol.i_POLYTAG_MATERIAL,implicit=False,connected=False):
    """Returns a list of all pTags for currently selected polys in all active layers.
    
    :param i_POLYTAG: type of tag to return (str), e.g. lx.symbol.i_POLYTAG_MATERIAL
    :param implicit: include polys adjacent to edge or vertex selection as appropriate (bool)
    :param connected: extend selection to connected polys (bool)
    """
    
    r = set()
    pp = polys.selected(connected)
    if pp:
        for p in pp:
            r.add(p.getTag(i_POLYTAG))
    return list(r)