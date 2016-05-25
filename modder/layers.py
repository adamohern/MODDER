#python

import lx, lxu, modo

def active():
    """Returns a list of all currently active mesh layers (regardless of selection state)."""
    
    lyr_svc = lx.service.Layer ()
    scan = lx.object.LayerScan (lyr_svc.ScanAllocate (lx.symbol.f_LAYERSCAN_ACTIVE))
    itemCount = scan.Count ()
    if itemCount > 0:
            items = [modo.Mesh( scan.MeshItem(i) ) for i in range(itemCount)]
    scan.Apply ()
    
    return items

def primary():
    """Returns the current primary mesh item (regardless of selection state)."""
    
    lyr_svc = lx.service.Layer ()
    scan = lx.object.LayerScan (lyr_svc.ScanAllocate (lx.symbol.f_LAYERSCAN_PRIMARY))
    itemCount = scan.Count ()
    if itemCount > 0:
            items = [modo.Mesh( scan.MeshItem(i) ) for i in range(itemCount)]
    scan.Apply ()
    
    return items

def background():
    """Returns a list of all background (inactive) mesh layers (regardless of selection state)."""
    
    lyr_svc = lx.service.Layer ()
    scan = lx.object.LayerScan (lyr_svc.ScanAllocate (lx.symbol.f_LAYERSCAN_BACKGROUND))
    itemCount = scan.Count ()
    if itemCount > 0:
            items = [modo.Mesh( scan.MeshItem(i) ) for i in range(itemCount)]
    scan.Apply ()
    
    return items