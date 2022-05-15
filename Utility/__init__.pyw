import os
from pathlib import Path
from mutagen import File as mFile
from contextlib import redirect_stdout
from tkinter import Tk, filedialog as fd, messagebox as msgbox

try:
	os.chdir(os.path.dirname(os.path.abspath(__file__)))
except:
	pass
Icon = "../Documents/Pictures/Icons/GUI/Icon.ico"

#---#

root = Tk()
root.withdraw()
try:
	root.iconbitmap(Icon)
except:
	pass

#---#

def Folder_Size():
	"""Calculates folder size recursively"""
	Files = [str(File.resolve()) for File in Path(".").glob("**/*")]
	Size = sum([os.path.getsize(File) for File in Files])
	return Size

def File_Size(Bytes: float) -> str:
	"""Returns human-readable file size"""
	for Unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
		if Bytes < 1024:
			break
		Bytes /= 1024
	return "{0} {1}".format(round(Bytes, 2), Unit)