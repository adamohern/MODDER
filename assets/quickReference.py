#python

# Get active mesh item (int)
activeMeshID = lx.eval('query layerservice layers ? main')

# Get primary mesh item
def activeLayers():
    lyr_svc = lx.service.Layer ()
    scan = lx.object.LayerScan (lyr_svc.ScanAllocate (lx.symbol.f_LAYERSCAN_ACTIVE))
    if scan.Count () > 0:
        item = scan.MeshItem (0)
    scan.Apply ()
    
# Get any currently active mesh items
def mainLayer():
    lyr_svc = lx.service.Layer ()
    scan = lx.object.LayerScan (lyr_svc.ScanAllocate (lx.symbol.f_LAYERSCAN_PRIMARY))
    if scan.Count () > 0:
        item = scan.MeshItem (0)
    scan.Apply ()

# Get layer id string from int id (string)
itemID = lx.eval('query layerservice layer.id ? %s' % activeMeshID)

# Get mesh items (list of IDs)
layers = lx.eval('query layerservice layers ? all')
fgLayers = lx.eval('query layerservice layers ? fg')
bgLayers = lx.eval('query layerservice layers ? bg')

# Get selected item(s) (list of strings)
selectedItems = lx.eval('query sceneservice selection ?')

# Get selected components (list of IDs)
vertSel = lx.eval('query layerservice verts ? selected')
edgeSel = lx.eval('query layerservice edges ? selected')
polySel = lx.eval('query layerservice polys ? selected')

# Get material for poly (string)
materials = lx.eval('query layerservice poly.material ? %s' % polyID)

# Get current selection mode (string)
def selMode():
    for mode in 'vertex;edge;polygon;item;pivot;center;ptag'.split(';'):
        if lx.eval('select.typeFrom %s;%s ?' % (mode, modes)): 
            return mode

# Get current selection and mode (dictionary)
def getSelection():
    s = {}
    for mode in 'vertex;edge;polygon;item;pivot;center;ptag'.split(';'):
        if lx.eval('select.typeFrom %s;%s ?' % (mode, modes)): 
            s["mode"] = mode
            break
    if s["mode"] == 'vertex':
        s["elements"] = lx.eval('query layerservice verts ? selected')
    elif s["mode"] == 'edge':
        s["elements"] = lx.eval('query layerservice edges ? selected')
    elif s["mode"] == 'polygon':
        s["elements"] = lx.eval('query layerservice polys ? selected')
    elif s["mode"] == 'item':
        s["elements"] = lx.eval('query sceneservice selection ?')
        
    return s