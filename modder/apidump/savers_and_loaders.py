#python

import os, lx

def savers_and_loaders_dump(path,filename="savers_and_loaders",ext="html"):
    fullpath = os.path.join(path,".".join([filename,ext]))
    target = open(fullpath,'w')
    target.write("<html>")
    target.close()
    
    target = open(fullpath,'a')
    savers = get_savers()
    loaders = get_loaders()
    
    target.write("<head>\n")
    target.write('<link rel="stylesheet" type="text/css" href="reset.css">'+"\n")
    target.write('<link rel="stylesheet" type="text/css" href="style.css">'+"\n")
    target.write('</head>'+"\n")
    target.write('<body>'+"\n")
    target.write('<h1>Savers</h1>'+"\n")
    target.write("<ul>\n")
    for saver in savers:
        target.write("\t<li><strong>%s:</strong> %s (%s - *.%s)</li>\n" % (saver[0],saver[1],saver[3],saver[2]))
    target.write("</ul>\n")
    target.write('<h1>Loaders</h1>'+"\n")
    target.write("<ul>\n")
    for loader in loaders:
        target.write("\t<li><strong>%s:</strong> %s (*.%s)</li>\n" % (loader[0],loader[1],loader[2]))
    target.write("</ul>\n")
    target.write("</body>\n</html>")
    target.close()

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
            dostype = saver.InfoTag(lx.symbol.sLOD_DOSPATTERN)
        except:
            dostype = ''
        loaders.append((name, uname, dostype,))
    return loaders