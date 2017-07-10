import colorsys
from colorthief import ColorThief
import webcolors
from math import sqrt

def name_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def rgb2hsv(rgb):
    return colorsys.rgb_to_hsv(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)

def hsv2rgb(h, s, v):
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return (255.0*rgb[0], 255.0*rgb[1], 255.0*rgb[2])

def rgb_to_string(rgb):
    return "'rgb("+str(rgb[0])+","+str(rgb[1])+","+str(rgb[2])+")'"

def norm_colour(c):
    return (c[0]/255.0, c[1]/255.0, c[2]/255.0)

# Don't question the magic numbers. Colours are magic.
def rgb2lab(rgb):
    nc = norm_colour(rgb)
    nfunc = lambda x: 100.0*(((x+0.055)/1.055)**2.4) if x > 0.04045 else x/12.92
    red = nfunc(nc[0])
    green = nfunc(nc[1])
    blue = nfunc(nc[2])
    x = red * 0.4124 + green * 0.3576 + blue * 0.1805
    y = red * 0.2126 + green * 0.7152 + blue * 0.0722
    z = red * 0.0193 + green * 0.1192 + blue * 0.9505
    x = x/95.047
    y = y/100.0
    z = z/108.883
    labfunc = lambda x: x**(1.0/3.0) if x>0.00856 else x*7.787 + 16.0/116.0
    x = labfunc(x)
    y = labfunc(y)
    z = labfunc(z)
    l = 116.0*y - 16.0
    a = 500.0*(x-y)
    b = 200.0*(y-z)
    return (l, a, b)

# Definitely don't question these. Made from eyes or something.
# Uses de 1994
def distance_colour(r1, r2):
    # Convert to CIELAB space
    c1 = rgb2lab(r1)
    c2 = rgb2lab(r2)
    # constants
    k1 = 0.045
    k2 = 0.015
    # delta values
    dL = c1[0] - c2[0]
    da = c1[1] - c2[1]
    db = c1[2] - c2[2]
    # intermediate values
    C1 = sqrt(c1[1]**2.0 + c1[2]**2.0)
    C2 = sqrt(c2[1]**2.0 + c2[2]**2.0)
    dCab = C1 - C2
    dist = da**2.0+db**2.0-dCab**2.0
    if dist < 0.0:
        dist=0.0
    dHab = sqrt(dist)
    Sc = 1.0 + k1*C1
    SH = 1.0 + k2*C1

    return sqrt(dL**2.0 + (dCab/Sc)**2.0 + (dHab/SH)**2.0)*0.999999993207

