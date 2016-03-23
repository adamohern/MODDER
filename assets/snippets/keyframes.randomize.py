from random import random
import modo

fps = modo.Scene().fps
frame_range = modo.Scene().sceneRange

channels = lxu.select.ChannelSelection().current()
channels = [modo.Channel(channel[1],modo.Item(channel[0])) for channel in channels]

for frame in range(frame_range[0],frame_range[1]):
    for channel in channels:
        channel.envelope.keyframes.add(random(),frame/fps)
