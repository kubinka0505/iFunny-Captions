if Config["Settings"]["Open_Folder"]:
	MessageBox = msgbox.showinfo(
		title = "Success",
		message = "Caption was successfully made in {0}.".format(__SUM_TIME[:-3])
		)

	os.chdir("Images")
	Command = 'start /max explorer /select,"{0}"'
	if MessageBox == "ok":
		if not system() == "Windows":
			Command = 'nautilus "{0}"'

		call(Command.format(__Name), shell = True)