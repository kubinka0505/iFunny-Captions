def Get_Service(URL: str) -> str:
	"""Scraping main Image URL from various pages.
	
	Commented statements are deprecated but may work.
	Enable on your own responsibility"""
	if "//" in URL:
		if "tenor.com/view" in URL:				URL = get(URL).text.split("contentUrl")[1].replace("\\u002F", "/").split('"')[2]
		if "giphy.com/gifs" in URL:				URL = "https://media" + str(get(URL).text).split("https://media")[2].split('"')[0]
		if "gfycat.com/" in URL:				URL = get(URL).text.split("twitter:image")[1].split('"')[2].replace("size_restricted", "small")
		if "imgflip.com/gif/" in URL:			URL = URL.replace("//", "//i.").replace("/gif", "") + ".gif"
		#if "www.pinterest." in URL:			URL = get(URL).text.split('"preload"')[1].split("href")[1].split('"')[1]
		#if "gifer.com/" in URL:				URL = "https://i.gifer.com/{0}.gif".format(URL.split("/")[-1])
		if "gifimage.net/" in URL:				URL = get(URL).text.split("attachment_img")[1].split('"')[2]
		if "bestanimations.com/gifs/" in URL:	URL = get(URL).text.split("meta itemprop=")[3].split('"')[3]
		if "gif-finder.com/" in URL:			URL = get(URL).text.split("preload")[1].split('"')[5].replace(".mp4", ".gif")
		if "www.reactiongifs.us/" in URL:		URL = get(URL).text.split("entry-content")[1].split('"')[8]
		if "preview.redd.it/" in URL:			URL = "https://i.redd.it/" + URL.split("/")[3]
		#if "replygif.net/" in URL:				URL = URL.replace("//replygif.net/", "//replygif.net/i/") + ".gif"
		try:
			URL = URL.split("?")[0].split("#")[0]
		except:
			pass
	else:
		return URL
	return URL

def Get_Emoji_Image(Name: str, Style: int = 5) -> Image.open:
	"""Gets Emoji image from "emojicdn.elk.sh" API using style lists from its GitHub main page"""
	Styles = {
		1: 'apple', 2: 'google', 3: 'microsoft', 4: 'samsung',
		5: 'whatsapp', 6: 'twitter', 7: 'facebook',
		8: 'joypixels', 9: 'openmoji',	10: 'emojidex',
		11: 'lg', 12: 'htc', 13: 'mozilla'
	}
	# Styles = {Keys: Values for Keys, Values in enumerate([get("http://github.com/benborgers/emojicdn").text.split("<ul>")[2].split("<li><code>")[x + 1].split("</code></li>\n")[0] for x in range(13)])}
	#---#
	Emoji_Image = Image.open(get(
		"https://emojicdn.elk.sh/{0}?style={1}".format(
			quote_plus(emojize(Name, use_aliases = 1)),
			str(Styles[Style]).lower()
			), stream = 1
		).raw
	).convert("RGBA")
	#---#
	ImageIO = io.BytesIO()
	Emoji_Image.save(ImageIO, "PNG")
	ImageIO.seek(0)
	return Image.open(io.BytesIO(ImageIO.read()))

def Get_Emoji_Image2(Name: str, Info: dict) -> Image.open:
	"""Gets Emoji image from `auepa` API"""
	Emoji_Image = Utils.center_image(Utils.get_image(Name, Info))
	#---#
	ImageIO = io.BytesIO()
	Emoji_Image.save(ImageIO, "PNG")
	ImageIO.seek(0)
	return Image.open(io.BytesIO(ImageIO.read()))

def Margin(Picture: Image, Top: int, Color = "#FFF") -> Image:
	"""Adds margin to the `Picture`"""
	Width, Height = Picture.size
	Height = Height + Top + 0
	#---#
	Field = Image.new(Picture.mode, (Width, Height), Color)
	Field.paste(Picture, (0, Top))
	return Field

def Percentage(Whole: float, Percent: float) -> float:
	"""Calculates `Percent` of `Whole`"""
	return int((Percent * Whole) / 1E2)

def Random_String(Length: int = 16) -> str:
	"""Random string creation used in saving files"""
	return "".join(choice(printable[0:62]) for String in range(Length))

def Replace(String: str, Phrases: dict):
	"""Batch string replacement"""
	pattern = re.compile("|".join([re.escape(x) for x in sorted(Phrases, key = len, reverse = 1)]), flags = re.DOTALL)
	return pattern.sub(lambda x: Phrases[x.group(0)], String)

def Variable_Search(Variable: str = "Path", Delimiter: str = os.pathsep, Content: str = "") -> str:
	"""Searches for `Content` in `Variable` environment variable"""
	try:
		Variables = os.environ[Variable]
		for Variable in Variables.split(Delimiter):
			if Content.lower() in Variable.lower():
				return Variable
	except KeyError:
		return None

def Remove_Pictures(Directory: os.path.abspath = ".", Format: str = "png") -> os.remove:
	"""Removes files ending with `Format` from `Directory`"""
	for Frame in next(os.walk(os.path.abspath(Directory)))[2]:
		if Frame.endswith(Format):
			os.chmod(Frame, 511)
			os.remove(Frame)
	return

def File_Size(Bytes: float) -> str:
	"""Returns human-readable file size"""
	for Unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
		if Bytes < 1024.: break
		Bytes /= 1024.
	return "{0} {1}".format(round(Bytes, 2), Unit)

def Grayscale(Path: os.path.abspath) -> bool:
	"""Checks if image can be converted into a grayscale color palette"""
	Picture = Image.open(Path).convert("RGB")
	#---#
	RGB = Picture.split()
	for Color in range(1, 2 + 1):
		if ImageChops.difference(RGB[0], RGB[Color]).getextrema()[1] != 0:
			return
	return 1

def Delay(Image_OBJ) -> int:
	"""Pseudo-automatic calculation of the average GIF image delay"""
	return int(math.ceil(math.sqrt(1E3 / Image_OBJ.info["duration"])))

def ArgParseBool(Boolean: bool) -> str:
	"""Converts default bool type to argument parser one"""
	return "store_" + str(not bool(Boolean)).lower()

def Get_Path(Path: str) -> os.path.abspath:
	"""Absolute path getter with additional user and variables expansion"""
	return os.path.abspath(os.path.expanduser(os.path.expandvars(Path)))