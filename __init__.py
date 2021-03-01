"""iFunny Captions Generator.

Pack of scripts providing iFunny Captions
generation, but this time You can input your
own text and picture using `Config.json` file."""

__STA_TIME = __import__("time").time()
import re, os, io
from requests import get
from textwrap import wrap
from platform import system
from string import printable
from datetime import timedelta
from json import load, decoder
from random import choice, randint
from urllib.parse import quote_plus
from time import sleep, strftime, time
from emoji import emojize, demojize, UNICODE_EMOJI
from PIL import Image, ImageColor, ImageDraw, ImageFile, ImageFont, UnidentifiedImageError

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= [__author__, "SuperCuber"]
__version__		= "2.8"
__date__		= "21.12.2020"
__status__		= "Development"
__license__		= "GPL V3	"

__FORMAT = "png"
__SLASH = "/"

# Opening Scripts/Utils.py

print("Setting up utils...")
exec(open("{0}/Scripts/Utils.py".format(os.getcwd(), __SLASH)).read())
try:
	Config = Config()
except decoder.JSONDecodeError as Error:
	raise SystemExit("Haven't You forgot something? (Position {0})".format(Error.__dict__["pos"]))

ImageFile.LOAD_TRUNCATED_IMAGES = True
__STA_TIME = timedelta(seconds = time() - __STA_TIME)

# Error Handling

try:
	with get(Get_Service(Config["Image"]["URL / Path"])) as Site:
		if Site.status_code != 200:
			exit("\nURL returns status code {0} ({1}).\nImage will not be processed.".format(Site.status_code, Site.reason.title()))
except:
	pass

# Getting FFmpeg Location

if Config["Settings"]["FFmpeg_Location"] == "":
	for File in next(os.walk(os.getcwd()))[2]:
		if os.path.basename(File)[:6] == "ffmpeg":
			__FFMPEG = os.getcwd() + "/" + File
else:
	__FFMPEG = Config["Settings"]["FFmpeg_Location"]

#-------------------------#

# Image to Frames conversion

__CNV_TIME = time()

print("Converting {0} Image to Frames... (This can take a while)".format("URL" if Config["Image"]["URL / Path"].startswith("http") else "Path"))
os.system("{0} -i {1} {2}Frame_%06d.{3} -hide_banner -loglevel panic".format(
		__FFMPEG,
		Get_Service(Config["Image"]["URL / Path"]),
		"-vf select='not(mod(n\,2))' " if Config["Settings"]["Delay"] == 1 else "",
		__FORMAT)
		)

__CNV_TIME = timedelta(seconds = time() - __CNV_TIME)

Frames = [File for File in next(os.walk(os.getcwd()))[2] if File.endswith(__FORMAT)]
Frames.sort(key = str)

#-------------------------#

# GIF Making Process

print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))
__MKE_TIME = time()
for Frame in Frames:
	Caption = Image.open(Frame)
	#---#
	exec(open("{0}{1}Scripts{1}Caption.py".format(os.getcwd(), __SLASH)).read())	
	exec(open("{0}{1}Scripts{1}Gifer.py".format(os.getcwd(), __SLASH)).read())
	#---#
	# if Config["Settings"]["Optimize"] == True: Captionized = Captionized.convert(mode = "P", palette = Image.ADAPTIVE)
	Captionized.save(Frame)
__MKE_TIME = timedelta(seconds = time() - __MKE_TIME)

print("Saving {0}...".format("PNG" if len(Frames) == 1 else "GIF"))

#-------------------------#

# Image Name

__NAME = "{0}_{1}.{2}".format(
	re.compile("[^a-zA-Z0-9]").sub("_", str(Config["Text"]["Content"]))[:192],
	Random_String(8),
	"png" if len(Frames) == 1 else "gif"
	)

# Saving Image

__SAV_TIME = time()
if len(Frames) == 1:
	GIF = Image.open(Frames[0])
	GIF.save("{0}/Images/{1}".format(
		os.getcwd(), __NAME))

#-------------------------#

# GIF Optimizing

if not len(Frames) == 1:
	os.system("{0} -i Frame_%06d.png -vf palettegen=reserve_transparent=1 Palette.png -y -hide_banner -loglevel panic".format(__FFMPEG))
	os.system("{0} -i Frame_%06d.png -i Palette.png -lavfi paletteuse=alpha_threshold=128 -gifflags -offsetting Images/{1} -y -hide_banner -loglevel panic".format(__FFMPEG, __NAME))
	os.system("gifsicle --careful {0}-b Images/{1} -w".format("" if Config["Settings"]["Delay"] == "0" else "-d{0} ".format("2" if Config["Settings"]["Delay"] == "1" else Config["Settings"]["Delay"]), __NAME))
	#---#
	if Config["Settings"]["Optimize"]["Enabled"] == True:
		print("Optimizing...")
		os.system("gifsicle --careful -b -O3 --lossy={0} Images/{1} -w".format(Config["Settings"]["Optimize"]["Lossy"], __NAME))

__SAV_TIME = timedelta(seconds = time() - __SAV_TIME)

#-------------------------#

# Frames Removal

print("Removing {0}...".format("Image" if len(Frames) == 1 else "Frames"))
__REM_TIME = time()
[os.remove("{0}/{1}".format(os.getcwd(), Frame)) for Frame in next(os.walk(os.getcwd()))[2] if Frame.endswith(__FORMAT)]
__REM_TIME = timedelta(seconds = time() - __REM_TIME)
print("Done!")

#-------------------------#

# `Time_Logs` Output

if Config["Settings"]["Time_Logs"] == True:
	print("\nModules were loaded in:\t\t\t{0}.".format(str(__STA_TIME)[2:]))
	print("Input {0} was converted to frames in:\t{1}.".format("file" if not Config["Image"]["URL / Path"].startswith("http") else "URL", str(__CNV_TIME)[2:]))
	print("Frames were processed in:\t\t{0}.".format(str(__MKE_TIME)[2:]))
	print("{0} was made in:\t\t\t{1}.".format("PNG" if len(Frames) == 1 else "GIF", str(__SAV_TIME)[2:]))
	print("Frames were deleted in:\t\t\t{0}.".format(str(__REM_TIME)[2:]))
	print("All operations were done in:\t\t{0}.".format(str(__STA_TIME + __CNV_TIME + __MKE_TIME + __SAV_TIME + __REM_TIME)[2:]))
