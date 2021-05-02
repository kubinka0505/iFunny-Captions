import os
from time import sleep
from shutil import rmtree
from platform import system

os.chdir(os.path.dirname(os.path.abspath(__file__)))

__TEMP		= os.getenv("Temp") if system() == "Windows" else "/tmp"
__Folder	= [__TEMP, "iFunny_Cache", "Captions", "Frames"]
Remove_All	= True

os.chdir(__TEMP)
if not Remove_All:
	os.chdir(os.sep.join(__Folder))
	for Folder in next(os.walk("."))[1]:
		print(Folder)
		#rmtree(Folder)
		print("Removed {0}".format(Folder))
		time.sleep(len(Folder) / 250)
else:
	print(__Folder[1])
	#rmtree(__Folder[1])
	print("Removed {0} folders".format(next(os.walk("."))[1]))