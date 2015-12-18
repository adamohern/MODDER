#!/usr/bin/env python

# By Gwynne Reddick via MODO dev Skype channel

import traceback

def main():
    args = lx.args()

    if args:
        ###===
        ###=== Executed before the preset is added to the scene, allows us to
        ###=== abort the preset application if we need to.
        ###===
        if args[0] == 'beforeCreate':
            pass

        ###===
        ###=== Executed after the preset is added to the scene
        ###===
        if args[0] == 'onDo':
            pass

        # 'onCreate' and 'onDrop' events are special cases. 'onCreate' is called
        # if the assembly preset has an 'onCreate' script defined as part of the
        # assembly. 'onDrop' is called of the preset is darg/dropped into a
        # viewport.
        if args[0] == 'onCreate':
            pass
        if args[0] == 'onDrop':
            pass

    else:
        sys.exit('LXe_ABORT:Unknown error applying preset')


if __name__ == '__main__':
    try:
        main()
    except:
        lx.out(traceback.format_exc())