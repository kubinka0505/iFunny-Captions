__TEMP		= Get_Path("~/AppData/Local/Temp") if os.sys.platform.startswith("win") else "/tmp"
__Folders	= [__TEMP, "iFunny", "Cache", "Captions", "Frames"]

for Folder in __Folders:
	try: os.mkdir(Folder)
	except FileExistsError: pass
	os.chdir(Folder)

os.chdir(__BaseDir)