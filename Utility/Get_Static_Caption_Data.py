exec(open("__init__.pyw", encoding = "utf-8").read())
if system_() == "Windows": system("title Static Caption Data Finder")
from random import randint
from PIL.PngImagePlugin import *
from collections import OrderedDict

#---#

Directory = "../Images/"
Title = "Select static caption image file"
print(Title + "...", end = "\r")

File = fd.askopenfilename(
	title = Title,
	initialdir = Directory,
	filetypes = [("Static Image Files", ".bmp .ico .jpeg .jpg .png .tiff .webp")],
)

print(" " * (len(Title) + 3), end = "\r")
if not File:
	print("No file selected, checking latest...")
	File = path.abspath(max([Directory + File for File in next(walk(Directory))[2]], key = path.getctime))

#---#

if File.endswith("png"):
	Info = OrderedDict(reversed(list(PngImageFile(File).text.items())))
	for Key, Value in Info.items(): print('{0}:\t\t"{1}"'.format(Key, Value))
else: print('No metadata was found in "{0}".'.format(File.split(sep)[-1]))

print()
if system_() == "Windows": system("pause")