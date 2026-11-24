import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random

img = Image.new('RGBA', [1920, 1080], 'mediumaquamarine')
draw = ImageDraw.Draw(img)
txt_font1 = ImageFont.truetype("arial.ttf", 200, encoding="unic")
txt_font2 = ImageFont.truetype("arial.ttf", 85, encoding="unic")

blur = 0

x=-100
y=-150

s1 = Image.open(r'a1.png').convert("RGBA")
s1 = s1.resize((50,50))
s2 = Image.open(r'a2.png').convert("RGBA")
s2 = s2.resize((50,50))
s3 = Image.open(r'a3.png').convert("RGBA")
s3 = s3.resize((43,50))

sensei = Image.open(r'sensei_transparent.png')
sensei = sensei.resize((698,878))

title = Image.open(r'jfd.png')

i = [s1,s2,s3]

if (blur):
    for c in range(3):
        converter = ImageEnhance.Color(s1)
        s1 = converter.enhance(0.5)


for w in range(25):
    if w % 2 == 0:
        x=-100
    else:
        x=-250
    for z in range(48):
        #r=random.choice([0, 1, 2, 3])
        img.paste(i[0], (x,y), i[0])
        x+=55
        img.paste(i[1], (x,y), i[1])
        x+=55
        img.paste(i[2], (x,y), i[2])
        x+=48
    y+=55

draw.rounded_rectangle(([100,100],[1200,600]), radius=100, fill="azure", outline="grey", width=2, corners=None)
draw.rounded_rectangle(([105,105],[1195,595]), radius=100, fill="azure", outline="black", width=10, corners=None)

img.paste(title, (105+75,105), title)
draw.text((650,355), "Season 42", fill="blue", anchor="mt", font=txt_font1)

x=655
y=795

line = "I already did the harmacist joke"

color_in = "white"
color_out = "black"

draw.text((x-5,y), line, fill=color_out, anchor="mt", font=txt_font2)
draw.text((x+5,y), line, fill=color_out, anchor="mt", font=txt_font2)
draw.text((x,y-5), line, fill=color_out, anchor="mt", font=txt_font2)
draw.text((x,y+5), line, fill=color_out, anchor="mt", font=txt_font2)
draw.text((x-5,y-5), line, fill=color_out, anchor="mt", font=txt_font2)
draw.text((x+5,y+5), line, fill=color_out, anchor="mt", font=txt_font2)
draw.text((x+5,y-5), line, fill=color_out, anchor="mt", font=txt_font2)
draw.text((x-5,y+5), line, fill=color_out, anchor="mt", font=txt_font2)

draw.text((x,y), line, fill=color_in, anchor="mt", font=txt_font2)

img.paste(sensei, (1920-698,1080-878), sensei)

img.save("thumb.png")