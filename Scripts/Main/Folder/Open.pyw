Message_Box = msgbox.askyesno(
	title = "Success",
	message = "Caption was successfully made in {0}. ({1})\nOpen containing folder?".format(
		__SUM_TIME[:-3], File_Size(os.path.getsize(__Name))
	),
	icon = "info",
)

#-=-=-=-#

if Message_Box:
	if os.sys.platform.startswith("win"):
		Command = r"start /max C:\Windows\explorer.exe"
	elif os.sys.platform.startswith("lin"):
		distro = id()
		if distro == "ubuntu":
			Command = "nautilus"
		elif distro == "debian":
			Command = "nemo"
		elif distro == "rhel":
			Command = "gnome-open"
		else:
			Command = "xdg-open"
	else:
		Command = "open"

	Command += ' "{0}"'.format(os.path.dirname(__Name))
	call(Command, shell = 1)