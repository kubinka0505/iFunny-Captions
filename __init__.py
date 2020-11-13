import PIL
import os
from json import load
from requests import get
from random import choice
from textwrap import wrap
from platform import system
from string import printable
from PIL import Image, ImageDraw, ImageFont, ImageColor

__author__		= "kubinka0505"
__copyright__		= __author__
__credits__		= [__author__, "SuperCuber"]
__version__		= "2.0"
__date__		= "13.11.2020"
__status__		= "Development"
__license__		= "GPL v1"

__FORMAT = "png"
print("Setting up utils...")
exec(open("{0}{1}Scripts{1}Utils.py".format(os.getcwd(), "\\" if system != "Windows" else "/")).read())

print("Converting URL Image to Frames... This can take a while.")
os.system("ffmpeg.exe -i {0} Frame_%06d.{1} -hide_banner -loglevel panic".format(__Get_Service(Config()["Image"]["URL"]), __FORMAT))
# -vf mpdecimate,setpts=N/FRAME_RATE/TB duration fix

Frames = [File for File in os.listdir(os.getcwd()) if File.endswith(__FORMAT)]
Frames.sort(key = str)

print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))
for Frame in Frames:
	Caption = Image.open(Frame)
	#---#
	exec(open("{0}{1}Scripts{1}Caption.py".format(os.getcwd(), "\\" if system != "Windows" else "/")).read())	
	exec(open("{0}{1}Scripts{1}Gifer.py".format(os.getcwd(), "\\" if system != "Windows" else "/")).read())
	#---#
	Captionized.save(Frame)

GIF = Image.open(Frames[0])
print("Saving {0}...".format("PNG" if len(Frames) == 1 else "GIF"))
GIF.save("{0}{1}Captions{1}{2}_{3}.{4}".format(
		os.getcwd(),
		"\\" if system != "Windows" else "/",
		Config()["Text"].\
		replace(" ", "_").\
		replace("\\", "_").\
		replace("/", "_").\
		replace(":", "_").\
		replace("*", "_").\
		replace("?", "_").\
		replace("<", "_").\
		replace(">", "_").\
		replace("|", "_").\
		encode().decode("utf-8", errors = "strict"),
		Random_String(8),
		"png" if len(Frames) == 1 else "gif"
		),
	save_all = True,
	append_images = [Image.open(Frame) for Frame in Frames[1:]],
	duration = Config()["Settings"]["Speed"],
	loop = Config()["Settings"]["Loop"],
	)

print("Removing {0}...".format("Image" if len(Frames) == 1 else "Frames"))
[os.remove("{0}{1}{2}".format(os.getcwd(), "\\" , Frame)) for Frame in os.listdir(os.getcwd()) if Frame.endswith(__FORMAT)]
print("Done!")
