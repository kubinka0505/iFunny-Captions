Clipboard_Warning = ""
if Config["Image"]["URL_or_Path"] == "clipboard":
	Clipboard_Warning = "{0}Warning{2}: {1}clipboard{2} is enabled.".format(Styles.Yellow, Styles.DarkGray, Styles.Reset)
	Config["Image"]["URL_or_Path"] = paste()

if not Config["Image"]["URL_or_Path"]:
	try:
		Config["Image"]["URL_or_Path"] = fd.askopenfilename(
			title = "Select visual media file",
			initialdir = "..",
			filetypes = [
				("Static Image Files", ".bmp .ico .jpeg .jpg .png .tiff"),
				("Dynamic Image Files", ".gif"),
				("Video Files", ".mov .mp4 .webm")
				],
			defaultextension = ".gif"
			)
	except AttributeError:
		raise SystemExit("File selection aborted!" + __BEL)

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