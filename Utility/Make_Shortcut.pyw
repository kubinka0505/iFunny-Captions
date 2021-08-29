exec(open("__init__.py", encoding = "utf-8").read())
from pyshortcuts import make_shortcut

Icon_HQ = path.abspath(Icon.replace(
	"Icon", "Icon_HQ"
	)
)

Script = path.abspath('../__init__.pyw')
Initial_Directory = "~/Desktop"

#---#

Folder = fd.askdirectory(
	title = "Make shortcut to program",
	initialdir = path.abspath(path.expanduser(Initial_Directory))
	)
Folder = path.abspath(Folder)

if Folder == getcwd():
	Folder = path.abspath(path.expanduser(Initial_Directory))
	raise SystemExit("Folder selection aborted")

chdir(Folder)

#---#

Name = "iFunny-Captions"
try:
	print("Removing previous shortcut...")
	for Shortcut in next(walk("."))[2]:
		if Shortcut.startswith(Name):
			remove(path.abspath(Shortcut))
except IndexError:
	pass

#---#

print("Making shortcut...")
make_shortcut(
	Script, Name,
	"Make the caption with predefined settings",
	Icon_HQ, Folder, startmenu = False,
)

#---#

Message = 'Shortcut successfully created in "{0}" folder.'.format(
	Folder.split(sep)[-1]
	)

msgbox.showinfo(
	title = "Success",
	message = Message,
	)

raise SystemExit(Message)