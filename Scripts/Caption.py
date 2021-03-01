Image_Base = Image.new("RGBA", (2000, 1500), (255,) * 3)			# White
Image_Trans = Image.new("RGBA", (2000, 1500), (255, 255, 255, 0))	# Transparent

Draw = ImageDraw.Draw(Image_Trans)

if Config()["Font"]["Type"] == 1:
	__Path = "{0}\\Fonts\\Roboto Black.otf".format(os.getcwd())
if Config()["Font"]["Type"] == 2:
	__Path = "{0}\\Fonts\\Futura Condensed Extra Bold.otf".format(os.getcwd())
if Config()["Font"]["Type"] == 3:
	__Path = "{0}\\Fonts\\Futura BT Pro Condensed Extra Black.ttf".format(os.getcwd())

if system() != "Windows":
	__Path = __Path.replace("\\", "/")

Font = ImageFont.truetype(__Path, Config()["Image"]["Max_Width"] // 10)
Draw.text((0,) * 2, text = "\n".join(wrap(Config()["Text"], Config()["Wrap"])), fill = (0,) * 3, font = Font, align = "center")

Image_Trans = Image_Trans.crop(Image_Trans.getbbox())	# Cropped Text

Pasted = Image.new("RGBA", (Config()["Image"]["Max_Width"], Image_Trans.size[1] + Config()["Image"]["Max_Width"] // 10 * 2), (255,) * 3)
Pasted = Trans_Paste(Pasted, Image_Trans)