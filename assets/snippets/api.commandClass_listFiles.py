#!/usr/bin/env python
 
'''
    By Matt Cox (https://gist.github.com/mattcox/6599717)

    Demonstrates how to setup a simple popup menu populated using dynamic values.
   
    This will search a directory for files and list all of the files inside the
    popup.
    
    As notifiers are currently unsupported in modo 701 SP2, we can't force the
    popup to update when the directory contents changes. So for now, it'll only
    update when the UI redraws (for example, switching between tabs).
    
    To use this command, embed it in a form with the following syntax:
        files.list path:{c:\Users\Matt\Desktop} file:?
'''
 
import lx
import lxifc
import lxu.command

SERVER_NAME = 'files.list'

ARG_FILE = 'file'
ARG_PATH = 'path'

path_argument_value = ''

class Popup (lxifc.UIValueHints):
    
    def __init__ (self):
        global path_argument_value
        
        self.Usernames = []
        self.Names = []
        self.Path = path_argument_value
 
    def BuildList (self):
        '''
            Here we will build the list that populates the popup. There are
            technically two lists; the first is a list of internal values, these
            are the actual values returned by the command. The second list is a
            list of usernames, these are what are displayed to the user in the UI.
            
            We'll store the entire file path in the internal name and only the
            filename in the username. This means that the user gets a simple list
            of filenames to choose from, but we can deal with the full filepath
            internally.
        '''
        
        '''
            We could search the directory for files using the built in Python
            functions, but as this is a Modo SDK example, we may as well use the
            FileService in the SDK.
        '''
        
        file_svc = lx.service.File ()
        
        '''
            Check if the search path exists and make sure it's a directory.
        '''
        
        if file_svc.TestFileType (self.Path) != lx.symbol.iFILETYPE_DIRECTORY:
            return            
        
        '''
            Allocate a file reference object. This allows us to easily list of
            the files inside the directory and work with them.
        '''
        
        file_ref = file_svc.AllocReference (self.Path)
        
        for i in range (file_ref.SubCount ()):
            sub_file_ref = file_ref.SubByIndex (i)
            
            '''
                Skip anything that isn't a file. For example, directories.
            '''
            
            if sub_file_ref.Type () != lx.symbol.iFILETYPE_NORMAL:
                continue
            
            '''
                Store the full path in the Names list and the NiceName in the
                Usernames list.
            '''
            
            self.Names.append (sub_file_ref.Path ())
            self.Usernames.append (sub_file_ref.NiceName ())
 
    def uiv_Flags (self):
        '''
            The Flags method defines how the popup is drawn in the UI. We'll
            return fVALHINT_POPUPS, which will tell modo to draw a simple
            popup list.
        '''
        
        return lx.symbol.fVALHINT_POPUPS
 
    def uiv_PopCount (self):
        '''
            Returns the number of elements to display in the popup.
        '''

        return len (self.Names)
 
    def uiv_PopUserName (self, index):
        '''
            This function is called repeatedly for every element in the list,
            (defined by PopCount). We simply return the username to display in
            the list.
        '''
        
        return self.Usernames[index]
 
    def uiv_PopInternalName (self, index):
        '''
            This function is called repeatedly for every element in the list,
            (defined by PopCount). We simply return the name for each value
            to hold. This is the actual value returned when the user chooses an
            option.
        '''
        
        return self.Names[index]
 
class Command (lxu.command.BasicCommand):
    
    def __init__ (self):
        lxu.command.BasicCommand.__init__(self)
        
        '''
            We want to add the arguments for the command. There are two arguments
            on this command; the first is the path to search and the second, which
            is queryable, returns the list of filenames in the popup. As we don't
            want the user to be able to change the path in the dialog, we mark
            that argument as hidden, so only the file string should ever be shown
            to the user.
        '''
        
        self.dyna_Add (ARG_PATH, lx.symbol.sTYPE_FILEPATH)
        self.dyna_Add (ARG_FILE, lx.symbol.sTYPE_STRING)
        
        self.basic_SetFlags (0, lx.symbol.fCMDARG_HIDDEN)
        self.basic_SetFlags (1, lx.symbol.fCMDARG_QUERY)
 
    def arg_UIValueHints (self, index):
        '''
            When the command is queried, it will call this function and pass it
            the index of the argument being queried. If the argument matches the
            index of the file argument, we'll create an instance of the Popup
            class and call its BuildPopup function, before returning the Popup
            class instance from the function.
        '''
        
        if index == 1:
            popup = Popup ()
            popup.BuildList ()
            
            return popup
 
    def cmd_Flags (self):
        '''
            The Flags method defines the type of command this is, specifically
            how it should work with the undo system. If your command isn't going
            to change the scene, you can technically return 0, however, returning
            MODEL and UNDO ensures that the command is undoable and prevents any
            nasty things happening.
        '''
        
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO
    
    def cmd_Execute (self, flags):
        '''
            This function is called when the user executes the command. Either
            manually from the command line or from selecting an option in the list.
            You could do anything you want here, but for now, we'll simply read
            the value they selected and print it out to the event log.
        '''
        
        if self.dyna_IsSet (1):
            lx.out('Filename: %s' % self.dyna_String (1))
 
    def cmd_Query (self, index, vaQuery):
        '''
            This function is called when the command is queried. We'll read the
            value of the path argument and store it in the global variable, so
            that it can be used when building the popup.
        '''
        
        global path_argument_value
        
        if self.dyna_IsSet (0):
            path_argument_value = self.dyna_String (0)
        
        return
 
'''
    Finally, we bless the Command class. This promotes it to be a first class
    plugin within modo.
'''

lx.bless (Command, SERVER_NAME)