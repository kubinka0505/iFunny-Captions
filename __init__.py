import os
from json import load
from requests import get
from random import choice
from textwrap import wrap
from platform import system
from string import printable
from time import time, sleep
from datetime import timedelta
from PIL import Image, ImageDraw, ImageFont, ImageColor

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= [__author__, "SuperCuber"]
__version__		= "2.4"
__date__		= "17.11.2020"
__status__		= "Development"
__license__		= "GPL V3"

os.chdir(os.getcwd())
__FORMAT = "png"
__SLASH = "\\" if system() == "Windows" else "/"

# Opening Scripts/Utils.py

print("Setting up utils...")
exec(open("{0}{1}Scripts{1}Utils.py".format(os.getcwd(), __SLASH)).read())

# Getting FFmpeg Location

if Config()["Settings"]["FFmpeg_Location"] == "":
	for File in os.listdir(os.getcwd()):
		if os.path.basename(File)[0:6] == "ffmpeg":
			__FFMPEG = os.getcwd() + __SLASH + File
else:
	__FFMPEG = Config()["Settings"]["FFmpeg_Location"]

# Image to frames conversion

print("Converting {0} Image to Frames... This can take a while.".format("URL" if Config()["Image"]["URL / Path"].startswith("http") else "Path"))
__CNV_TIME = time()
os.system('{0} -i {1} Frame_%06d.{2} -hide_banner -loglevel panic'.format(__FFMPEG, __Get_Service(Config()["Image"]["URL / Path"]), __FORMAT))
__CNV_TIME = timedelta(seconds = time() - __CNV_TIME)

Frames = [File for File in os.listdir(os.getcwd()) if File.endswith(__FORMAT)]
Frames.sort(key = str)

# GIF making process

print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))
__MKE_TIME = time()
for Frame in Frames:
	Caption = Image.open(Frame)
	#---#
	exec(open("{0}{1}Scripts{1}Caption.py".format(os.getcwd(), __SLASH)).read())	
	exec(open("{0}{1}Scripts{1}Gifer.py".format(os.getcwd(), __SLASH)).read())
	#---#
	Captionized.save(Frame)
__MKE_TIME = timedelta(seconds = time() - __MKE_TIME)

print("Saving {0}...".format("PNG" if len(Frames) == 1 else "GIF"))

# Image Name

__NAME = "{0}_{1}.{2}".format(Config()["Text"].\
	replace(" ", "_").\
	replace("\\", "_").\
	replace("/", "_").\
	replace(":", "_").\
	replace("*", "_").\
	replace("?", "_").\
	replace('"', "_").\
	replace("<", "_").\
	replace(">", "_").\
	replace("|", "_").\
	encode().decode("utf-8", errors = "strict")[0:192],
	Random_String(8),
	"png" if len(Frames) == 1 else "gif"
	)

# Saving Image

__SAV_TIME = time()
if len(Frames) == 1:
	GIF = Image.open(Frames[0])
	GIF.save("{0}{1}Images{1}{2}".format(
			os.getcwd(),
			__SLASH,
			__NAME
			),
		loop = 0,
		save_all = True,
		append_images = [Image.open(Frame) for Frame in Frames[1:]],
		duration = Config()["Settings"]["Delay"],
		)

if not len(Frames) == 1:
	os.system("{0} -i Frame_%06d.png -vf palettegen=reserve_transparent=1 Palette.png -hide_banner -loglevel panic".format(__FFMPEG))
	os.system("{0} -i Frame_%06d.png -i Palette.png -lavfi paletteuse=alpha_threshold=128 -gifflags -offsetting Images{1}{2} -hide_banner -loglevel panic".format(__FFMPEG, __SLASH, __NAME))
	#---#
	if Config()["Settings"]["Optimize_Factor"] > 0:
		sleep(1)
		print("Optimizing with gifsicle...")
		os.system("gifsicle --careful -d={0} -b -O{1} Images/{2} -w".format(Config()["Settings"]["Delay"], Config()["Settings"]["Optimize_Factor"], __NAME))

__SAV_TIME = timedelta(seconds = time() - __SAV_TIME)

# Frames Removal

print("Removing {0}...".format("Image" if len(Frames) == 1 else "Frames"))
__REM_TIME = time()
[os.remove("{0}{1}{2}".format(os.getcwd(), __SLASH, Frame)) for Frame in os.listdir(os.getcwd()) if Frame.endswith(__FORMAT)]
__REM_TIME = timedelta(seconds = time() - __REM_TIME)
print("Done!")

# `Logs` printing

if Config()["Settings"]["Logs"] == True:
	print("\nInput file was converted to frames in:\t{0}.".format(str(__CNV_TIME)[2:]))
	print("Frames were processed in:\t\t{0}.".format(str(__MKE_TIME)[2:]))
	print("{0} was made in:\t\t\t{1}.".format("PNG" if len(Frames) == 1 else "GIF", str(__SAV_TIME)[2:]))
	print("Frames were deleted in:\t\t\t{0}.".format(str(__REM_TIME)[2:]))
	print("All operations were done in\t\t{0}.".format(str(__CNV_TIME + __MKE_TIME + __SAV_TIME + __REM_TIME)[2:]))