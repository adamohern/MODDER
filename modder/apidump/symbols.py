#python

import lx, lxu, os

FILENAME = "symbols.html"
PREAMBLE = "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"reset.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"></head><body><h1>lx.symbol:</h1>\n\n"

def symbolDump(fullpath):
        
    symbols = {}
    for i in dir(lx.symbol):
        symbols[i] = str(getattr(lx.symbol,i))
    
    output = PREAMBLE
    output += "<ul>"
    for k,v in sorted(symbols.iteritems()):
        output += '<li><strong>%s</strong><br />\n"%s"</li>\n\n' % (k,v)
    output += "</ul></body></html>"
        
    target = open(os.path.join(fullpath,FILENAME),'w')
    target.write(output)
    target.close()