#python

#Must be inside a folder called 'lxserv' somewhere in a MODO search path.

import lx
import lxu.command
import traceback

class myGreatCommand(lxu.command.BasicCommand):
    def __init__(self):
        lxu.attributes.DynamicAttributes.__init__(self)
        self._flags = []
        self._has_varg = False
        self._msg = lx.service.Message().Allocate()

		#command accepts an argument
        self.dyna_Add('arg1', lx.symbol.sTYPE_STRING) #or sTYPE_FLOAT
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)


    def cmd_Message(self):
        """Returns our message object."""
        return self._msg


    def cmd_Flags(self):
        """Required method, but should be overridden by the client.
        The default retuns zero, which means this is a side-effect command.

        """
        return 0


    def dyna_Add(self, name, type):
        """We override dyna_Add() to expand our flags array."""
        self._flags.append(0)
        lxu.attributes.DynamicAttributes.dyna_Add(self, name, type)


    def basic_SetFlags(self, index, flags):
        """Flags can be set by the client during initialization."""
        self._flags[index] = flags;
        if flags & lx.symbol.fCMDARG_VARIABLE:
            self._has_varg = True


    def basic_Enable(self, msg):
        """basic_Enable() gives the enable state (true/false) and reason.
        It can also return None if the command is not available at all.
        """
        return True

    def cmd_Enable(self, msg):
        msg = lx.object.Message(msg)
        res = self.basic_Enable(msg)
        if res == None:
            msg.SetCode(lx.result.CMD_NOT_AVAILABLE)
            lx.throw(lx.result.CMD_NOT_AVAILABLE)
        elif not res:
            msg.SetCode(lx.result.CMD_DISABLED)
            lx.throw(lx.result.CMD_DISABLED)
        else:
            msg.SetCode(lx.result.OK)

    def cmd_NotifyAddClient(self,argument,object):
        lx.notimpl()
    def cmd_NotifyRemoveClient(self,object):
        lx.notimpl()


    def cmd_ArgClear(self, index):
        """Clearing arguments has to deal with the vararg flags on all arguments."""
        self.dyna_SetType(index, None)
        if not self._has_varg:
            return

        for i in range(len(self._flags)):
            self._flags[i] = self._flags[i] & ~lx.symbol.fCMDARG_REQFORVAR_SET
            if self._flags[i] & lx.symbol.fCMDARG_VARIABLE:
                self.cmd_ArgClear(i)


    def cmd_ArgResetAll(self):
        for i in range(len(self._flags)):
            self.cmd_ArgClear(i)


    def cmd_ArgFlags(self, index):
        """Get the flags, getting value_set from the dyna attrs."""
        f = self._flags[index]
        if self.dyna_IsSet(index):
           f = f | lx.symbol.fCMDARG_VALUE_SET

        return f


    def basic_ArgType(self, index):
        """Dynamic argument types can be supported with this method."""
        lx.notimpl()


    def cmd_ArgSetDatatypes(self):
        if not self._has_varg:
            return

        for i in range(len(self._flags)):
            if self._flags[i] & lx.symbol.fCMDARG_REQFORVARIABLE and not self.dyna_IsSet(i):
                lx.throw(lx.result.CMD_MISSING_ARG)

        for i in range(len(self._flags)):
            self._flags[i] = self._flags[i] | lx.symbol.fCMDARG_REQFORVAR_SET
            if self._flags[i] & lx.symbol.fCMDARG_VARIABLE:
                self.dyna_SetType(i, self.basic_ArgType(i))


    def basic_ButtonName(self):
        """Button name override."""
        pass


    def cmd_ButtonName(self):
        s = self.basic_ButtonName()
        if s:
            return s
        lx.notimpl()


    def basic_Icon(self):
        """Icon name override."""
        pass


    def cmd_Icon(self):
        s = self.basic_Icon()
        if s:
            return s
        lx.notimpl()


    def basic_PreExecute(self, msg):
        """Pre-Execution: failure is trapped by the message object."""
        pass

    def cmd_PreExecute(self):
        try:
            self.basic_PreExecute(self._msg)
        except:
            lx.outEx("basic_PreExecute failed")
            self._msg.SetCode(lx.result.FAILED)
            raise   # outEx doesn't work -- only way to see the error is to raise it again


    def basic_Execute(self, msg, flags):
        """Execution: failure is trapped by the message object."""
        lx.notimpl()


    def cmd_Execute(self, flags):
        try:
            self.basic_Execute(self._msg, flags)
        except:
            lx.outEx("basic_Execute failed")
            self._msg.SetCode(lx.result.FAILED)
            raise   # outEx doesn't work -- only way to see the error is to raise it again

lx.bless(myGreatCommand, "mecco.myGreatCommand")
