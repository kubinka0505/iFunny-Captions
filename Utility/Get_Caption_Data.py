exec(open("__init__.pyw", encoding = "U8").read())
if system_() == "Windows": system("title Display Caption Metadata")
from PIL.PngImagePlugin import *
from mutagen import File as mFile
from collections import OrderedDict

#---#

Directory = "../Images/"
Title = "Select caption file"
print(Title + "...", end = "\r")

File = fd.askopenfilename(
	title = Title,
	initialdir = Directory,
	filetypes = [
		("Static Image Files", ".bmp .ico .jpeg .jpg .png .tiff .webp"),
		("Video Files", ".mp4")
	],
)

print(" " * (len(Title) + 3), end = "\r")
if not File: exit()

#---#

if File.endswith("png"):
	Info = OrderedDict(list(PngImageFile(File).text.items()))
else:
	File = {Key: Value[0] for Key, Value in mFile(File).items()}
	Info = {"Text": File["©cmt"], "Image": File["desc"], "Audio": File["©nam"]}

if len(Info):
	for Key, Value in Info.items(): print('{0}:\t\t"{1}"'.format(Key, Value[2:-1]))
else:
	print('No metadata was found in "{0}".'.format(File.split("/")[-1]))

print()
if system_() == "Windows": system("pause")