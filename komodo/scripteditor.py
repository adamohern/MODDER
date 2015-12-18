#python

import lx

def exists():
    """
    By Adam O'Hern
    Returns True if a script editor currently exists.
    
    NOTE: As of 902 build 100509, a bug exists that keeps a script editor 
    from being recognized by lx.current_scripteditor until it has been initialized
    by the Run command (ctrl+enter). Once the editor has been run, the following code
    works fine.
    
    "If you want to hot-fix it yourself now, 
    add "lx.current_scripteditor = scriptEditor" in extra\scripts\lxserv\lxscripteditor.py line 69 
    after it is initialized. (also delete the corresponding lxscripteditor.pyc file to ensure the change manifests)."
    -Ivo
    
    This should be fixed in future versions.
    """
    try:
        se = lx.current_scripteditor
        se._editor._input.toPlainText()
        return True
    except:
        return False

def clear_output():
    """
    By Ivo Grigull @ The Foundry
    Clear the history pane
    """
    try:
        se = lx.current_scripteditor
        se._output.clear()
        return True
    except:
        return False
        
def append_output(string):
    """
    By Ivo Grigull @ The Foundry
    Write to the history output
    """
    try:
        se = lx.current_scripteditor
        se._output.updateOutput('%s\n' % string)
        return True
    except:
        return False

def clear_script():
    """
    By Ivo Grigull @ The Foundry
    Clear the script editor and history panes
    """
    try:
        se = lx.current_scripteditor
        se._editor._input.insertPlainText('')
        return True
    except:
        return False
    
def insert_script(string):
    """
    By Ivo Grigull @ The Foundry
    Clear the script editor and history panes
    """
    try:
        se = lx.current_scripteditor
        se._editor._input.insertPlainText('%s\n' % string)
        return True
    except:
        return False
    
def set_script(string):
    """
    By Ivo Grigull @ The Foundry
    Clear the script editor and history panes
    """
    try:
        se = lx.current_scripteditor
        se._editor._input.clear()
        se._editor._input.insertPlainText('%s\n' % string)
        return True
    except:
        return False
    
def get_script():
    """
    By Adam O'Hern
    Get the current contents of the script editor
    """
    try:
        se = lx.current_scripteditor
        return se._editor._input.toPlainText()
    except:
        return False