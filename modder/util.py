#python

import lx



def random_color(h=None,s=None,v=None):
    """
    By Adam O'Hern
    Returns a random color using HSV.

    :param h: Fixed Hue. If None, a random hue will be used.
    :param s: Fixed Saturation. If None, a random saturation will be used.
    :param v: Fixed Value. If None, a random value will be used.
    """
    import colorsys, random

    h = random.random() if h == None else h
    s = random.random() if s == None else s
    v = random.random() if v == None else v

    return colorsys.hsv_to_rgb(h, s, v)


def quick_user_value(valHandle='modder_tmp',valType='string',nicename='String',default=''):
    """
    By Adam O'Hern
    Creates a new user value, requests that value of the user, then returns the result.
    """
    if lx.eval('query scriptsysservice userValue.isDefined ? %s' % valHandle) == 0:
        lx.eval('user.defNew %s %s' % (valHandle, valType))
    try:
        lx.eval('user.def %s username {%s}' % (valHandle, nicename))
        lx.eval('user.def %s type %s' % (valHandle, valType))
        lx.eval('user.value %s {%s}' % (valHandle, default))
        lx.eval('+user.value %s' % valHandle)
        return lx.eval('user.value %s value:?' % valHandle)
    except:
        return None

def get_imagesavers():
    """
    By The Foundry
    http://sdk.luxology.com/wiki/Snippet:Image_Savers

    Returns a list of available image savers. Each entry in the returned list
       is a tuple made up of the format's internal name, it's username and it's
       DOS type (extension).
    """
    host_svc = lx.service.Host()
    savers = []
    for x in range(host_svc.NumServers('saver')):
        saver = host_svc.ServerByIndex('saver', x)
        out_class = saver.InfoTag(lx.symbol.sSAV_OUTCLASS)
        if  (out_class == 'image' or out_class == 'layeredimage'):
            name = saver.Name()
            uname = saver.UserName()
            try:
                dostype = saver.InfoTag(lx.symbol.sSAV_DOSTYPE)
            except:
                dostype = ''
            savers.append((name, uname, dostype,))
    return savers
