if Config["Settings"]["Dark_Mode"]["Enabled"] == True:
	if int(strftime("%H")) >= Config["Settings"]["Dark_Mode"]["After_Hour"]:
		__Pasted_Color = (20,) * 3
		__Fill = (128,) * 3
else:
	__Pasted_Color = (255,) * 3
	__Fill = (0,) * 3

Image_Trans = Image.new("RGBA", (1250, 5000), (0,) * 4)

Draw = ImageDraw.Draw(Image_Trans)

__Fonts = [File[:-4] for File in os.listdir(os.getcwd() + __SLASH + "Fonts") if File.endswith("otf")][::-1]
if Config["Font"]["Type"] == 1:
	__Path = r"{0}\Fonts\{1}.otf".format(os.getcwd(), __Fonts[0])
if Config["Font"]["Type"] == 2:
	__Path = r"{0}\Fonts\{1}.otf".format(os.getcwd(), __Fonts[1])
	
if system() != "Windows":
	__Path = __Path.replace("\\", "/")

Font = ImageFont.truetype(__Path, Config["Image"]["Max_Width"] // 10 if Config["Font"]["Size"] == False else Config["Font"]["Size"])

__Y = 0

for Line in wrap(Config["Text"]["Content"], width = Font.size // Config["Text"]["Wrap_Factor"] + (4 if ' '.join(Font.getname()) == __Fonts[1] else 1)):
	Draw.text(((Image_Trans.size[0] - Font.getsize(Line)[0]) // 2, __Y), text = Line, font = Font, fill = __Fill, align = "center")
	#---#
	__Y += Font.size // 5 * 6 
	#__Y += eval("+".join([str(Element) for Element in list(Font.getmask("|").getbbox())])) // 6 * 5

Image_Trans = Image_Trans.crop(Image_Trans.getbbox())

Pasted = Image.new("RGBA", (Config["Image"]["Max_Width"], Image_Trans.size[1] + Config["Image"]["Max_Width"] // 6), __Pasted_Color)
Pasted = Trans_Paste(Pasted, Image_Trans)