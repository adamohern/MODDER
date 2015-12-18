#python

import lx

se = lx.current_scripteditor

def exists():
    """
    By Adam O'Hern
    Returns True if a script editor currently exists.
    """
    try:
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
        se._editor._input.insertPlainText('')
        return True
    except:
        return False
    
def set_script(string):
    """
    By Ivo Grigull @ The Foundry
    Clear the script editor and history panes
    """
    try:
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
        return se._editor._input.toPlainText()
    except:
        return False