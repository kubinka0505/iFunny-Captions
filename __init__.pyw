"""iFunny-Captions

Pack of scripts providing widely
customizable iFunny Captions generation"""

__STA_TIME = __import__("time").time()
import io, os, re, ctypes
from sty import fg
from auepa import Utils
from requests import get
from textwrap import wrap
from platform import system
from clipboard import paste
from subprocess import call
from time import sleep, time
from string import printable
from json import load, decoder
from mutagen import File as mFile
from requests.exceptions import *
from random import choice, randint
from shutil import copyfile, rmtree
from urllib.parse import quote_plus
from datetime import datetime, timedelta
from argparse import ArgumentParser as ap
SUPPRESS = __import__("argparse").SUPPRESS
from unidecode import unidecode as normalize
from emoji import emojize, demojize, UNICODE_EMOJI_ENGLISH
from tkinter import Tk, filedialog as fd, messagebox as msgbox
from PIL import Image, ImageChops, ImageColor as IC, ImageDraw, ImageFile, ImageFont, PngImagePlugin, UnidentifiedImageError, ImageOps

#-------------------------#

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__, "SuperCuber"
__version__		= "3.4"
__date__		= "05.10.2021"
__status__		= "Mature"
__license__		= "GPL V3"

__BaseDir	= os.path.abspath(os.path.dirname(__file__))
os.chdir(__BaseDir)

#-------------------------#

try:
	root = Tk()
	root.withdraw()
	try: root.iconbitmap("./Documents/Pictures/Icons/GUI/Icon.ico")
	except: pass
except:
	print('No Tkinter environment found. ("DISPLAY" environment variable)')
	print('Do not try to fix this if you use CLI with "-p" option enabled - this is not a serious error\n')

#-------------------------#

exec(open("./Scripts/Main/Make_Folder.pyw", encoding = "utf-8").read())

# Opening Scripts/Utils.pyw
exec(open("./Scripts/Utils.pyw", encoding = "utf-8").read())
exec(open("./Scripts/Main/Utils.pyw", encoding = "utf-8").read())
exec(open("./Scripts/ArgParse.pyw", encoding = "utf-8").read())
print("{2}> iFunny-Captions {0} {3}({1}){4}\n".format(
	__version__, __date__, Styles.Warning, Styles.Meta_Info, Styles.Reset
	)
)
if system() == "Windows": os.system("title iFunny-Captions")
print("{0}Set up utils...".format(Styles.Reset))

Remove_Pictures(__BaseDir)
__STA_TIME = timedelta(seconds = time() - __STA_TIME)

# Error Handling
exec(open("./Scripts/Main/Error_Handler.pyw", encoding = "utf-8").read())

# Getting Packages Location
if not system() == "Windows":
	import apt
	cache = apt.Cache()

exec(open("./Scripts/Main/Packages_Location/FFmpeg.pyw", encoding = "utf-8").read())
exec(open("./Scripts/Main/Name_Folder.pyw", encoding = "utf-8").read())

# Image to Frames conversion & Cache System
__CNV_TIME = time()
exec(open("./Scripts/Main/Convert_Image.pyw", encoding = "utf-8").read())
exec(open(__BaseDir + "/Scripts/Main/Copy_File.pyw", encoding = "utf-8").read())

os.chdir(__BaseDir)
__CNV_TIME = timedelta(seconds = time() - __CNV_TIME)

Frames = sorted(
	[File for File in next(os.walk("."))[2] if File.endswith("png")],
	key = str
)

#-------------------------#

try:
	# GIF Making Process
	exec(open("./Scripts/Main/Make_GIF.pyw", encoding = "utf-8").read())

	# Image Name
	exec(open("./Scripts/Main/Name_Image.pyw", encoding = "utf-8").read())
	exec(open("./Scripts/Main/Save_Image.pyw", encoding = "utf-8").read())
except KeyboardInterrupt:
	print(Styles.Flaw + "\nFrames copying process was interrupted by the user, exiting." + Styles.Reset + __BEL)
	try:
		Remove_Pictures(__BaseDir)
	except PermissionError:
		print(Styles.Flaw + "Frames will be deleted at the next program launch." + Styles.Reset)
	raise SystemExit()

# Optimizing
#if Config["Settings"]["Delay"] == 1:
#	Config["Settings"]["Delay"] = 2 # TODO

try:
	exec(open("./Scripts/Main/Optimize/Dynamic.pyw", encoding = "utf-8").read())
	exec(open("./Scripts/Main/Optimize/Static.pyw", encoding = "utf-8").read())
	exec(open("./Scripts/Main/Optimize/Grayscale.pyw", encoding = "utf-8").read())
except KeyboardInterrupt:
	raise SystemExit("\n{0}Image optimization process was interrupted by the user, exiting.{1}".format(Styles.Flaw, Styles.Reset) + __BEL)

__SAV_TIME = timedelta(seconds = time() - __SAV_TIME)

#-------------------------#

exec(open("./Scripts/Video.pyw", encoding = "utf-8").read())
exec(open("./Scripts/Main/Frames_Removal.pyw", encoding = "utf-8").read())
exec(open("./Scripts/Main/Time_Logs.pyw", encoding = "utf-8").read())
exec(open("./Scripts/Main/Open_Folder.pyw", encoding = "utf-8").read())