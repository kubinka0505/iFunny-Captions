if Config["Settings"]["Open_Folder"]:
	MessageBox = msgbox.askyesno(
		title = "Success",
		message = "Caption was successfully made in {0}. ({1})\nOpen containing folder?".format(
			__SUM_TIME[:-3], File_Size(os.path.getsize(__Name))
			),
		icon = "info",
		)

	if MessageBox:
		Command = 'start /max explorer /select,"{0}"'
		if not system() == "Windows":
			Command = 'nautilus "{0}"'

		call(Command.format(__Name), shell = True)
	else:
		pass
else:
	print(end = __BEL)