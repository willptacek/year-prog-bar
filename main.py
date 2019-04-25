from PIL import Image, ImageDraw, ImageFont
import datetime
#Will Ptacek
x = datetime.datetime.now()
pixelPerDate = 800 / 366

dateNum = float(x.strftime("%j"))
datePixel = pixelPerDate * dateNum + 100
img = Image.new('RGB', (1000, 400), color = 'white')
img.save('prog_bar.png')
im = Image.open('prog_bar.png')

draw = ImageDraw.Draw(im)
draw.polygon([(100, 300), (900, 300), (900, 100), (100, 100)], outline = 'black')
draw.polygon([(100, 300), (datePixel, 300), (datePixel, 100), (100, 100)], fill = 'green')


draw.text((400, 350), "The year is " + str(dateNum / 365) + " done.", fill = 'black')
del draw

im.save('prog_bar.png')