#python

#!/usr/bin/env python
 
################################################################################
#
# FormCommandList.py
#
#
# Description: A simple example of creating a 'Form Command List' custom command,
#              see http://sdk.luxology.com/wiki/LXfVALHINT_FORM_COMMAND_LIST_(index)#C73
#              for more info
#
#
# Usage: Enter the command name into a form as a query ie
#        replace.me ?
#
# Last Update: 22:41 30/04/13
#
################################################################################
 
import lx
import lxifc
import lxu.command
 
# This is our list of commands. You can generate this list any way you like
# including procedurally - in fact the most common use case for a Form Command
# List would be to generate a list of commands to show in a form procedurally.
cmdlist = ['file.open {kit_mecco_sky_py:assets/snippets/api.commandClass.py}',
           # A string in the list that starts with a dash (hyphen) followed by 
           # a space becomes a line divider in the form.
           '- ',
           'item.color',
           'item.comment',
           # A string in the list that starts with a dash (hyphen) followed by 
           # a space and then a string becomes a labelled divider in the form.
           '- I am a Divider',
           'item.create',
           'item.tagAdd']
 
 
# The UIValueHints object that returns the items in the list of commands
# to the form.
class MycommandsList(lxifc.UIValueHints):
    def __init__(self, items):
        self._items = items
 
    def uiv_Flags(self):
        # This is a series of flags, although in this case we're only returning 
        # ''fVALHINT_FORM_COMMAND_LIST'' to indicate that there's a Form Command 
        # List implemented.
        return lx.symbol.fVALHINT_FORM_COMMAND_LIST
 
    def uiv_FormCommandListCount(self):
        return len(self._items)
 
    def uiv_FormCommandListByIndex(self,index):
        return self._items[index]
 
 
# This is the command that will be replaced by the commands in MyCommandsList
# in any form in which it's embedded as a query. It requires a queriable 
# attribute/argument but neither of the command's ''cmd_Execute'' or ''cmd_Query'' methods
# need to be implemented as neither will be called when the argument is queried 
# in a form.  You can still implement them, but they will only be used when 
#executing/querying from scripts or CHist etc.
class CmdMyFormCommandsList(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        # Add an integer attribute. The attribute is required
        self.dyna_Add('cmds', lx.symbol.sTYPE_INTEGER)
        # mark it as queriable
        self.basic_SetFlags(0, lx.symbol.fCMDARG_QUERY)
 
    def arg_UIValueHints(self, index):
        # create an instance of our commands list object passing it the
        # list of commands.
        if index == 0:
            return MycommandsList(cmdlist)
 
    def cmd_Execute(self,flags):
        # dummy execute method
        pass
 
    def cmd_Query(self,index,vaQuery):
        # dummy query method
        pass
 
# 'blessing' the class registers it as a plugin command. The command string, the
# string that you embed as a query in a form is the second argument to bless(), ie
# 'replace.me'
lx.bless(CmdMyFormCommandsList, "sky.snippetsList")