exec(open("__init__.pyw", encoding = "U8").read())
from shutil import rmtree

#---#

__TEMP = getenv("Temp") if system_() == "Windows" else "/tmp"
__Folder = __TEMP + "/iFunny"

#---#

try:
	chmod(__Folder, 511)

	Files = sum(len(Files) for _, _, Files in walk(__Folder))
	Files_Size = File_Size(Folder_Size())

	rmtree(__Folder)
	msgbox.showinfo(
		title = "Success",
		message = "Removed cache folder ({1}, {0} file{2})".format(
			Files,
			Files_Size,
			"s" if not Files or Files > 1 else ""
			),
		)
except Exception as Error:
	print(Error)
	msgbox.showwarning(
		title = Error.__class__.__name__,
		message = "No cache folder found!"
		)