from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from os import listdir, path, makedirs
from os.path import isfile, join

fontpath = "fonts"
destpath = "images"

fontfiles = [f for f in listdir(fontpath) if isfile(join(fontpath, f))]
digits = [u"১", u"২", u"৩", u"৪", u"৫", u"৬", u"৭", u"৮", u"৯"]

if not path.exists(destpath):
    makedirs(destpath)

for fontfile in fontfiles:
	for digit in digits:
		filename = fontfile.split(".")[0] + "_" + str(digit)
		img = Image.new("RGB", (28, 28), "white")
		img.save(destpath + "/" + filename + ".bmp")
		img = Image.open(destpath + "/" + filename + ".bmp")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(fontpath + "/" + fontfile, 28)
		draw.text((0, 0), digit, (0, 0, 0), font=font)
		img.save(destpath + "/" + filename + ".bmp")