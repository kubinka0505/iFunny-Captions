__TEMP		= os.getenv("Temp") if system() == "Windows" else "/tmp"
__Folders	= [__TEMP, "iFunny", "Cache", "Captions", "Frames"]

for Folder in __Folders:
	try: os.mkdir(Folder)
	except FileExistsError: pass
	os.chdir(Folder)

os.chdir(__BaseDir)