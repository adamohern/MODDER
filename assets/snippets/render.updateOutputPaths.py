import modo, re, os

basepath = os.path.join('Q:',os.sep,'Adam','output')

sceneName = os.path.splitext(modo.Scene().name)
newpath = os.path.join(basepath, sceneName[0])
defaultFormat = "openexr"

for i in modo.Scene().items('renderOutput'):
    directory = os.path.join(newpath, i.name)

    i.channel('filename').set(os.path.join(directory, sceneName[0]))

    if not i.channel("format").get():
        i.channel("format").set(defaultFormat)

    print directory
    if not os.path.exists(directory):
        os.makedirs(directory)
