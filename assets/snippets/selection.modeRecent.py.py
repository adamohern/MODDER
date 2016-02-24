#python

sel_svc = lx.service.Selection()
selTypes = [lx.symbol.sSELTYP_VERTEX, lx.symbol.sSELTYP_EDGE, lx.symbol.sSELTYP_POLYGON, lx.symbol.sSELTYP_ITEM]
selTypeStorage = lx.object.storage ('i', len(selTypes))
selTypeStorage.set (map (sel_svc.LookupType, selTypes))
print sel_svc.LookupName (sel_svc.CurrentType(selTypeStorage))
