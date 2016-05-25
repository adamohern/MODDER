#python

import re
import lx
import os.path

def sceneserviceRef():

    text = '<html>\n<body>\n'
    text += '<head><link rel="stylesheet" type="text/css" href="reset.css"><link rel="stylesheet" type="text/css" href="style.css"></head>'

    attributesArray = lx.eval('query sceneservice "" ?')

    text += '<h1>sceneservice:</h1>\n\n'
    text += '<p><em>query sceneservice "" ?</em></p>'

    text += '<ul>\n'
    for attribute in attributesArray:
        text += '<li>'+attribute+'</li>\n'
    text += '</ul>\n'

    text += '\n\n<h2>attributes:</h2>\n\n'

    for attribute in attributesArray:
        attributesArrayList = '<ul>\n'

        #if (attribute.startswith('attribute.')) and (attribute.startswith('attribute.argArgTypes') == 0) and (attribute.startswith('attribute.toggleArg') == 0):
        query = '!!query sceneservice %s ?' % (attribute)
        try:
            q = lx.eval(query)
            if isinstance(q,(list,tuple)):
                attributesArrayList += '\t<li><strong>%s</strong><br />\n<span class="light">query sceneservice %s ?</span>\n\t\t<ul>' % (attribute,attribute)
                for v in q:
                    if v == '': v = '(n/a)'
                    try:
                        attributesArrayList += '\n\t\t\t<li>%s</li>\n' % (v)
                    except:
                        attributesArrayList += '\n\t\t\t<li>(error)</li>'
                attributesArrayList += '\n\t\t</ul>\n\t</li>\n'
            else:
                try:
                    if (str(q) != '') and (str(q) != 'None') and (str(q) != '0'):
                        attributesArrayList += '\t<li><strong>'+attribute+':</strong><br />'
                        attributesArrayList += str(q)+'</li>\n'
                except:
                    attributesArrayList += '<!--error reading %s--></li>\n' % attribute
        except:
            lx.out('FAILED: %s' % query)


        attributesArrayList += '</ul>\n'

        if attributesArrayList != '<ul></ul>\n':
            text += attributesArrayList+'\n\n\n'

    text += '</body>\n</html>'

    kit_path  = lx.eval("query platformservice alias ? {kit_MODDER:}")
    f = open(os.path.join(kit_path,'html','sceneservice.html'),'w')
    fpath = os.path.abspath(f.name)

    try:
        f.write(text)
        lx.out('saved to %s' % fpath)
    except:
        lx.out('could not save to %s' % fpath)
