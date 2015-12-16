#python

import lx, os

def imagesaversRef(path,filename="imagesavers",ext="html"):
    fullpath = os.path.join(path,".".join([filename,ext]))
    target = open(fullpath,'w')
    target.write("<html>")
    target.close()
    
    target = open(fullpath,'a')
    savers = get_imagesavers()
    target.write("<head>\n")
    target.write('<link rel="stylesheet" type="text/css" href="reset.css">'+"\n")
    target.write('<link rel="stylesheet" type="text/css" href="style.css">'+"\n")
    target.write('</head>'+"\n")
    target.write('<body>'+"\n")
    target.write("<ul>\n")
    for saver in savers:
        target.write("\t<li><strong>%s:</strong> %s (.%s)</li>\n" % (saver[0],saver[1],saver[2]))
    target.write("</ul>\n</body>\n</html>")
    target.close()

def get_imagesavers():
        """ Returns a list of available image savers. Each entry in the returned list
             is a tuple made up of the format's internal name, it's username and it's
             DOS type (extension).
 
     """
        host_svc = lx.service.Host()
        savers = []
        for x in range(host_svc.NumServers('saver')):
                saver = host_svc.ServerByIndex('saver', x)
                out_class = saver.InfoTag(lx.symbol.sSAV_OUTCLASS)
                if    (out_class == 'image' or out_class == 'layeredimage'):
                        name = saver.Name()
                        uname = saver.UserName()
                        try:
                                dostype = saver.InfoTag(lx.symbol.sSAV_DOSTYPE)
                        except:
                                dostype = ''
                        savers.append((name, uname, dostype,))
        return savers