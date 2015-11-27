#python

import lx, lxu

NAME_CMD = "symbolsearch"

class CMD_DUI(lxu.command.BasicCommand):
  
  def __init__(self):
    lxu.command.BasicCommand.__init__(self)
    self.dyna_Add('search', lx.symbol.sTYPE_STRING)
  
  def basic_Execute(self, msg, flags):
    text = self.dyna_String(0)
    
    # Create a dict of all symbols and their values
    dict = {str( getattr( lx.symbol, i) ) : i for i in dir(lx.symbol) }
    # Filter for keyword
    results = [(k, v) for k, v in dict.items() if (
        text.lower() in k.lower() or
        text.lower() in v.lower()
      )]
    for r in results:
      lx.out('%s\n%s' % (r[1],r[0]))

        
      
lx.bless(CMD_DUI, NAME_CMD)