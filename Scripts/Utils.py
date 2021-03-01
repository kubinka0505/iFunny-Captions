def BBox(Picture: Image) -> Image:
	"""Getting transparent pixels around the `Picture`."""
	Array = np.array(Picture)[:, :, :3]
	Map = np.any(Array != [255, 255, 255], axis = 2)
	Coordinates = np.argwhere(Map)
	#---#
	y0, x0, y1, x1 = *np.min(Coordinates, axis = 0), *np.max(Coordinates, axis = 0)
	return (x0, y0, x1 + 1, y1 + 1)

def Trans_Paste(Background: Image, Foreground: Image) -> Image:
	"""Pasting transparent `Foreground` to `Background`."""
	FRGRND_TRNS = Image.new("RGBA", Background.size)
	#---#
	Background_Width, Background_Height = Background.size
	Foreground_Width, Foreground_Height = Foreground.size
	#---#
	FRGRND_TRNS.paste(Foreground, ((Background_Width - Foreground_Width) // 2, (Background_Height - Foreground_Height) // 2), mask = Foreground)
	#---#
	IMG_RET = Image.alpha_composite(Background, FRGRND_TRNS)
	return IMG_RET

# GIF
def Iterate(Picture: Image) -> Image:
	"""`Picture` to iterate through."""
	try:
		Count = 0
		while 1:
			Picture.seek(Count)
			Frame = Picture.copy()
			yield Frame
			Count += 1
	except EOFError:
		pass

def Margin(Picture: Image, Top: int, Color: ImageColor = "#FFF") -> Image:
	"""Adds margin to an `Picture`."""
	Width, Height = Picture.size
	Height = Height + Top + 0
	#---#
	Field = Image.new(Picture.mode, (Width, Height), Color)
	Field.paste(Picture, (0, Top))
	return Field

def Config():
	"""Loading values from JSON file."""
	__Path = "{0}\Config.json"
	#---#
	if system() != "Windows":
		__Path = __Path.replace("\\", "/")
	#---#
	return load(open(__Path.format(os.getcwd()), encoding = "utf-8"))

def Random_String(Length: int = 16):
	"""Random string creation used in saving files."""
	return "".join(choice(printable[0:62]) for String in range(Length))
