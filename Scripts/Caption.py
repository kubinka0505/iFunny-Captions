Image_Base = Image.new("RGBA", (2000, 2250), (255,) * 3)			# White
Image_Trans = Image.new("RGBA", (2000, 2250), (255, 255, 255, 0))	# Transparent

Draw = ImageDraw.Draw(Image_Trans)

__Fonts = ["Roboto Black", "Futura Extra Black Condensed Regular"]
if Config()["Font"]["Type"] == 1:
	__Path = "{0}\\Fonts\\{1}.otf".format(os.getcwd(), __Fonts[0])
if Config()["Font"]["Type"] == 2:
	__Path = "{0}\\Fonts\\{1}.otf".format(os.getcwd(), __Fonts[1])

if system() != "Windows":
	__Path = __Path.replace("\\", "/")

Font = ImageFont.truetype(__Path, Config()["Image"]["Max_Width"] // 10 if Config()["Font"]["Size"] == False else Config()["Font"]["Size"])

__Y = 0
for Line in wrap(Config()["Text"], width = Font.size // Config()["Wrap_Factor"] + (2 if ' '.join(Font.getname()) == __Fonts[1] else 1)):
	Draw.text(((Image_Trans.size[0] - Font.getsize(Line)[0]) // 2, __Y), text = Line, font = Font, fill = (0,) * 3, align = "center")
	#---#
	if ' '.join(Font.getname()) == __Fonts[0]: __Y += Font.size // 4 * 5
	if ' '.join(Font.getname()) == __Fonts[1]: __Y += Font.size // 5 * 6

Image_Trans = Image_Trans.crop(Image_Trans.getbbox())	# Cropped Text

Pasted = Image.new("RGBA", (Config()["Image"]["Max_Width"], Image_Trans.size[1] + Config()["Image"]["Max_Width"] // 5), (255,) * 3)
Pasted = Trans_Paste(Pasted, Image_Trans)