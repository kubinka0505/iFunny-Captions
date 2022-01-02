exec(open("__init__.pyw", encoding = "U8").read())
if system_() == "Windows": system("title Display Caption Metadata")
from requests import get
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
		("All files", "*.*"),
		("Static Image Files", ".bmp .ico .jpeg .jpg .png .tiff .webp"),
		("Video Files", ".mp4")
	]
)

print(" " * (len(Title) + 3), end = "\r")
if not File: exit()

#---#

if File.endswith("png"):
	Info = OrderedDict(list(PngImageFile(File).text.items()))
else:
	Info = {Key: Value[0] for Key, Value in mFile(File).items()}
	try: Info = {"Text": Info["©cmt"], "Image": Info["desc"], "Audio": Info["©nam"]}
	except: Info = []

if len(Info):
	for Key, Value in Info.items():
		Output = ""
		#---#
		try:
			Site = get(Value)
			Output = "\t({0} - {1})".format(
				Site.status_code, Site.reason
			)
		except:
			pass
		
		#---#
		print('{0}:\t\t"{1}"{2}'.format(
				Key, Value,
				("\t" + Output) if Output else ""
			)
		)
else:
	print('No metadata was found in "{0}".'.format(File.split("/")[-1]))

print()
if system_() == "Windows": system("pause")