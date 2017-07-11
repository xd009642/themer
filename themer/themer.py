import sys
import os
import glob
import colorsys
from colorthief import ColorThief
import webcolors
from colour_math import *;
from statistics import mean


def palette2str(p):
    res = "["
    for c in p:
        res += rgb_to_string(c) +','
    res =  res[:-1]
    res += ']'
    return res

def average_S_V(palette):
    return (mean(rgb2hsv(c)[1] for c in palette), mean(rgb2hsv(c)[2] for c in palette))

def average_palette_distance(colour, palette):
    return (1.0/len(palette)) * sum([colour_distance(colour, p) for p in palette])

def generate_palette_str(palette, light, dark):
    #hsv_palette = [ x for p in palette rgb2hsv(p)]
    # I now have lightest and darkest (again). Make a palette!
    # Palette design:
    # Row 1
    # darkest, lighest, accent, ...
    # Row 2
    # Different shades of row 1?
    result = [dark, light];
    org_dark = min(palette, key=lambda c:rgb2hsv(c)[2]) 
    # Fill first row of palette with beautiful colours.
    for i in range(6):
        accent = max((p for p in palette if p!=org_dark), key = lambda c: average_palette_distance(c, result))
        palette.remove(accent);
        # Don't include background, too dark so drags things down
        #(s, v) = average_palette_distance(palette[1:])
        accent_hsv = rgb2hsv(accent);
        # aim for within _% of S and V
        result.append(accent)
    backhsv = rgb2hsv(dark)
    # Colour heuristics, activate!
    result.append(hsv2rgb(backhsv[0], backhsv[1], min(1.0 - backhsv[2], 0.9)))
    # Fill in other tints. These are more sensible!
    for i in range(1, 8):
        # Erring towards lighter by 10%
        hsv = rgb2hsv(result[i])
        result.append(hsv2rgb(hsv[0], hsv[1], min(0.9, hsv[2]+0.25)))
    return palette2str(result) 

# Plan
# modes
# Init. Run on terminal startup if colour scheme not persisted
# New. Change desktop background, new colour scheme!
# Shuffle. Change to a random previous background
# List. list available backgrounds
#
# Improvements
# See if palette is too sparse, add some complementary colours (opposite hue 
# same SL etc).

if len(sys.argv) == 1:
    exit("No image specified")
else:
    picture = sys.argv[1]
    picture = os.path.abspath(picture)


WALLPAPER_DIR = "~/Pictures/Wallpapers"
# Gonna oversample to try and increase variance
ncolours = 16
thief = ColorThief(picture);


palette = thief.get_palette(color_count=ncolours)
os.system("gsettings set org.gnome.desktop.background picture-uri " + picture);
os.system("gsettings set org.gnome.desktop.screensaver picture-uri " + picture);

# work out background colour!
darkest = min(palette, key=lambda c: rgb2hsv(c)[2]);
darkhsv = rgb2hsv(darkest);
if darkhsv[2] > 0.4:
    darkest = hsv2rgb(darkhsv[0], darkhsv[1], 0.2)

lightest = max(palette, key=lambda c: rgb2hsv(c)[2]);
lighthsv = rgb2hsv(lightest)
print(lighthsv)
if lighthsv[2] < 0.5:
    lightest = hsv2rgb(lighthsv[0], lighthsv[1], 0.6)

prof_guid = "b1dcc9dd-5262-4d8d-a863-c897e6d979b9"
prof_preamble = "/org/gnome/terminal/legacy/profiles:/:" + prof_guid +"/"
os.system('dconf write ' + prof_preamble + 'background-color "' + rgb_to_string(darkest) + '"') 
os.system('dconf write ' + prof_preamble + 'foreground-color "' + rgb_to_string(lightest) + '"') 

# Generate palette!
# This is harder
os.system('dconf write ' + prof_preamble + 'palette "' + generate_palette_str(palette, lightest, darkest)+ '"');

