def Get_Service(URL: str) -> str:
	"""Scraping main Image URL from page.

	Supported Services:
	- Tenor.com
	- Giphy.com
	- Gfycat.com
	- ImgFlip.com
	- Gifer.com
	- GifImage.net
	- BestAnimations.com
	- Gif-Finder.com
	- ReactionGifs.us
	"""
	if "tenor.com/view" in URL:				return get(URL).text.split("contentUrl")[1].split("content")[0][2:].split('"')[1].replace("\\u002F", "/")
	if "giphy.com/gifs" in URL:				return "https://media"+str(get(URL).text).split("https://media")[2].split('"')[0]
	if "//gfycat.com/" in URL:				return get(URL).text.split("twitter:image")[1].split('"')[2].replace("size_restricted", "small")
	if "//imgflip.com/gif/" in URL:			return URL.replace("//", "//i.").replace("/gif", "") + ".gif"
	if "//www.pinterest." in URL:			return get(URL).text.split('"preload"')[1].split("href")[1].split('"')[1]
	if "//gifer.com/" in URL:				return "https://i.gifer.com/{0}.gif".format(URL.split("/")[-1])
	if "//gifimage.net/" in URL:			return get(URL).text.split("attachment_img")[1].split('"')[2]
	if "//bestanimations.com/gifs/" in URL:	return get(URL).text.split("meta itemprop=")[3].split('"')[3]
	if "//gif-finder.com/" in URL:			return get(URL).text.split("preload")[1].split('"')[5].replace(".mp4", ".gif")
	if "//www.reactiongifs.us/" in URL:		return get(URL).text.split("entry-content")[1].split('"')[8]
	#if "//replygif.net/" in URL:			return URL.replace("//replygif.net/", "//replygif.net/i/") + ".gif"
	else: return URL

def Get_Emoji_Image(Name: str, Style: int = 5) -> Image.open:
	"""Gets Emoji image from "emojicdn.elk.sh" API using style lists from its GitHub main page."""
	Styles = {
	1: 'apple', 2: 'google', 3: 'microsoft', 4: 'samsung',
	5: 'whatsapp', 6: 'twitter', 7: 'facebook',
	8: 'joypixels', 9: 'openmoji',  10: 'emojidex',
	11: 'lg', 12: 'htc', 13: 'mozilla'
	}
	# Styles = {Keys: Values for Keys, Values in enumerate([get("https://github.com/benborgers/emojicdn").text.split("<ul>")[2].split("<li><code>")[x+1].split("</code></li>\n")[0] for x in range(13)])}
	#---#
	Emoji_Image = Image.open(get(
		"https://emojicdn.elk.sh/{0}?style={1}".format(
			quote_plus(emojize(Name, use_aliases = True)),
			str(Styles[Style]).lower()
			), stream = True
		).raw
	)
	#---#
	ImageIO = io.BytesIO()
	Emoji_Image.save(ImageIO, "PNG")
	ImageIO.seek(0)
	return Image.open(io.BytesIO(ImageIO.read()))

def Margin(Picture: Image, Top: int, Color: ImageColor = "#FFF") -> Image:
	"""Adds margin to an `Picture`."""
	Width, Height = Picture.size
	Height = Height + Top + 0
	#---#
	Field = Image.new(Picture.mode, (Width, Height), Color)
	Field.paste(Picture, (0, Top))
	return Field

def Config() -> load:
	"""Loading values from JSON file."""
	__Path = "{0}\Config.json"
	#---#
	if system() != "Windows":
		__Path = __Path.replace("\\", "/")
	#---#
	return load(open(__Path.format(os.getcwd()), encoding = "utf-8"))

def Random_String(Length: int = 16) -> str:
	"""Random string creation used in saving files."""
	return "".join(choice(printable[0:62]) for String in range(Length))