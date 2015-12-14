#python

import lx, lxu, os

FILENAME = "symbols.html"
PREAMBLE = "<h1>lx.symbol:</h1>\n\n"

def symbolDump(fullpath):
        
    symbols = {}
    for i in dir(lx.symbol):
        symbols[i] = str(getattr(lx.symbol,i))
    
    output = PREAMBLE
    for k,v in sorted(symbols.iteritems()):
        output += '%s<br />\n\t%s\n\n<br /><br />' % (k,v)
        
    target = open(os.path.join(fullpath,FILENAME),'w')
    target.write(output)
    target.close()