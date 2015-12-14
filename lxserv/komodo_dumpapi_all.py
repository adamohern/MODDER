#python

import lx, lxu, komodo.apidump as apidump

BLESS = "komodo.dumpAPI"

class CMD_CLASS(lxu.command.BasicCommand):
  
  def basic_Execute(self, msg, flags):
    reload (apidump)
    apidump.dump()

lx.bless(CMD_CLASS, BLESS)