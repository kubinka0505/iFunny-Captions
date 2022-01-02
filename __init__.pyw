"""iFunny-Captions

Pack of scripts providing widely
customizable iFunny Captions generation"""

__STA_TIME = __import__("time").time()
import ctypes, io, math, os, re
from sty import fg
from auepa import Utils
from colour import Color
from textwrap import wrap
from platform import system
from clipboard import paste
from subprocess import call
from mutagen.id3 import ID3
from time import sleep, time
from string import printable
from requests import Session
from json import load, decoder
from mutagen import File as mFile
from requests.exceptions import *
from random import choice, randint
from urllib.parse import quote_plus
from urllib.request import urlretrieve
from datetime import datetime, timedelta
from unidecode import unidecode as normalize
from argparse import ArgumentParser as ap, SUPPRESS
from emoji import emojize, demojize, UNICODE_EMOJI_ENGLISH
from tkinter import Tk, filedialog as fd, messagebox as msgbox
from shutil import copyfile, move as mv, rmtree, unpack_archive
from PIL import Image, ImageChops, ImageColor as IC, ImageDraw, ImageFile, ImageFont, ImageOps, PngImagePlugin, UnidentifiedImageError

#-------------------------#

__author__	= "kubinka0505"
__copyright__ = __author__
__credits__	= __author__, "SuperCuber"
__version__	= "3.6"
__date__	= "02.01.2022"
__status__	= "Mature"
__license__	= "GPL V3"

__BaseDir = os.path.abspath(os.path.dirname(__file__))
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

open_ = lambda _open: open(__BaseDir + "/Scripts/Main/" + _open + ".pyw", encoding = "U8").read()

exec(open_("../Utils"))
exec(open_("Utils"))
exec(open_("Make_Folder"))

if system() == "Windows": os.system("title iFunny-Captions")
exec(open_("Update/Check"))

print("{2}> iFunny-Captions {0} {3}({1}){4}\n".format(
	__version__, __date__,
	Styles.Warning, Styles.Meta_Info, Styles.Reset
	)
)

exec(open_("../ArgParse"))
print("{0}Set up utils...".format(Styles.Reset))

Remove_Pictures(__BaseDir)
__STA_TIME = timedelta(seconds = time() - __STA_TIME)

# Error Handling
exec(open_("Error_Handler"))

# Getting Packages Location
if not system() == "Windows":
	import apt
	cache = apt.Cache()

exec(open_("Packages_Location/FFmpeg"))
exec(open_("Name_Folder"))

# Image to Frames conversion & Cache System
__CNV_TIME = time()
exec(open_("Convert_Image"))
exec(open_("Copy_File"))

os.chdir(__BaseDir)
__CNV_TIME = timedelta(seconds = time() - __CNV_TIME)

Frames = sorted(
	[File for File in next(os.walk("."))[2] if File.endswith("png")],
	key = str
)

#-------------------------#

try:
	# GIF Making Process
	exec(open_("Make_GIF"))

	# Image Name
	exec(open_("Name_Image"))
	exec(open_("Save_Image"))
except KeyboardInterrupt:
	print(Styles.Flaw + "\nFrames copying process was interrupted by the user, exiting." + Styles.Reset + __BEL)
	try: Remove_Pictures(__BaseDir)
	except PermissionError: print(Styles.Flaw + "Frames will be deleted at the next program launch." + Styles.Reset)
	raise SystemExit()

# Optimizing
try:
	if Config["Media"]["Video"]["Audio"]["URL_or_Path"]:
		Config["Settings"]["Optimize"]["Enabled"] = \
		Config["Media"]["Image"]["Scale_Back"] = 0
	#---#
	if len(Frames) > 1: exec(open_("Optimize/Dynamic"))
	elif len(Frames) == 1: exec(open_("Optimize/Static"))
	exec(open_("Optimize/Grayscale"))
except KeyboardInterrupt:
	raise SystemExit("\n{0}Image optimization process was interrupted by the user, exiting.{1}".format(Styles.Flaw, Styles.Reset) + __BEL)

__SAV_TIME = timedelta(seconds = time() - __SAV_TIME)

#-------------------------#

__VID_TIME = 0
if Config["Media"]["Video"]["Audio"]["URL_or_Path"]: exec(open_("../Video"))

__Name = __Name_Out if Config["Media"]["Video"]["Audio"]["URL_or_Path"] else __Name
if Config["Settings"]["Add_Metadata"]: exec(open_("../Metadata"))

exec(open_("Frames_Removal"))

print(Styles.OK + "Done!")
print("\n{2}Output file:{3}\n\t{4}Name{5}\t\t{0}{4}\n\tAbsolute path{5}\t{1}{3}".format(
		__Name.split(os.sep)[-1],
		__Name.replace(
			os.path.expanduser("~"),
			"%UserProfile%" if system() == "Windows" else "~"
		),
		Styles.OK, Styles.Reset,
		Styles.Info, Styles.Meta_Info
	)
)

if Config["Settings"]["Time_Logs"]:	exec(open_("Time_Logs"))
if Config["Settings"]["Open_Folder"]: exec(open_("Open_Folder"))