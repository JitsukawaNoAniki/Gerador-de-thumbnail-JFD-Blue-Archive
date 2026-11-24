import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random

img = Image.new('RGBA', [1920, 1080], 'powderblue')
draw = ImageDraw.Draw(img)
txt_font1 = ImageFont.truetype("arial.ttf", 200, encoding="unic")
txt_font2 = ImageFont.truetype("arial.ttf", 90, encoding="unic")

blur = 0

x=-100
y=-150

s1 = Image.open(r'mybelovedreisa.png')
#s1 = s1.resize((50,50))

for w in range(25):
    if w % 2 == 0:
        x=-100
    else:
        x=-125
    for z in range(48):
        #r=random.choice([0, 1, 2])
        img.paste(s1, (x,y), s1)
        x+=400
    y+=280

img.save("V2thumb.png")