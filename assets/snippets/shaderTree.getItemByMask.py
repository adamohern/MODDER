'''
    By Matt Cox (https://gist.github.com/mattcox/5933979)

    Demonstrates how to get the item being masked from a material group.
    Simply pass the material group to the function and it should return
    the masked item.
'''

def itemMask_get (matGroup):
    matGroup = lx.object.Item (matGroup)

    if matGroup.test() == False:
        return None

    if group.TestType(lx.service.Scene().ItemTypeLookup(lx.symbol.sITYPE_MASK)) == False:
        return None

    scene = matGroup.Context()
    shadeloc_graph = lx.object.ItemGraph(scene.GraphLookup(lx.symbol.sGRAPH_SHADELOC))

    if shadeloc_graph.FwdCount(matGroup) > 0:
        maskedItem = shadeloc_graph.FwdByIndex(matGroup, 0)
    else:
        return None

    return maskedItem