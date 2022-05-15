exec(open("__init__.pyw", encoding = "U8").read())

with redirect_stdout(None):
	from pyshortcuts import make_shortcut

Initial_Directory = os.path.abspath(os.path.expanduser("~/Desktop"))
Script = os.path.abspath("../iFunny_Captions.pyw")
Icon_HQ = os.path.abspath(Icon.replace("Icon.", "Icon_HQ."))

#---#

Folder = fd.askdirectory(
	title = "Select folder to create the shortcut in",
	initialdir = Initial_Directory
)
Folder = os.path.abspath(Folder)

if Folder == os.getcwd():
	Folder = Initial_Directory
	raise SystemExit("Folder selection aborted.")

os.chdir(Folder)

#---#

Name = "iFunny-Captions"
try:
	for Shortcut in next(os.walk("."))[2]:
		if Shortcut.startswith(Name):
			print("Removing previous shortcut...")
			os.remove(os.path.abspath(Shortcut))
			break
except IndexError:
	pass

#---#

print("Making shortcut...")
make_shortcut(
	Script, Name,
	"Make the iFunny Caption",
	Icon_HQ, Folder, startmenu = False,
)

#---#

Message = 'Shortcut successfully created in "' + os.path.basename(Folder) + '" folder.'

msgbox.showinfo(
	title = "Success",
	message = Message,
)

print(Message)