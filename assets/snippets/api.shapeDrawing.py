#python

'''
    By Matt Cox (https://gist.github.com/mattcox/5764657)

    Shape Draw python example. This python plugins demonstrates how to create
    a Package that can be added to existing items, that controls how they draw
    in the GL viewport. We will simply draw a circle. A radius channel and an
    sides channel will control how the circle is drawn.
    
    To use, add the python script to an lxserv folder in your scripts directory.
    Select an locator item and enter: item.addPackage shape.draw. To remove the
    package, enter: item.remPackage shape.draw.
'''

import lx
import lxifc
import lxu.vector
import math

PACKAGE_NAME = 'shape.draw'

CHAN_RADIUS = 'Radius'
CHAN_SIDES = 'Sides'

class Instance(lxifc.PackageInstance, lxifc.ViewItem3D):
    
    def __init__(self):
        self.item = lx.object.Item()
    
    def pins_Initialize(self,item,super):
        '''
            The initialize method is called when the instance is associated with
            an item. We get the item and localize it so that we can easily access
            it's channels from other methods.
        '''
        self.item = lx.object.Item(item)
    
    def vitm_Draw(self,chanRead,strokeDraw,selectionFlags):
        '''
            The Draw method simply draws whatever we tell it to in the GL view.
            We're going to read the channels on the package and use them to
            calculate a circle, which we'll then draw.
        '''

        if self.item.test() == False:
            return
        
        chan_read = lx.object.ChannelRead(chanRead)
        stroke_draw = lx.object.StrokeDraw (strokeDraw)
        
        colour = (1.0,1.0,1.0)

        chan_sides_id = self.item.ChannelLookup(CHAN_SIDES)
        chan_radius_id = self.item.ChannelLookup(CHAN_RADIUS)

        chan_sides = chan_read.Integer(self.item, chan_sides_id)
        chan_radius = chan_read.Double(self.item, chan_radius_id)

        degrees = 360.0 / float(chan_sides)

        stroke_draw.BeginW(lx.symbol.iSTROKE_LINE_LOOP, colour, 1.0, 1.0)

        for i in range(chan_sides):
            degree = degrees * i
            x = math.cos((degree*(math.pi/180))) * chan_radius
            z = math.sin((degree*(math.pi/180))) * chan_radius
            stroke_draw.Vertex3(x, 0.0, z, lx.symbol.iSTROKE_ABSOLUTE)

class Package(lxifc.Package, lxifc.ChannelUI):
        
    def pkg_SetupChannels(self, addChan):
        '''
            The SetupChannels function is where we add any extra channels to our
            custom item. We are going to be adding two channels to our item;
            "Radius" and "Sides". These channel will be used by the package
            instance to control how it draws.
        '''
        addChan = lx.object.AddChannel(addChan)
        
        addChan.NewChannel(CHAN_RADIUS, lx.symbol.sTYPE_DISTANCE)
        addChan.SetDefault(0.5, 0)
        
        addChan.NewChannel(CHAN_SIDES, lx.symbol.sTYPE_INTEGER)
        addChan.SetDefault(0.0, 32)
    
    def pkg_Attach(self):
        '''
            The Attach function is called to create a new Instance of our item
            in the scene. We simply return an instance of our Instance class.
        '''
        return Instance()
        
    def pkg_TestInterface(self, guid):
        '''
            The TestInterface function is called for every potential interface
            that the Instance could inherit from. We need to return true when
            queried for any interface that it does inherit from. We do this
            by comparing the GUID that is being passed as an argument against
            the GUID of the interfaces that we know our Instance inherits from.
            As our Instance inherits from PackageInstance and ViewItem3D, we
            need to return True for both of them.
        '''
        return (lx.service.GUID().Compare(guid, lx.symbol.u_PACKAGEINSTANCE) == 0) or (lx.service.GUID().Compare(guid, lx.symbol.u_VIEWITEM3D) == 0)
        
    def cui_UIHints(self,channelName,hints):
        '''
            The UIHints method is provided by the ChannelUI interface that our
            Package class inherits from. This allows us to specify various
            hints for a channel, such as Min and Max. Ideally, we'd do this when
            creating the channel using the SetHints() method, however, that's
            currently impossible in Python.
        '''
        hints = lx.object.UIHints(hints)
        
        if channelName == CHAN_RADIUS:
            hints.MinFloat(0.0)
            hints.MaxFloat(10.0)
        elif channelName == CHAN_SIDES:
            hints.MinInt(3)
            hints.MaxInt(128)

'''
    Finally, bless the item package so that it is registered as a plugin inside
    of modo. As this is a package that is added to another item and not a full
    item in itself, we won't define a supertype.
'''
lx.bless(Package, PACKAGE_NAME)