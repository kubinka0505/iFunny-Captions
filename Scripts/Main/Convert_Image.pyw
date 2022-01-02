os.chdir(os.sep.join(__Folders))
__Dynamic_Formats = __Dynamic_Formats[0] + __Dynamic_Formats[1]

if __Folder_Name in next(os.walk("."))[1]:
	os.chdir(__Folder_Name)
	print(Styles.OK + "URL was located in the cache folder!" + Styles.Reset)
else:
	try: os.mkdir(__Folder_Name)
	except FileExistsError: pass
	os.chdir(__Folder_Name)
	print(Styles.Warning + "URL was not located in cache folder!" + Styles.Reset)
	print("Converting {0} Image to Frames... {1}(This can take a while){2}".format(
		"URL" if Config["Media"]["Image"]["URL_or_Path"].startswith("http") else "Path",
		Styles.Info, Styles.Flaw
		)
	)
	try:
		os.system('{0} -i "{1}" {2} -loglevel {3} -y'.format(
			__FFmpeg,
			Get_Service(Config["Media"]["Image"]["URL_or_Path"]),
			"Frame.png" if not Get_Service(Config["Media"]["Image"]["URL_or_Path"]).endswith(__Dynamic_Formats) else "{0}Frame_%05d.png".format(
				"-vf select=not(mod(n\,2)) " if Config["Settings"]["Delay"] == 1 else ""
				),
			"40" if Config["Settings"]["Packages"]["Logs"] else "-8 -hide_banner"
			)
		)
	except KeyboardInterrupt:
		__Frames = len([File for File in next(os.walk("."))[2] if File.endswith("png")])
		print("\n{1}Warning{3}: User interrupted the frames conversion process. Converted {2}{0}{3} frames so far.{4}".format(
			str(__Frames), Styles.Warning, Styles.Warning if __Frames else Styles.Error, Styles.Reset, __BEL
			)
		)
		if not __Frames:
			rmtree(os.getcwd())
			raise SystemExit("No converted frames found, removing directory and exiting." + __BEL)
