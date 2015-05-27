#!/usr/bin/env python
 
################################################################################
#
# formpopUpList.py
#
# Version: 1.000
#
# Description: Example custom command that displays a pop-up list choice for
#              setting it's attribute/argument.
#
#
# Usage: choose.me ?snippets:string
#
# Last Update: 13:20 01/05/13
#
################################################################################
 
import lx
import lxifc
import lxu.command

from os import listdir
from os.path import join
from os.path import dirname

import re

 
# The UIValueHints class we'll be using to manage the list and it's items
class projectScriptListerPopup(lxifc.UIValueHints):
    def __init__(self, path):
        listItemHandles = []
        listItemNames = []
        
        if path == 0:
            listItemHandles.append('unsaved')
            listItemNames.append('(unsaved document)')
            
        if path:
            filenames = listdir(path)

            # regex = re.compile(r'^\.')
            regex = re.compile('\.py$')
            listItemHandles = [i for i in filenames if regex.search(i)]
            listItemNames = [i for i in listItemHandles]
            
        listItemHandles.append('update')
        listItemNames.append('(update list)')

        # the list we'll be using to populate the example pop-up. Note that it's a list
        # of two tuples. The first tuple contains the 'InternalNames' of the items and
        # the second contains the 'friendly' or 'UserNames'.
        # Adam: Since we're using filenames, the 'friendly' names are the same as the
        # actual filenames, so we just use the same list twice.
        self._items = [listItemHandles,listItemNames]

    def uiv_Flags(self):
        # This can be a series of flags, but in this case we're only returning
        # ''fVALHINT_POPUPS'' to indicate that we just need a straight pop-up
        # List implemented.
        return lx.symbol.fVALHINT_POPUPS
 
    def uiv_PopCount(self):
        # returns the number of items in the list
        return len(self._items[0])
 
    def uiv_PopUserName(self,index):
        # returns the Username of the item at ''index''
        return self._items[1][index]
 
    def uiv_PopInternalName(self,index):
        # returns the internal name of the item at ''index' - this will be the
        # value returned when the custom command is queried
        return self._items[0][index]
 
 
# The custom command class that implements a list attribute/argument
class projectScriptListerCmd(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        # Add a string attribute. Note: this could also be an integer if the list
        # is static rather than dynamic and ''TextValueHints'' are used. Currently
        # ''TextValueHints'' aren't implemented in the python API so it's
        # adviseable to use a string attribute.
        self.dyna_Add('project scripts', lx.symbol.sTYPE_STRING)
        # Set the attribute's queriable flag
        self.basic_SetFlags(0, lx.symbol.fCMDARG_QUERY)
 
 
    def arg_UIValueHints(self, index):
        # create an instance of our pop-up list object passing it the
        # list of commands.
        filepath = lx.eval('query sceneservice scene.file ? current')
        if index == 0:
            if filepath:
                path = dirname(filepath)
            else:
                path = 0
            return projectScriptListerPopup(path)
        else:
            return 0
 
    def cmd_Execute(self,flags):
        # in the execute method we're going to store the current value of our
        # attribute so that it can be retrieved by the query method later. There's
        # no way to permanently store this information inside the command class
        # itself as the command is created & destroyed between each use. Normally
        # we'd want to be using persistent storage but for simplicity in this
        # example we'll use a UserValue.
        if self.dyna_IsSet(0):
            if self.dyna_String(0) == 'update':
                lx.out('Update Code Goes Here.')
            elif self.dyna_String(0) == 'unsaved':
                lx.out('Unsaved document.')
            else:
                filepath = lx.eval('query sceneservice scene.file ? current')
                path = dirname(filepath)
                lx.eval('@{'+path+'/%s}' % self.dyna_String(0))
 
    def cmd_Query(self,index,vaQuery):
        # In the query method we need to retrieve the value we stored in the execute
        # method and add it to a ValueArray object to be returned by the query.
        va = lx.object.ValueArray(vaQuery)
        
        if index == 0:
            # retrieve the value we stored earlier and add it to the ValueArray
            va.AddString(self.dyna_String(0))
        return lx.result.OK
 
# bless() the command to register it as a plugin
lx.bless(projectScriptListerCmd, "sky.projectScriptLister")