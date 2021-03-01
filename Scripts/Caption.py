# Image setup

__Pasted_Color = (255,) * 3
__Fill = (0,) * 3

if Config["Settings"]["Dark_Mode"]["Enabled"] == True:
	if int(strftime("%H")) >= Config["Settings"]["Dark_Mode"]["After_Hour"]:
		__Pasted_Color = (20,) * 3
		__Fill = (160,) * 3

Image_Base = Image.new("RGBA", (1250, 5000), (0,) * 4)
Draw = ImageDraw.Draw(Image_Base)

# Automatic Max Width

Config["Image"]["Max_Width"] = 450
#Config["Image"]["Max_Width"] = Image.open(Frames[0]).size[0]

# Font Size Setup

__Font_Size = Config["Image"]["Max_Width"] // 10

# Font & Emoji Style Setup

__Fonts = {Keys + 1: Values for Keys, Values in enumerate([File[:-4] for File in next(os.walk(os.getcwd() + "/Fonts"))[2] if File.endswith("otf")][::-1])}

if Config["Font"]["Type"] == 1:
	__Style = 3
if Config["Font"]["Type"] == 2:
	__Style = 1

if Config["Text"]["Emoji_Style"] != False: __Style = int(Config["Text"]["Emoji_Style"])

__Path = "{0}/Fonts/{1}.otf".format(os.getcwd(), __Fonts[Config["Font"]["Type"]])
Font = ImageFont.truetype(__Path, __Font_Size)

# Automatic Text Wrap

Text = wrap(emojize(r"{0}".format(Config["Text"]["Content"]), use_aliases=True), width = 1)
Text = wrap(emojize(r"{0}".format(Config["Text"]["Content"]), use_aliases=True), width = Font.getsize(sorted(Text, key=len)[-1])[0] - int(Config["Text"]["Additional_Wrap"]))

# Caption Setup

__Styles = {Key: Value for Key, Value in enumerate([Get_Emoji_Image.__code__.co_consts[x+1] for x in range(len(Get_Emoji_Image.__code__.co_consts[14]))])}
Images = []

__Y = 0

for Line in Text:
	Line_Image = Image_Base.copy()
	Line_ImageDraw = ImageDraw.Draw(Line_Image)
	__X = 0
	#---#
	for Character in Line:
		if Character in UNICODE_EMOJI:
			try:
				Emoji = Get_Emoji_Image(
					demojize(Character),
					__Style,
					)
			except UnidentifiedImageError as Error:
				raise SystemExit("{0}: The `{1}` emoji is not supported on the {2} style. Image processing aborted.".format(
					Error.__class__.__name__,
					demojize(Character),
					__Style.title(),
						)
					)
			#---#
			Emoji = Emoji.resize(
				(Font.getsize("|")[1],) * 2,
				Image.LANCZOS
				)
			#---#
			Line_Image.paste(
				Emoji,
				(__X, 0),
				Emoji
				)
			__X += Emoji.size[0]
			Character = Character.replace(Character, "")
		#---#
		Line_ImageDraw.text(
			xy = (__X, 0),
			text = Character,
			font = Font,
			fill = __Fill
			)
		#---#
		__X += Font.getsize(Character)[0]
		#---#
	__Y += Font.getsize(Line)[1]
	Line_Image = Line_Image.crop(Line_Image.getbbox())
	Images.append(Line_Image)

# Text Alignment

__Y = 0
for IMG in range(len(Images)):
	__Y += Font.getsize("|")[1] // 6 * 7
	Image_Base.paste(Images[IMG], ((Image_Base.size[0] - Images[IMG].size[0]) // 2, __Y), Images[IMG])

# Caption Field Setup

Image_Base = Image_Base.crop(Image_Base.getbbox())

Pasted = Image.new("RGBA", (Config["Image"]["Max_Width"], Image_Base.size[1] + Config["Image"]["Max_Width"] // 6), __Pasted_Color)
Pasted.paste(Image_Base, ((Pasted.size[0] - Image_Base.size[0]) // 2, (Pasted.size[1] - Image_Base.size[1]) // 2), Image_Base)
