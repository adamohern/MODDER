#python

import re
import lx
import os.path

def layerserviceRef():

    text = '<html>\n<body>\n'
    text += '<head><link rel="stylesheet" type="text/css" href="reset.css"><link rel="stylesheet" type="text/css" href="style.css"></head>'

    attributesArray = lx.eval('query layerservice "" ?')

    text += '<h1>layerservice (**depricated**):</h1>\n\n'
    text += '<p><em>query layerservice "" ?</em></p>'

    text += '<ul>\n'
    for attribute in attributesArray:
        text += '<li>'+attribute+'</li>\n'
    text += '</ul>\n'

    text += '</body>\n</html>'

    kit_path  = lx.eval("query platformservice alias ? {kit_MODDER:}")
    f = open(os.path.join(kit_path,'html','layerservice.html'),'w')
    fpath = os.path.abspath(f.name)

    try:
        f.write(text)
        lx.out('saved to %s' % fpath)
    except:
        lx.out('could not save to %s' % fpath)
