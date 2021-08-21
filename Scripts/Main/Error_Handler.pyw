Clipboard_Warning = ""
if Config["Image"]["URL_or_Path"] == "clipboard":
	Clipboard_Warning = "{0}Warning{2}: {1}clipboard{2} is enabled.".format(Styles.Yellow, Styles.DarkGray, Styles.Reset)
	Config["Image"]["URL_or_Path"] = paste()

if not Config["Image"]["URL_or_Path"]:
	Config["Image"]["URL_or_Path"] = fd.askopenfilename(
		title = "Select visual media file",
		initialdir = "..",
		filetypes = [
			("Static Image Files", ".bmp .ico .jpeg .jpg .png .tiff .webp"),
			("Dynamic Image Files", ".apng .gif"),
			("Video Files", "." + " .".join(__Dynamic_Formats[1:])),
			],
		defaultextension = ".gif"
		)
	if not Config["Image"]["URL_or_Path"]:
		print("\n{0}Warning{3}: {1}No URL / File given!{3}\nInput {2}URL{3} or {2}absolute path{3} to image.\n\nPerform {2}CTRL{3} + {2}C{3}, then {2}Enter{3} when done.\nPress {2}CTRL{3} + {2}Z{3}, then {2}Enter{3} to exit.\n\nText will be stripped. Multilne supported. ({2}Enter{3})\n{4}".format(
			Styles.Yellow, Styles.LightRed, Styles.LightBlue, Styles.Reset, __BEL
			)
		)

		try:
			ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), False)
			ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
		except AttributeError:
			pass

		Lines = []
		while 1:
			try:
				Line = input("{0}> {1}".format(Styles.Green, Styles.Reset))
				Lines.append(Line)
			except KeyboardInterrupt:
				break
			except EOFError:
				Lines = "exit"
				break
		if Lines:
			Lines = "".join(Lines).replace("\n", "")
			Config["Image"]["URL_or_Path"] = Lines
			if Lines == "exit":
				raise SystemExit("Exiting.")
		else:
			raise SystemExit("No text inputted - exiting.")
		print("Finishing text input!\n")

#---#

try:
	with get(Get_Service(Config["Image"]["URL_or_Path"])) as Site:
		if not Site.ok:
			raise SystemExit("\nURL returns status code {2}{0}{3} ({2}{1}{3}).\n{2}Image will not be processed.{3}{4}".format(Site.status_code, Site.reason.title(), Styles.Red, Styles.Reset, __BEL))
except MissingSchema:
	raise SystemExit('\n{1}Invalid URL{4}! {2}("{0}"){3}\nImage will not be processed.{4}\n{5}{6}'.format(
		"None" if not Get_Service(Config["Image"]["URL_or_Path"]) else Get_Service(Config["Image"]["URL_or_Path"]),
		Styles.Yellow, Styles.DarkGray, Styles.Red, Styles.Reset, Clipboard_Warning, __BEL
		)
	)
except InvalidSchema:
	pass