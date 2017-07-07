import sys
import os
import colorsys
from colorthief import ColorThief

def rgb2hsv(rgb):
    return colorsys.rgb_to_hsv(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)

def hsv2rgb(h, s, v):
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return (255.0*rgb[0], 255.0*rgb[1], 255.0*rgb[2])

def rgb_to_string(rgb):
    return '"'+ "'rgb("+str(rgb[0])+","+str(rgb[1])+","+str(rgb[2])+")'" +'"'
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

ncolours = 15
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

prof_guid = "b1dcc9dd-5262-4d8d-a863-c897e6d979b9"
os.system('dconf write /org/gnome/terminal/legacy/profiles:/:' + prof_guid + "/background-color " + rgb_to_string(darkest)) 
os.system('dconf write /org/gnome/terminal/legacy/profiles:/:' + prof_guid + "/foreground-color " + rgb_to_string(lightest)) 

