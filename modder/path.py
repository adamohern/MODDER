#python

import lx

def expand_alias(pathalias):
    return lx.eval("query platformservice alias ? {%s}" % pathalias)