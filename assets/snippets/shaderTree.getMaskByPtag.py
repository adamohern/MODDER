'''
    By Matt Cox (https://gist.github.com/mattcox/5940170)
    
    Demonstrates how to find a material ptag in the shader tree. Give it
    a ptag and it will return the first mask item in the shader tree that
    is using that Ptag.
'''

import lx
import lxu.select

def FindPtagMask (ptagName):
    scn_svc = lx.service.Scene()
    scene = lxu.select.SceneSelection().current()
    
    chan_read = scene.Channels(lx.symbol.s_ACTIONLAYER_EDIT, 0.0)
    mask_type = scn_svc.ItemTypeLookup(lx.symbol.sITYPE_MASK)
    
    for i in range (scene.ItemCount(mask_type)):
        mask = scene.ItemByIndex(mask_type, i)
        
        if chan_read.String(mask, mask.ChannelLookup(lx.symbol.sICHAN_MASK_PTYP)) == 'Material' and chan_read.String(mask, mask.ChannelLookup(lx.symbol.sICHAN_MASK_PTAG)) == ptagName:
            return mask
        
    return None