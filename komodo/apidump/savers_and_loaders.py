#python

def get_savers():
    """ Returns a list of available image savers. Each entry in the returned list
        is a tuple made up of the format's internal name, it's username and it's
        DOS type (extension).
 
    """
    host_svc = lx.service.Host()
    savers = []
    for x in range(host_svc.NumServers('saver')):
        saver = host_svc.ServerByIndex('saver', x)
        out_class = saver.InfoTag(lx.symbol.sSAV_OUTCLASS)
        name = saver.Name()
        uname = saver.UserName()
        try:
            dostype = saver.InfoTag(lx.symbol.sSAV_DOSTYPE)
        except:
            dostype = ''
        savers.append((name, uname, dostype, out_class,))
    return savers

def get_loaders():
    host_svc = lx.service.Host()
    loaders = []
    for x in range(host_svc.NumServers('loader')):
        loader = host_svc.ServerByIndex('loader', x)
        name = loader.Name()
        uname = loader.UserName()
        try:
            dostype = saver.InfoTag(lx.symbol.sSAV_DOSTYPE)
        except:
            dostype = ''
        loaders.append((name, uname, dostype,))
    return loaders