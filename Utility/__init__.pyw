from os import *
del open
from platform import system as system_
from tkinter import Tk, filedialog as fd, messagebox as msgbox

try: chdir(path.dirname(path.abspath(__file__)))
except: pass
Icon = "../Documents/Pictures/Icons/GUI/Icon.ico"

#---#

root = Tk()
root.withdraw()
try: root.iconbitmap(Icon)
except: pass

#---#

def Folder_Size():
	"""Calculates folder size recursively"""
	Size = 0
	for Root, Dirs, Files in walk("."):
		for File in Files:
			Path = path.join(Root, File)
			if not path.islink(Path):
				Size += path.getsize(Path)
	return Size

def File_Size(Bytes: float) -> str:
	"""Returns human-readable file size"""
	for Unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
		if Bytes < 1024.: break
		Bytes /= 1024.
	return "{0} {1}".format(round(Bytes, 2), Unit)