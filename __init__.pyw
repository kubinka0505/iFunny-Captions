"""iFunny Captions Generator.

Pack of scripts providing iFunny Captions
generation, but this time You can input your
own text and picture using `Config.json` file."""

__STA_TIME = __import__("time").time()
import re, os, io, ctypes
from auepa import Utils
from requests import get
from textwrap import wrap
from platform import system
from clipboard import paste
from subprocess import call
from shutil import copyfile
from time import sleep, time
from string import printable
from json import load, decoder
from datetime import timedelta
from random import choice, randint
from urllib.parse import quote_plus
from emoji import emojize, demojize, UNICODE_EMOJI_ENGLISH
from requests.exceptions import InvalidSchema, MissingSchema
from tkinter import Tk, filedialog as fd, messagebox as msgbox
from PIL import Image, ImageColor, ImageDraw, ImageFile, ImageFont, PngImagePlugin, UnidentifiedImageError

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__, "SuperCuber"
__version__		= "3.1"
__date__		= "20.08.2021"
__status__		= "Mature"
__license__		= "GPL V3"

__BaseDir	= os.path.abspath(os.path.dirname(__file__))

root = Tk()
root.withdraw()
try: root.iconbitmap("../Documents/Pictures/GUI/Icon.ico")
except: pass

exec(open("Scripts/Main/Make_Folder.pyw", encoding = "utf-8").read())

os.chdir(__BaseDir)

# Opening Scripts/Utils.pyw
exec(open("Scripts/Main/Utils.pyw", encoding = "utf-8").read())
print("{0}Set up utils...".format(Styles.Reset))
__STA_TIME = timedelta(seconds = time() - __STA_TIME)

# Error Handling
__Dynamic_Formats = "gif", "3gp", "flv", "mov", "mp4", "webm"
exec(open("Scripts/Main/Error_Handler.pyw", encoding = "utf-8").read())

# Getting Packages Location
if not system() == "Windows":
	import apt
	cache = apt.Cache()

exec(open("Scripts/Main/Packages_Location/FFmpeg.pyw", encoding = "utf-8").read())
exec(open("Scripts/Main/Name_Folder.pyw", encoding = "utf-8").read())

# Image to Frames conversion & Cache System
__CNV_TIME = time()
exec(open("Scripts/Main/Convert_Image.pyw", encoding = "utf-8").read())

print("{0}Copying files to main directory...".format(Styles.Reset))
exec(open(__BaseDir + "/Scripts/Main/Copy_File.pyw", encoding = "utf-8").read())

os.chdir(__BaseDir)
__CNV_TIME = timedelta(seconds = time() - __CNV_TIME)

Frames = [File for File in next(os.walk("."))[2] if File.endswith("png")]
Frames.sort(key = str)

#-------------------------#

# GIF Making Process
exec(open("Scripts/Main/Make_GIF.pyw", encoding = "utf-8").read())

# Image Name
exec(open("Scripts/Main/Name_Image.pyw", encoding = "utf-8").read())
exec(open("Scripts/Main/Save_Image.pyw", encoding = "utf-8").read())

# Optimizing
if Config["Settings"]["Delay"] == 1:
	Config["Settings"]["Delay"] = 2

exec(open("Scripts/Main/Optimize/Dynamic.pyw", encoding = "utf-8").read())
exec(open("Scripts/Main/Optimize/Static.pyw", encoding = "utf-8").read())

__SAV_TIME = timedelta(seconds = time() - __SAV_TIME)

#-------------------------#

exec(open("Scripts/Main/Frames_Removal.pyw", encoding = "utf-8").read())
exec(open("Scripts/Main/Time_Logs.pyw", encoding = "utf-8").read())
exec(open("Scripts/Main/Open_Folder.pyw", encoding = "utf-8").read())