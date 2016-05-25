def selected(implicit=False,connected=False):
    """Returns a list of all implicitly selected polys in all active layers.
    If in poly mode, returns selected polys. If in edge or vertex mode, 
    returns all polys adjacent to all selected components.
    
    :param implicit: If True, returns polys touching the current edge or vertex selection. If False, uses only explicitly selected polys.
    :param connected: If True, returns all polys connected to the selection."""
    
    result = set()
    scene = modo.scene.current()
    
    for layer in layers.active():

        if implicit:
            if mode() == 'polygon':
                if layer.geometry.polygons.selected:
                    for p in layer.geometry.polygons.selected:
                        result.add(p)
                else:
                    for p in layer.geometry.polygons:
                        result.add(p)
            elif mode() == 'edge':
                if layer.geometry.edges.selected:
                    for e in layer.geometry.edges.selected:
                        for p in e.polygons:
                            result.add(p)
                else:
                    for p in layer.geometry.polygons:
                        result.add(p)
            elif mode() == 'vertex':
                if layer.geometry.edges.selected:
                    for v in layer.geometry.vertices.selected:
                        for p in v.polygons:
                            result.add(p)
                else:
                    for p in layer.geometry.polygons:
                        result.add(p)

            elif mode() == 'ptag':
                return False
            else:
                return False
            
        if not implicit:
            if layer.geometry.polygons.selected:
                for p in layer.geometry.polygons.selected:
                    result.add(p)
            else:
                for p in layer.geometry.polygons:
                    result.add(p)
        
        if connected:
            queue = list(result)
            island = set()

            while queue:
                poly = queue.pop()
                if not poly in island:
                    island.add(poly)
                    queue.extend( poly.neighbours )
            
            result = island
            
    return list(result)