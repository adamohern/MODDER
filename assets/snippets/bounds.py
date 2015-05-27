#python

import math

item = lx.eval('query sceneservice selection ? mesh')
b = lx.eval('query layerservice layer.bounds ? %s' % item)

xd = b[3]-b[0]
yd = b[4]-b[1]
zd = b[5]-b[2]
Distance = math.sqrt(xd*xd + yd*yd + zd*zd)

lx.out('length x,y,z: %s,%s,%s' % (xd,yd,zd))
lx.out('diagonal: %s' % Distance)