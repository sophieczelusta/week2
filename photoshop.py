from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import time

def preview(img):
    print("You will be shown a preview of your image. When done, please exit the window and return to the command line.")
    print("You may need to wait a moment after viewing the picture.")
    time.sleep(3)
    img.show()
    save = input("Would you like to save the picture? ")
    if save == "yes":
        save = input("Choose a name to save your picture as, including the file type. ")
        img.save(save)
        retry = input("Your image has been saved. Would you like to try again? ")
        if retry == "yes":
            photoshop()
        elif retry == "no":
            retry = retry
    else:
        retry = input("Would you like to retry? ")
        if retry == "yes":
            photoshop()
        elif retry == "no":
            retry = retry

def lighten(pic,amount):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(int(r*amount),int(g*amount),int(b*amount)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)


def darken(pic,amount):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(int(r*0.8),int(g*0.8),int(b*0.8)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)

def grayscale(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(int((r + g + b) / 3),int((r + g + b) / 3),int((r + g + b) / 3)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)

def solarer(x):
    if x < 128:
        x = 255 - x
        return x
    else:
        return x

def solarize(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(solarer(r),solarer(g),solarer(b)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)

def posterer(x):
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

def posterize(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(posterer(r),posterer(g),posterer(b)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)

def invert(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(255 - r,255 - g,255 - b) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)

def contrast(pic,amount):
    img = Image.open(pic)
    img = img.convert("RGBA")
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(amount)
    preview(img)

def saturation(pic,amount):
    img = Image.open(pic)
    img = img.convert("RGBA")
    color = ImageEnhance.Color(img)
    img = color.enhance(amount)
    preview(img)

def blur(pic,amount):
    img = Image.open(pic)
    img = img.convert("RGBA")
    img = img.filter(ImageFilter.GaussianBlur(radius=amount))
    preview(img)

def sharp(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    img = img.filter(ImageFilter.SHARPEN)
    preview(img)

def crop(pic,left,top,right,bottom):
    left = left / 100
    right = 1 - (right / 100)
    bottom = 1 - (bottom / 100)
    top = top / 100
    img = Image.open(pic)
    w,h = img.size
    img = img.crop((left * w, top * h, right * w, bottom * h))
    preview(img)

def additive(x):
    if x < 175:
        x = x + 75
        return x
    else:
        x = 255
        return x

def warm(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(additive(r),g,b) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)

def cool(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(r,g,additive(b)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    preview(img)

def silvered(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(int((r + g + b) / 3),int((r + g + b) / 3),int((r + g + b) / 3)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.6)
    preview(img)

def poppy(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    color = ImageEnhance.Color(img)
    img = color.enhance(1.8)
    pixels = [(int(r*1.1),int(g*1.1),int(b*1.1)) for (r,g,b,a) in img.getdata()] #light
    img.putdata(pixels)
    img = img.filter(ImageFilter.SHARPEN)
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.3)
    preview(img)

def ramp(white):
    ramp = []
    r,g,b = white
    for i in range(255):
        ramp.extend((int(r*i/255),int(g*i/255),int(b*i/255)))
    return ramp

def sepia(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    sepia = ramp((255,233,190))
    if img.mode != "L":
        img = img.convert("L")
    img = ImageOps.autocontrast(img)
    img.putpalette(sepia)
    img = img.convert("RGB")
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.6)
    preview(img)

def underwater(pic):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(r,additive(g),255) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.3)
    preview(img)


def photoshop():
    print("Welcome to Photoshop!")
    pic = input("Please enter the name of the picture you would like to edit, including the file type. ")
    adjustment = input("""Choose one of the following adjustments:
1. Brightness
2. Grayscale
3. Solarize
4. Posterize
5. Invert
6. Contrast
7. Saturation
8. Blur
9. Sharpen
10. Crop
11. Filters
""")

    if adjustment == "1": #light/dark
        adjustment = input("Would you like to lighten or darken your image? ")
        amount = float(input("By how much? Enter a number between 1 and 10. "))
        if adjustment == "lighten":
            amount = (amount / 10) + 1
            lighten(pic,amount)
        elif adjustment == "darken":
            amount = 1 - (amount / 10)
            darken(pic,amount)
        else:
            print("Error 404. Adjustment not found.")

    elif adjustment == "2": #grayscale
        grayscale(pic)

    elif adjustment == "3":
        solarize(pic)

    elif adjustment == "4":
        posterize(pic)

    elif adjustment == "5":
        invert(pic)

    elif adjustment == "6":
        print("Please choose a number between 0 and 5 to enhance the contrast of your picture by. ")
        amount = float(input("Any number less than 1 will decrease the contrast. "))
        contrast(pic,amount)

    elif adjustment == "7":
        print("Please choose a number between 0 and 5 to enhance the saturation of your picture by.")
        amount = float(input("Any number less than one will decrease the saturation. "))
        saturation(pic,amount)

    elif adjustment == "8":
        amount = float(input("Please choose a blur radius between 0 and 20. "))
        blur(pic,amount)

    elif adjustment == "9":
        sharp(pic)

    elif adjustment == "10":
        print("Choose a number between 1 and 100 to remove that percentage from one edge of the picture.")
        rightedge = float(input("The right edge: "))
        leftedge = float(input("The left edge: "))
        topedge = float(input("The top edge: "))
        bottomedge = float(input("The bottom edge: "))
        crop(pic,leftedge,topedge,rightedge,bottomedge)

    elif adjustment == "11":
        adjustment = input("""Choose one of the following filters:
1. Warm
2. Cool
3. Silvered
4. Vibrant
5. Sepia
6. Underwater
""")
        if adjustment == "1":
            warm(pic)
        elif adjustment == "2":
            cool(pic)
        elif adjustment == "3":
            silvered(pic)
        elif adjustment == "4":
            poppy(pic)
        elif adjustment == "5":
            sepia(pic)
        elif adjustment == "6":
            underwater(pic)
        else:
            print("Error 404. Adjustment not found.")

    else:
        print("Error 404. Adjustment not found.")

if __name__ == '__main__':
    print
    photoshop()
