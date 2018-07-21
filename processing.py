from PIL import Image

def removered():
    img = Image.open("vases.png")
    pixels = [(0,200,b) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("removered.png")

def invert():
    img = Image.open("vases.png")
    pixels = [(255 - r,255 - g,255 - b) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("invert.png")

def darken():
    img = Image.open("vases.png")
    pixels = [(int(r*0.8),int(g*0.8),int(b*0.8)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("darken.png")

def lighten():
    img = Image.open("vases.png")
    pixels = [(int(r*1.2),int(g*1.2),int(b*1.2)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("lighten.png")

def grayscale():
    img = Image.open("vases.png")
    pixels = [(int((r + g + b) / 3),int((r + g + b) / 3),int((r + g + b) / 3)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("grayscale.png")

def rounder(x):
    if x <= 63:
        x = 0
        return x
    elif x > 63 and x <= 127:
        x = 100
        return x
    elif x > 127 and x <= 191:
        x = 150
        return x
    elif x > 191 and x <= 255:
        x = 200
        return x
    else:
        print("broken")

def posterize():
    img = Image.open("vases.png")
    pixels = [(rounder(r),rounder(g),rounder(b)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("posterize.png")

def solarer(x):
    if x < 128:
        x = 255 - x
        return x
    else:
        return x

def solarize():
    img = Image.open("vases.png")
    pixels = [(solarer(r),solarer(g),solarer(b)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("solarize.png")

def denoise():
    img = Image.open("vases.png")
    pixels = [(r * 10, 0, 0) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("newnoise.png")

def denoise2():
    img = Image.open("copper-puzzle.png")
    pixels = [(0, g * 20, b * 20) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    img.save("newnoise.png")

def denoise3():
    img = Image.open("clue2.bmp")
    img.show()
    pixels = [(0,0,0) for (255,0,0,a) in img.getdata()]
    img.putdata(pixels)
    pixels = [(0,0,0) for (255,255,255,a) in img.getdata()]
    img.putdata(pixels)
    img.show()

denoise3()
