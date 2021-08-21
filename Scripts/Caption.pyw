# Image setup

__Pasted_Color = (255,) * 3
__Fill = (0,) * 3

if Config["Settings"]["Dark_Mode"]["Enabled"]:
	if int(strftime("%H")) >= Config["Settings"]["Dark Mode"]["After Hour"]:
		__Pasted_Color = (20,) * 3
		__Fill = (160,) * 3

Image_Base = Image.new("RGBA", (1250, 5000), (0,) * 4)
Draw = ImageDraw.Draw(Image_Base)

# Automatic Max Width

Config["Image"]["Max_Width"] = 450

# Font Setup

__Font_Size = Percentage(Config["Image"]["Max_Width"], Config["Settings"]["Percentage_Elements_Size"]["Font"])
__Fonts = {Keys + 1: Values for Keys, Values in enumerate([File[:-4] for File in sorted(next(os.walk("Fonts"))[2], key = str) if File.endswith("otf")][::-1])}

if not Config["Font"]["Type"]: Config["Font"]["Type"] = randint(1, len(__Fonts))
__Path = "Fonts/{0}.otf".format(__Fonts[Config["Font"]["Type"]])
Font = ImageFont.truetype(__Path, __Font_Size)

# Emoji Setup

if Config["Font"]["Type"] == 1:
	if Config["Emoji"]["API_Type"] == 1:
		if not Config["Emoji"]["Style_if_1"]:
			__Style = 3
		else:
			__Style = Config["Emoji"]["Style_if_1"]
	if Config["Emoji"]["API_Type"] == 2:
		__Style = {"Google": "7.1"}
		Get_Emoji_Image = Get_Emoji_Image2

if Config["Font"]["Type"] == 2:
	if Config["Emoji"]["API_Type"] == 1:
		if not Config["Emoji"]["Style_if_1"]:
			__Style = 3
		else:
			__Style = Config["Emoji"]["Style_if_1"]
	if Config["Emoji"]["API_Type"] == 2:
		__Style = {"iOS": "9.3"}
		Get_Emoji_Image = Get_Emoji_Image2


if Config["Text"]["Content"] == "":
	print("\n{0}Warning{3}: {1}No text given!{3}\nInput {2}URL{3} or {2}absolute path{3} to image.\n\nPerform {2}CTRL{3} + {2}C{3}, then {2}Enter{3} when done.\nPress {2}CTRL{3} + {2}Z{3}, then {2}Enter{3} to exit.\n\nText will be stripped. Multilne supported. ({2}Enter{3})\n{4}".format(
		Styles.Yellow, Styles.LightRed, Styles.LightBlue, Styles.Reset, __BEL
		)
	)

	try:
		ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), False)
		ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
	except AttributeError:
		pass

	Lines = []
	while 1:
		try:
			Line = input("{0}> {1}".format(Styles.Green, Styles.Reset))
			Lines.append(Line)
		except KeyboardInterrupt:
			break
		except EOFError:
			raise SystemExit("Exiting.")
	if Lines:
		Lines = "\n".join(Lines).replace("\n", ". ")
		Config["Text"]["Content"] = Lines.rstrip(".") # You may put 2 dots in text instead
	else:
		raise SystemExit("No text inputted - exiting.")
	print("Finishing text input{0}\n".format(" - Generating empty caption." if not Lines else "!"))
	Config["Text"]["Content"] = "".join(Lines)

Config["Text"]["Content"] = emojize(Config["Text"]["Content"], use_aliases = True)
Config["Text"]["Content"] = Replace(Config["Text"]["Content"], Config["Text"]["Replacements"])
Config["Text"]["Content"] = Config["Text"]["Content"].strip().strip("\n")
if Config["Text"]["Content"] == "": Config["Text"]["Content"] = "あ"

# Automatic Text Wrap

Text = wrap("{0}".format(Config["Text"]["Content"]), width = 1)
Text = wrap("{0}".format(Config["Text"]["Content"]), width = Font.getsize(sorted(Text, key = len)[-1])[0] - int(Config["Text"]["Additional_Wrap"]))

# Caption Setup

Images = []
Expanded_Images = []

for Line in Text:
	Line_Image = Image.new("RGBA", (Font.getsize("x")[0] * len(Line) * 2, Font.getsize("qÓ")[1] * 2))
	Line_ImageDraw = ImageDraw.Draw(Line_Image)
	__X = 0
	#---#
	for Character in Line:
		if Character in UNICODE_EMOJI_ENGLISH:
			try:
				Emoji = Get_Emoji_Image(
					demojize(Character),
					__Style,
					)
			except UnidentifiedImageError as Error:
				raise SystemExit("{0}: The `{1}` emoji is not supported on this style. Image processing aborted.".format(
					Error.__class__.__name__,
					demojize(Character),
						)
					)
			#---#
			Emoji = Emoji.resize(
				(Percentage(Font.getsize("qÓ")[1], Config["Settings"]["Percentage_Elements_Size"]["Emojis"]),) * 2,
				Image.LANCZOS
				)
			#---#
			Line_Image.paste(
				Emoji,
				(__X, Percentage(Font.getsize("pÓ")[1], Config["Settings"]["Percentage_Elements_Size"]["Emoji_Height_Spacing"])),
				Emoji
				)
			__X += Emoji.size[0] + Config["Text"]["Kerning"]
			Character = Character.replace(Character, "")
		#---#
		Line_ImageDraw.text(
			xy = (__X, 5),
			text = Character,
			font = Font,
			fill = __Fill
			)
		#---#
		__X += Font.getsize(Character)[0] + Config["Text"]["Kerning"]
		#---#
	Line_Image = Line_Image.crop(Line_Image.getbbox())
	Images.append(Line_Image)

# Text Alignment

for IMG in range(len(Images)):
	Text_Image = Image.new("RGBA", (Images[IMG].size[0], Images[IMG].size[1] + Font.getsize("Ó")[1] + len(Images) * 10), (0,) * 4) # Bug
	Text_Image.paste(Images[IMG], (0, Font.getsize("qÓ")[1]), Images[IMG])
	Expanded_Images.append(Text_Image)

__Y = 0
for IMG in range(len(Expanded_Images)):
	if IMG == len(Expanded_Images): __Y += Expanded_Images[0].size[1] // len(Expanded_Images)
	else: __Y += Percentage(Font.getsize("qÓ")[1], Config["Settings"]["Percentage_Elements_Size"]["Leading"]) + 5
	Image_Base.paste(Expanded_Images[IMG], ((Image_Base.size[0] - Expanded_Images[IMG].size[0]) // 2, __Y), Expanded_Images[IMG])
	

# Caption Field Setup

Image_Base = Image_Base.crop(Image_Base.getbbox())

Pasted = Image.new("RGBA", (Config["Image"]["Max_Width"], Image_Base.size[1] + Percentage(Font.getsize("qÓ")[1], Config["Settings"]["Percentage_Elements_Size"]["Caption_Field_Height"])), __Pasted_Color)
Pasted.paste(Image_Base, ((Pasted.size[0] - Image_Base.size[0]) // 2, (Pasted.size[1] - Image_Base.size[1]) // 2), Image_Base)
