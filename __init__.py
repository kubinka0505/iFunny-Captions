import os
from json import load
from time import time
from requests import get
from random import choice
from textwrap import wrap
from platform import system
from string import printable
from datetime import timedelta
from PIL import Image, ImageDraw, ImageFont, ImageColor

__author__		= "kubinka0505"
__copyright__		= __author__
__credits__		= [__author__, "SuperCuber"]
__version__		= "2.3"
__date__		= "16.11.2020"
__status__		= "Development"
__license__		= "GPL V3"

__FORMAT = "png"
print("Setting up utils...")
exec(open("{0}{1}Scripts{1}Utils.py".format(os.getcwd(), "\\" if system == "Windows" else "/")).read())

print("Converting {0} Image to Frames... This can take a while.".format("URL" if Config()["Image"]["URL"].startswith("http") else "Path"))
__CNV_TIME = time()
os.system('ffmpeg -i {0} Frame_%06d.{1} -hide_banner -loglevel panic'.format(__Get_Service(Config()["Image"]["URL"]), __FORMAT))
__CNV_TIME = timedelta(seconds = time() - __CNV_TIME)

Frames = [File for File in os.listdir(os.getcwd()) if File.endswith(__FORMAT)]
Frames.sort(key = str)

print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))
__MKE_TIME = time()
for Frame in Frames:
	Caption = Image.open(Frame)
	#---#
	exec(open("{0}{1}Scripts{1}Caption.py".format(os.getcwd(), "\\" if system == "Windows" else "/")).read())	
	exec(open("{0}{1}Scripts{1}Gifer.py".format(os.getcwd(), "\\" if system == "Windows" else "/")).read())
	#---#
	Captionized.save(Frame)
__MKE_TIME = timedelta(seconds = time() - __MKE_TIME)

if Config()["Settings"]["Saving_Method"] == 1:
	print("Saving {0}... (PIL)".format("PNG" if len(Frames) == 1 else "GIF"))
if Config()["Settings"]["Saving_Method"] == 2:
	print("Saving {0}... (ffmpeg)".format("PNG" if len(Frames) == 1 else "GIF"))

__NAME = "{0}_{1}.{2}".format(Config()["Text"].\
			replace(" ", "_").\
			replace("\\", "_").\
			replace("/", "_").\
			replace(":", "_").\
			replace("*", "_").\
			replace("?", "_").\
			replace("<", "_").\
			replace(">", "_").\
			replace("|", "_").\
			encode().decode("utf-8", errors = "strict")[0:192],
			Random_String(8),
			"png" if len(Frames) == 1 else "gif"
			)

__SAV_TIME = time()
if Config()["Settings"]["Saving_Method"] == 1:
	GIF = Image.open(Frames[0])
	GIF.save("{0}{1}Captions{1}{2}".format(
			os.getcwd(),
			"\\" if system == "Windows" else "/",
			__NAME
			),
		loop = 0,
		save_all = True,
		append_images = [Image.open(Frame) for Frame in Frames[1:]],
		duration = Config()["Settings"]["Delay"],
		)

if Config()["Settings"]["Saving_Method"] == 2:
	os.system("ffmpeg -i Frame_%06d.png -vf palettegen Palette.png -hide_banner -loglevel panic")
	os.system("ffmpeg -i Frame_%06d.png -i palette.png -lavfi paletteuse Output.mp4 -hide_banner -loglevel panic")
	os.system("ffmpeg -i Output.mp4 Captions{0}{1} -hide_banner -loglevel panic".format("\\" if system == "Windows" else "/", __NAME))
	os.remove("{0}{1}Output.mp4".format(os.getcwd(), "\\" if system == "Windows" else "/"))
	os.remove("{0}{1}Palette.png".format(os.getcwd(), "\\" if system == "Windows" else "/"))

if len(Frames) > 1:
	if Config()["Settings"]["Optimize"] == True:
		print("Optimizing with GifSicle...")
		os.system("gifsicle --careful -d={0} -b -O8 Captions{1}{2} -w".format(Config()["Settings"]["Delay"], "\\" if system == "Windows" else "/", __NAME))

__SAV_TIME = timedelta(seconds = time() - __SAV_TIME)

print("Removing {0}...".format("Image" if len(Frames) == 1 else "Frames"))
__REM_TIME = time()
[os.remove("{0}{1}{2}".format(os.getcwd(), "\\" if system == "Windows" else "/", Frame)) for Frame in os.listdir(os.getcwd()) if Frame.endswith(__FORMAT)]
__REM_TIME = timedelta(seconds = time() - __REM_TIME)
print("Done!")

if Config()["Settings"]["Logs"] == True:
	print("\nInput file was converted to frames in:\t{0}.".format(str(__CNV_TIME)[2:]))
	print("Frames were processed in:\t\t{0}.".format(str(__MKE_TIME)[2:]))
	print("{0} was made in:\t\t\t{1}.".format("PNG" if len(Frames) == 1 else "GIF", str(__SAV_TIME)[2:]))
	print("Frames were deleted in:\t\t\t{0}.".format(str(__REM_TIME)[2:]))
	print("\nAll operations were done in\t\t{0}.".format(str(__CNV_TIME + __MKE_TIME + __SAV_TIME + __REM_TIME)[2:]))