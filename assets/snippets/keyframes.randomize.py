#python

from random import random
import modo

fps = modo.Scene().fps
frame_range = modo.Scene().sceneRange

b = modo.Scene().selected[0].position.x.envelope.keyframes

#c = b.numKeys
#b.setIndex(1)

for frame in range(frame_range[0],frame_range[1]):
	b.add(random(),frame/fps)