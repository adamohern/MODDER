#python

# Icons added via markup in the string itself.
# "\x03(i:uiicon_bm_overlay) Some text" < Adds icon resource "bm_overlay" to cell

# All markup flags have the format '\03(pre:string)', where 'pre' is the
# letter f (font), c (color), or i (icon), so we may as well:
def markup(pre,string):
    return '\03(%s:%s)' % (pre,string)

# "\03(c:color)Some Text" < Where "color" is a string representing a decimal
# integer computed with 0x01000000 | ((r << 16) | (g << 8) | b)
def bitwise_rgb(r,g,b):
    return str(0x01000000 | ((r << 16) | (g << 8 | b)))

RED = markup('c',bitwise_rgb(255,0,0))

# I happen to hate 8-bit RGB values. Let's use hex instead.
def bitwise_hex(h):
    h = h.strip()
    if h[0] == '#': h = h[1:]
    r, g, b = h[:2], h[2:4], h[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return bitwise_rgb(r, g, b)

BLUE = markup('c',bitwise_hex('#0e76b7'))

# The below "c:4113" is a special case pre-defined gray color for text,
# which is why the format is different from that of arbitrary colors above.
GRAY = markup('c','4113')

# Italics and bold are done with:
# "\03(c:font)" where "font" is the string "FONT_DEFAULT", "FONT_NORMAL",
# "FONT_BOLD" or "FONT_ITALIC"
DEFAULT = markup('f','FONT_DEFAULT')
NORMAL = markup('f','FONT_NORMAL')
BOLD = markup('f','FONT_BOLD')
ITALIC = markup('f','FONT_ITALIC')

# You can combine styles by stringing them together:
GRAY_ITALIC = GRAY + ITALIC

# These flags are pilfered from the modo source code itself:
fTREE_VIEW_ITEM_ATTR = 0x00000001
fTREE_VIEW_ITEM_EXPAND = 0x00000002
fTREE_VIEW_ATTR_EXPAND = 0x00000004
