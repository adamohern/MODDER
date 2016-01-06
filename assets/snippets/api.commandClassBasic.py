#python

import lx, lxu.command

BLESS = "world.hello"

class commandClass(lxu.command.BasicCommand):
	def basic_Execute(self, msg, flags):
        lx.out("Hello world.")
		
lx.bless(commandClass, BLESS)