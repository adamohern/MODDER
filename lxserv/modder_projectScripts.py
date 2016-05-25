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
from os.path import isfile

import os, re, time, inspect

""" Toggles """
DEBUG_MODE = 1

""" Strings """
NEW = "New Script"
REFRESH = "Refresh List"
UNSAVED = "..."
NONE = "..."
POPOVER_TOP_SLOT = "Project Scripts"
DIVIDER = "- "

""" Services """
svc_sel = lx.service.Selection()
svc_scn = lx.service.Scene()

""" Names """
NAME_NOTIFIER = 'modder.notifier'
NAME_CMD_UPDATE = 'modder.update'
NAME_CMD_NEW = '+@modder.newProjectScript.py'
NAME_CMD_SCRIPTLISTER = 'modder.projectScriptLister'

""" Symbols """
fCMDARG_OPTIONAL = lx.symbol.fCMDARG_OPTIONAL

""" Selection type integers """
SELTYPE_ITEM = svc_sel.LookupType('item')

""" Item type integers """
ITEMTYPE_SCENE = svc_scn.ItemTypeLookup('scene')

def bugger(comment=0):
    if DEBUG_MODE:
        comment = ": " + comment if comment else ""
        lx.out("line " + str(inspect.currentframe().f_back.f_lineno) + comment)

class modderListener(lxifc.SceneItemListener, lxifc.SelectionListener):
    def __init__ (self):
        # We attach the listener.
        self.listenerService = lx.service.Listener()
        self.listenerService.AddListener(self)

    def __del__ (self):
        # In case we need to remove it...
        self.listenerService.RemoveListener(self)
    def notify(self):
        notifier = modderNotifier()
        notifier.Notify(lx.symbol.fCMDNOTIFY_CHANGE_ALL)
    def sil_SceneCreate(self,scene):
        self.notify()
    def sil_SceneDestroy(self,scene):
        self.notify()
    def sil_SceneFilename(self,scene,filename):
        self.notify()
    def sil_SceneClear(self,scene):
        self.notify()
    def selevent_Add(self,type,subType):
        # Scene changes happen via an item selection apparently.
        if type == SELTYPE_ITEM:
            if subType == ITEMTYPE_SCENE:
                self.notify()

    def sil_ItemPreChange(self,scene):
        pass
    def sil_ItemPostDelete(self,scene):
        pass
    def sil_ItemAdd(self,item):
        pass
    def sil_ItemRemove(self,item):
        pass
    def sil_ItemParent(self,item):
        pass
    def sil_ItemChild(self,item):
        pass
    def sil_ItemAddChannel(self,item):
        pass
    def sil_ItemLocal(self,item):
        pass
    def sil_ItemName(self,item):
        pass
    def sil_ItemSource(self,item):
        pass
    def sil_ItemPackage(self,item):
        pass
    def sil_ChannelValue(self,action,item,index):
        pass
    def sil_LinkAdd(self,graph,itemFrom,itemTo):
        pass
    def sil_LinkRemBefore(self,graph,itemFrom,itemTo):
        pass
    def sil_LinkRemAfter(self,graph,itemFrom,itemTo):
        pass
    def sil_LinkSet(self,graph,itemFrom,itemTo):
        pass
    def sil_ChanLinkAdd(self,graph,itemFrom,chanFrom,itemTo,chanTo):
        pass
    def sil_ChanLinkRemBefore(self,graph,itemFrom,chanFrom,itemTo,chanTo):
        pass
    def sil_ChanLinkRemAfter(self,graph,itemFrom,chanFrom,itemTo,chanTo):
        pass
    def sil_ChanLinkSet(self,graph,itemFrom,chanFrom,itemTo,chanTo):
        pass

    def selevent_Current(self,type):
        pass
    def selevent_Remove(self,type,subtType):
        pass
    def selevent_Time(self,time):
        pass
    def selevent_TimeRange(self,type):
        pass

# We don't need to bless a listener,
# we just need to call it once
modderListener()

# I've no idea what any of this means,
# but apparently it needs to be there.
class modderNotifier(lxifc.Notifier,lxifc.CommandEvent):
    masterList = {}
    def noti_Name(self):
        return NAME_NOTIFIER
    def noti_AddClient(self,event):
        self.masterList[event.__peekobj__()] = event
    def noti_RemoveClient(self,event):
        del self.masterList[event.__peekobj__()]
    def Notify(self, flags):
        for event in self.masterList:
            evt = lx.object.CommandEvent(self.masterList[event])
            evt.Event(flags)

lx.bless(modderNotifier, NAME_NOTIFIER)


# Manual update command.
class cmd_modderNotify(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
    def basic_Execute(self, msg, flags):
        # We get an instance of the notifier,
        # and then we call its Notify method,
        # telling it to update everything.
        notifier = modderNotifier()
        notifier.Notify(lx.symbol.fCMDNOTIFY_CHANGE_ALL)
    def cmd_Flags(self):
        # fCMD_UI since it's a UI command, and fCMD_INTERNAL
        # to prevent it from appearing in the command list.
        return lx.symbol.fCMD_UI | lx.symbol.fCMD_INTERNAL
    def basic_Enable(self,msg):
        return True

lx.bless(cmd_modderNotify, NAME_CMD_UPDATE)


# The UIValueHints class we'll be using to manage the list and it's items
class projectScriptListerPopup(lxu.command.BasicHints, lxifc.UIValueHints):
    def __init__(self, path):
        # We attach our notifier
        self._notifiers = [(NAME_NOTIFIER,'')]

        self._items = [['0'],[POPOVER_TOP_SLOT]]

        if path:
            filenames = [os.path.join(dp, f) for dp, dn, fn in os.walk(path) for f in fn]

            regex = re.compile('\.py$')
            filenames = [i for i in filenames if regex.search(i)]

            if filenames:
                self._items[0].append('0')
                self._items[1].append(DIVIDER)

                self._items[0].extend(filenames[:])
                self._items[1].extend([os.path.basename(f) for f in filenames][:])

                self._items[0].append('0')
                self._items[1].append(DIVIDER)

            else:
                self._items[0].append('0')
                self._items[1].append(NONE)



            self._items[0].append(NAME_CMD_NEW)
            self._items[1].append(NEW)

        else:
            self._items[0].append('0')
            self._items[1].append(UNSAVED)


        self._items[0].append(NAME_CMD_UPDATE)
        self._items[1].append(REFRESH)


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
        self.dyna_Add('scripts', lx.symbol.sTYPE_STRING)
        # Set the attribute's queriable flag
        self.basic_SetFlags(0, lx.symbol.fCMDARG_QUERY)


    def arg_UIValueHints(self, index):
        # create an instance of our pop-up list object passing it the
        # list of commands.

        filepath = lx.eval('query sceneservice scene.file ? current')

        if filepath:
            path = dirname(filepath)
        else:
            path = None


        # We *HAVE* to return the UIValueHints here, regardless
        # of the path, otherwise nothing works!
        # Invalid paths are handled by it.
        return projectScriptListerPopup(path)

    def cmd_Execute(self,flags):
        # in the execute method we're going to store the current value of our
        # attribute so that it can be retrieved by the query method later. There's
        # no way to permanently store this information inside the command class
        # itself as the command is created & destroyed between each use. Normally
        # we'd want to be using persistent storage but for simplicity in this
        # example we'll use a UserValue.
        if self.dyna_IsSet(0):
            value = self.dyna_String(0)
            if value == NAME_CMD_UPDATE:
                # Apparently we fired the update command:
                lx.eval(NAME_CMD_UPDATE)
                return lx.result.OK
            elif value == NAME_CMD_NEW:
                lx.eval(NAME_CMD_NEW)
                return lx.result.OK
            else:
                path_scene = lx.eval('query sceneservice scene.file ? current')
                path = join(dirname(path_scene), value)
                if isfile(path):
                    lx.eval('++@{%s}' % path)

    def cmd_Query(self,index,vaQuery):
        # We don't actually need to return anything from the query
        # It just needs to be queryable to create the UI...
        return lx.result.OK

# bless() the command to register it as a plugin
lx.bless(projectScriptListerCmd, NAME_CMD_SCRIPTLISTER)
