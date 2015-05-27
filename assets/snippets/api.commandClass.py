#python

#Must be inside a folder called 'lxserv' somewhere in a MODO search path.

import lx
import lxu.command
import traceback

class myGreatCommand(lxu.command.BasicCommand):
    
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        
		#command accepts an argument
        self.dyna_Add('arg1', lx.symbol.sTYPE_STRING) #or sTYPE_FLOAT
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)
		
	def cmd_Flags (self):
		#make the command undoable
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO
        
    def CMD_EXE(self, msg, flags):
		if arg1:
			arg1 = self.dyna_String(0, 0.0)
			lx.out('arg1: %s' % arg1)
		
	def basic_Execute(self, msg, flags):
        try:
            self.CMD_EXE(msg, flags)
        except Exception:
            lx.out(traceback.format_exc())
		
    def basic_Enable(self,msg):
        return True
        
lx.bless(myGreatCommand, "mecco.myGreatCommand")