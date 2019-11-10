from PIL import Image
import glob

# Load our icon files and convert green to transparency
for icon in glob.glob("icon-*.png"):
    print(icon)
    im = Image.open(icon).convert('P', palette=Image.ADAPTIVE, colors=4)
    im.putpalette([
        255, 255, 255,
        0, 0, 0,
        255, 0, 0,
        0, 255, 0,
    ])
    im.save(icon, transparency = 3, optimize = 1)
