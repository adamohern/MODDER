#python

def fileDialog(dtype, title, ftype, uname, pattern=None, ext=None, path=None):
    """ Open a file save dialog for a custom filetype(s)

        params:

            dtype   - Dialog type. One of 'fileOpen', 'fileOpenMulti' or 'fileSave'
            title   - Dialog title string
            ftype   - List or tuple of file fomat type names. This is an internal
                      name for use by  the script, and can be read out after the
                      dialog is dismissed by  querying  dialog.fileSaveFormat.
            uname   - List of usernames that will be displayed in the dialog for
                      each of the types specified in ftype.
            pattern - Optional list or tuple of semicolon-delimited string list
                      of file extensions that the particular file format supports.
                      Only used for fileOpen dialogs. Each extension must include
                      a leading asterisk and period for the filtering to work
                      properly, such as *.jpg;*.jpeg .
            ext     - List or tuple of save extensions, one for each of the types
                      specified in ftype. each ext is a single extension that
                      will automatically  be appended to the end of the filename
                      selected in a save dialog. The period should not be entered,
                      just the extension such as lwo, tga  or txt.
            path    - Optional defailt path to open the dialog at.

    """
    cmd_svc = lx.service.Command()

    cmd_svc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.setup %s' % dtype)
    cmd_svc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.title {%s}' % title)
    for index, name in enumerate(ftype):
        if dtype == 'fileOpen':
            cmd_svc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.fileTypeCustom {%s} {%s} {%s} ""' % (name[index], uname[index], pattern[index]))
        else:
            cmd_svc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.fileTypeCustom {%s} {%s} "" {%s}' % (name[index], uname[index], ext[index]))
    if path:
        cmd_svc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.result {%s}' % path)
    try:
        cmd_svc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.open')
    except:
        return

    command = cmd_svc.Spawn(lx.symbol.iCTAG_NULL, "dialog.result")
    val_arr = cmd_svc.Query(command, 0)

    if val_arr.Count() < 1:
        return

    return val_arr.GetString(0)