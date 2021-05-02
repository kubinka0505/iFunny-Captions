"""iFunny Captions Generator.

Pack of scripts providing iFunny Captions
generation, but this time You can input your
own text and picture using `Config.json` file."""

__STA_TIME = __import__("time").time()
import re, os, io
from auepa import Utils
from requests import get
from textwrap import wrap
from platform import system
from shutil import copyfile
from time import sleep, time
from string import printable
from json import load, decoder
from datetime import timedelta
from random import choice, randint
from urllib.parse import quote_plus
from emoji import emojize, demojize, UNICODE_EMOJI_ENGLISH
from requests.exceptions import InvalidSchema, MissingSchema
from PIL import Image, ImageColor, ImageDraw, ImageFile, ImageFont, PngImagePlugin, UnidentifiedImageError

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= [__author__, "SuperCuber"]
__version__		= "3.0"
__date__		= "02.05.2021"
__status__		= "Mature"
__license__		= "GPL V3"

__BaseDir	= os.path.abspath(os.path.dirname(__file__))
__TEMP		= os.getenv("Temp") if system() == "Windows" else "/tmp"
__Folders	= [__TEMP, "iFunny_Cache", "Captions", "Frames"]

for Folder in __Folders:
	try: os.mkdir(Folder)
	except FileExistsError: pass
	os.chdir(Folder)

__Format = "png"
os.chdir(__BaseDir)

#-------------------------#

# Opening Scripts/Utils.pyw

print("Setting up utils...")
[os.remove(Frame) for Frame in next(os.walk("."))[2] if Frame.endswith(__Format)]
exec(open("Scripts/Utils.pyw", encoding = "utf-8").read())

try: Config = load(open("Config.json", encoding = "utf-8"))
except decoder.JSONDecodeError as Error: raise SystemExit("{2}Haven't You forgot something?{4} (Line {3}{0}{4} / Position {3}{1}{4})".format(Error.__dict__["lineno"], Error.__dict__["pos"], Styles.Yellow, Styles.Red, Styles.Reset))

__BEL = "" if Config["Settings"]["Sound"] else ""

class Styles():
	"""Colored Prints."""
	Red		= "\033[31m" if Config["Settings"]["Colored Prints"] else ""
	Green	= "\033[32m" if Config["Settings"]["Colored Prints"] else ""
	Yellow	= "\033[33m" if Config["Settings"]["Colored Prints"] else ""
	Cyan	= "\033[36m" if Config["Settings"]["Colored Prints"] else ""
	Reset	= "\033[0m" if Config["Settings"]["Colored Prints"] else ""

try: os.mkdir("Images")
except FileExistsError: pass

ImageFile.LOAD_TRUNCATED_IMAGES = True
__STA_TIME = timedelta(seconds = time() - __STA_TIME)

# Error Handling

try:
	with get(Get_Service(Config["Image"]["URL / Path"])) as Site:
		if not Site.ok:
			raise SystemExit("\nURL returns status code {2}{0}{3} ({2}{1}{3}).\n{2}Image will not be processed.{3}{4}".format(Site.status_code, Site.reason.title(), Styles.Red, Styles.Reset, __BEL))
except MissingSchema:
	raise SystemExit("\n{0}Invalid URL{2}!\n{1}Image will not be processed.{2}{3}".format(Styles.Yellow, Styles.Red, Styles.Reset, __BEL))
except InvalidSchema:
	pass

# Getting Packages Location

if not Config["Settings"]["Packages"]["Location"]["FFmpeg"]:
	for File in next(os.walk("."))[2]:
		if os.path.basename(File)[:6] == "ffmpeg":
			try:
				__FFmpeg = os.path.abspath(File)
			except:
				pass
	else:
		for Key, Value in os.environ.items():
			if "ffmpeg" in Value:
				__FFmpeg = os.path.abspath(Value)
				print('\n{1}FFmpeg{3} was found in the "{2}{0}{3}" environment variable!'.format(Key, Styles.Green, Styles.Cyan, Styles.Reset))
				break
else:
	__FFmpeg = os.path.abspath(Config["Settings"]["Packages"]["Location"]["FFmpeg"])
	if os.path.isfile(__FFmpeg):
		pass
	else:
		raise SystemExit("\n{0}FFmpeg{2} not found!\n{1}Image will not be processed.{2}{3}".format(Styles.Yellow, Styles.Red, Styles.Reset, __BEL))

if not Config["Settings"]["Packages"]["Location"]["Gifsicle"]:
	for File in next(os.walk("."))[2]:
		if os.path.basename(File)[:8] == "gifsicle":
			try:
				__Gifsicle = os.path.abspath(File)
			except:
				pass
	else:
		for Key, Value in os.environ.items():
			if "gifsicle" in Value:
				__Gifsicle = os.path.abspath(Value)
				print('{1}Gifsicle{3} was found in the "{2}{0}{3}" environment variable!\n'.format(Key, Styles.Green, Styles.Cyan, Styles.Reset))
				break
else:
	__Gifsicle = os.path.abspath(Config["Settings"]["Packages"]["Location"]["Gifsicle"])
	if os.path.isfile(__Gifsicle):
		pass
	else:
		raise SystemExit("\n{0}Gifsicle{2} not found!\n{1}Image will not be processed.{2}{3}".format(Styles.Yellow, Styles.Red, Styles.Reset, __BEL))

#-------------------------#

# Folder Name

__Folder_Name = re.compile("[^a-zA-Z0-9]").sub("_", str(Get_Service("".join(Config["Image"]["URL / Path"].split("//")[1:]))))

if not __Folder_Name:
	__Folder_Name = re.compile("[^a-zA-Z0-9]").sub("_", str("".join(Config["Image"]["URL / Path"])))
else:
	pass

__Folder_Name = __Folder_Name[:100]

# Image to Frames conversion & Cache System

__CNV_TIME = time()

os.chdir(os.sep.join(__Folders))
if __Folder_Name in next(os.walk("."))[1]:
	os.chdir(__Folder_Name)
	print("{0}URL was located in cache folder!{1}".format(Styles.Green, Styles.Reset))
else:
	os.mkdir(__Folder_Name)
	os.chdir(__Folder_Name)
	print("{0}URL was not located in cache folder!{1}".format(Styles.Yellow, Styles.Reset))
	print("Converting {0} Image to Frames... {1}(This can take a while){2}".format("URL" if Config["Image"]["URL / Path"].startswith("http") else "Path", Styles.Yellow, Styles.Reset))
	try:
		os.system('{0} -i "{1}" {2} -hide_banner -loglevel panic'.format(
				__FFmpeg,
				Get_Service(Config["Image"]["URL / Path"]),
				"Frame.{0}".format(__Format) if not Get_Service(Config["Image"]["URL / Path"]).endswith("gif") else "{0}Frame_%05d.{1}".format("-vf select='not(mod(n\,2))' " if Config["Settings"]["Delay"] == 1 else "", __Format)
				))
	except KeyboardInterrupt:
		print("{1}WARNING{2}: User interrupted the frames conversion process. Converted {1}{0}{2} frames so far.{3}".format(str(len([File for File in next(os.walk("."))[2] if File.endswith(__Format)])), Styles.Yellow, Styles.Reset, __BEL))
		pass

print("Copying files to main directory...")

for File in next(os.walk("."))[2]:
	if File.endswith(__Format):
		try:
			copyfile(os.path.abspath(File), __BaseDir + os.sep + File)
			#print(File)
			#os.rename(File, "Frame_{0}.png".format(str(__FileToCopy.index(File)).zfill(5)))
		except KeyboardInterrupt:
			print("{1}WARNING{2}: User interrupted the frames copying process. Copied {1}{0}{2} frames so far.{3}".format(str(len([File for File in next(os.walk("."))[2] if File.endswith(__Format)])), Styles.Yellow, Styles.Reset, __BEL))
			pass

os.chdir(__BaseDir)
__CNV_TIME = timedelta(seconds = time() - __CNV_TIME)

Frames = [File for File in next(os.walk("."))[2] if File.endswith(__Format)]
Frames.sort(key = str)

#-------------------------#

# GIF Making Process

print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))
__MKE_TIME = time()
for Frame in Frames:
	try:
		Caption = Image.open(Frame)
		#---#
		exec(open("Scripts/Caption.pyw", encoding = "utf-8").read())	
		exec(open("Scripts/Gifer.pyw", encoding = "utf-8").read())
		#---#
		# if Config["Settings"]["Optimize"]: Captionized = Captionized.convert(mode = "P", palette = Image.ADAPTIVE)
		Captionized.save(Frame)
	except FileNotFoundError:
		pass
__MKE_TIME = timedelta(seconds = time() - __MKE_TIME)

print("Saving {0}...{1}".format("PNG" if len(Frames) == 1 else "GIF", Styles.Red))

#-------------------------#

# Image Name

__Name = "{0}_{1}.{2}".format(
	re.compile("[^a-zA-Z]").sub("_", Config["Text"]["Content"][:192]),\
	Random_String(8),
	"png" if len(Frames) == 1 else "gif"
	)

# Saving Image

__Meta = PngImagePlugin.PngInfo()
__Meta.__dict__ = {
	"chunks":
		[
			(b"tEXt",
			bytes("Text\x00{0}".format(demojize(Config["Text"]["Content"])),
				encoding = "utf-8")
			),
			(b"tEXt",
			bytes("Image\x00{0}".format(Config["Image"]["URL / Path"]),
				encoding = "utf-8")
			)
		]
	}

__SAV_TIME = time()
if len(Frames) == 1:
	GIF = Image.open(Frames[0])
	GIF.save("Images/{0}".format(__Name),
	pnginfo = __Meta)

#-------------------------#

# GIF Optimizing

if Config["Settings"]["Delay"] == 1:
	Config["Settings"]["Delay"] = 2

if not len(Frames) == 1:
	try:
		os.system('{0} -i "Frame_%05d.png" -vf palettegen=reserve_transparent=1 "Palette.png" -y {1}'.format(
			__FFmpeg,
			"" if not Config["Settings"]["Packages"]["Logs"] else "-hide_banner -loglevel panic"
		))
		os.system('{0} -i "Frame_%05d.png" -i "Palette.png" -lavfi paletteuse=alpha_threshold=128 "Images/{1}" -y {2}'.format(
			__FFmpeg,
			__Name,
			"" if not Config["Settings"]["Packages"]["Logs"] else "-hide_banner -loglevel panic",
		))
		os.system('{0} --careful {1}-b "Images/{2}" -w'.format(
			__Gifsicle,
			"" if Config["Settings"]["Delay"] == 0 else "-d{0} ".format(Config["Settings"]["Delay"]),
			__Name,
			))
	except KeyboardInterrupt:
		print("{1}{0}{2}".format(KeyboardInterrupt.__name__, Styles.Red, Styles.Reset))
	#---#
	if Config["Settings"]["Optimize"]["Enabled"]:
		print("{0}Optimizing...{1}".format(Styles.Reset, Styles.Red))
		os.system('{0} --careful -b -O3 --lossy={1} "Images/{2}" -w'.format(
			__Gifsicle,
			Config["Settings"]["Optimize"]["Lossy"],
			__Name,
		))
			#"" if not Config["Settings"]["Packages"]["Logs"] else "--verbose"

__SAV_TIME = timedelta(seconds = time() - __SAV_TIME)

#-------------------------#

# Frames Removal

print("{1}Removing {0}...".format("Image" if len(Frames) == 1 else "Frames", Styles.Reset))
__REM_TIME = time()
[os.remove(Frame) for Frame in next(os.walk("."))[2] if Frame.endswith(__Format)]
__REM_TIME = timedelta(seconds = time() - __REM_TIME)
print("{0}Done!{1}{2}".format(Styles.Green, Styles.Reset, __BEL))

#-------------------------#

# `Time_Logs` Output

if Config["Settings"]["Time Logs"]:
	print("\nModules were loaded in:\t\t\t{1}{0}{2}.".format(str(__STA_TIME)[2:], Styles.Cyan, Styles.Reset))
	print("Input {0} was converted to frames in:\t{2}{1}{3}.".format("file" if not Config["Image"]["URL / Path"].startswith("http") else "URL", str(__CNV_TIME)[2:], Styles.Cyan, Styles.Reset))
	print("Frames were processed in:\t\t{1}{0}{2}.".format(str(__MKE_TIME)[2:], Styles.Cyan, Styles.Reset))
	print("{0} was made in:\t\t\t{2}{1}{3}.".format("PNG" if len(Frames) == 1 else "GIF", str(__SAV_TIME)[2:], Styles.Cyan, Styles.Reset))
	print("Frames were deleted in:\t\t\t{1}{0}{2}.".format(str(__REM_TIME)[2:], Styles.Cyan, Styles.Reset))
	print("All operations were done in:\t\t{1}{0}{2}.".format(str(__STA_TIME + __CNV_TIME + __MKE_TIME + __SAV_TIME + __REM_TIME)[2:], Styles.Cyan, Styles.Reset))