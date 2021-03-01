Image_Base = Image.new("RGBA", (4000, 3000), (255,) * 3)			# White
Image_Trans = Image.new("RGBA", (4000, 3000), (255, 255, 255, 0))	# Transparent

Draw = ImageDraw.Draw(Image_Trans)

if Config()["Font"]["Type"] == 1:
	__Path = "{0}\\Fonts\\Roboto Black.otf".format(os.getcwd())
if Config()["Font"]["Type"] == 2:
	__Path = "{0}\\Fonts\\Limerick Serial X-Bold Regular.ttf".format(os.getcwd())

if system() != "Windows":
	__Path = __Path.replace("\\", "/")

Font = ImageFont.truetype(__Path, Config()["Font"]["Size"])
Draw.text((0,) * 2, text = "\n".join(wrap(Config()["Text"], Config()["Wrap"])), fill = (0,) * 3, font = Font, align = "center")

Image_Trans = Image_Trans.crop(Image_Trans.getbbox())	# Cropped Text
Image_Trans.show()

Pasted = Image.new("RGBA", (Image_Base.size[0] // 5, Image_Trans.size[1] + Config()["Font"]["Size"] * 2), (255,) * 3)
Pasted = Trans_Paste(Pasted, Image_Trans)