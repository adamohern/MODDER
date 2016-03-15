#python

import modo
from sys import exit

frame_range = modo.Scene().currentRange
frame_range = range(frame_range[0], frame_range[1])

fps = modo.Scene().fps
channel = modo.Scene().item('Mesh').position.x

if not channel.isAnimated:
	exit

frozen_values = [channel.get(frame/fps) for frame in frame_range]
for index, frame in enumerate(frame_range):
	channel.envelope.keyframes.add(frozen_values[index], frame/fps)

# set to linear interpolation
channel.envelope.interpolation = 1