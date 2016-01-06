#python

def active_pass():
    """
    Returns the currently active pass in the active pass group.
    """

    passid = lx.eval('layer.active ? type:pass')

    if passid:
        return passid
    else:
        return False