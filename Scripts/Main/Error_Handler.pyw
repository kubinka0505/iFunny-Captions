Clipboard_Warning = ""
if Config["Media"]["Image"]["URL_or_Path"] == "clipboard":
	Clipboard_Warning = "{0}Warning{2}: {1}clipboard{2} is enabled.".format(
		Styles.Warning, Styles.Meta_Info, Styles.Reset
	)
	Config["Media"]["Image"]["URL_or_Path"] = paste()

#-=-=-=-#

if not Config["Media"]["Image"]["URL_or_Path"]:
	Config["Media"]["Image"]["URL_or_Path"] = fd.askopenfilename(
		title = "Select visual media file",
		initialdir = "..",
		filetypes = [
			("Static Image Files", ".bmp .ico .jpeg .jpg .png .tiff .webp"),
			("Dynamic Image Files", " .".join(__Dynamic_Formats[0])),
			("Video Files", "." + " .".join(__Dynamic_Formats[1])),
			],
		defaultextension = ".gif"
		)
	if not Config["Media"]["Image"]["URL_or_Path"]:
		print("\n{0}Warning{3}: {1}No URL / File given!{3}\nInput {2}URL{3} or {2}absolute path{3} to image.\n\nPerform {2}CTRL{3} + {2}C{3}, then {2}Enter{3} when done.\nPress {2}CTRL{3} + {2}Z{3}, then {2}Enter{3} to exit.\n\nText will be stripped. Multilne supported. ({2}Enter{3})\n{4}".format(
			Styles.Warning, Styles.Flaw, Styles.Info, Styles.Reset, __BEL
			)
		)

		try:
			ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
			ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
		except AttributeError:
			pass

		Lines = []
		while 1:
			try:
				Line = input("{0}> {1}".format(Styles.OK, Styles.Reset))
				Lines.append(Line)
			except KeyboardInterrupt:
				break
			except EOFError:
				Lines = "exit"
				break
		if Lines:
			Lines = "".join(Lines).replace("\n", "")
			Config["Media"]["Image"]["URL_or_Path"] = Lines
			if Lines == "exit":
				raise SystemExit("Exiting.")
		else:
			raise SystemExit("No text inputted - exiting.")
		print("Finishing text input!\n")

#-=-=-=-#

try:
	try:
		with get(Get_Service(Config["Media"]["Image"]["URL_or_Path"])) as Site:
			if not Site.ok:
				raise SystemExit("\nURL returns status code {2}{0}{3} ({2}{1}{3}).\n{2}Image will not be processed.{3}{4}".format(
					Site.status_code, Site.reason.title(),
					Styles.Error, Styles.Reset, __BEL
					)
				)
	except ConnectionError:
		raise SystemExit("{0}No internet connection!{1}{2}".format(
			Styles.Error, Styles.Reset, __BEL
			)
		)
except MissingSchema:
	raise SystemExit('\n{1}Invalid URL{4}! {2}("{0}"){3}\nImage will not be processed.{4}\n{5}{6}'.format(
		Get_Service(Config["Media"]["Image"]["URL_or_Path"]) if Get_Service(Config["Media"]["Image"]["URL_or_Path"]) else "None"),
		Styles.Warning, Styles.Meta_Info, Styles.Error, Styles.Reset, Clipboard_Warning, __BEL
	)
except InvalidSchema:
	pass