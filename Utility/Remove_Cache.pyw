exec(open("__init__.pyw", encoding = "U8").read())
from shutil import rmtree

#---#

__TEMP = os.getenv("TEMP") if os.sys.platform.startswith("win") else "/tmp"
__Folder = os.path.join(__TEMP, "iFunny")

#---#

try:
	Files = sum(len(Files) for _, _, Files in os.walk(__Folder))
	Files_Size = File_Size(Folder_Size())

	#-=-=-=-#

	rmtree(__Folder)

	message = "Removed cache folder ({1}, {0} file{2})".format(
		Files,
		Files_Size,
		"s" if not Files or Files > 1 else ""
	)

	msgbox.showinfo(
		title = "Success",
		message = Message,
		)
except OSError:
	Message = "No cache folder found!"

	msgbox.showwarning(
		title = "Failure",
		message = Message
		)