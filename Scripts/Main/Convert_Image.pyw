os.chdir(os.sep.join(__Folders))

if __Folder_Name in next(os.walk("."))[1]:
	os.chdir(__Folder_Name)
	print("{0}URL was located in cache folder!{1}".format(Styles.Green, Styles.Reset))
else:
	os.mkdir(__Folder_Name)
	os.chdir(__Folder_Name)
	print("{0}URL was not located in cache folder!{1}".format(Styles.Yellow, Styles.Reset))
	print("Converting {0} Image to Frames... {1}(This can take a while){2}".format("URL" if Config["Image"]["URL_or_Path"].startswith("http") else "Path", Styles.LightBlue, Styles.LightRed))
	try:
		os.system('{0} -i "{1}" {2} {3}'.format(
				__FFmpeg,
				Get_Service(Config["Image"]["URL_or_Path"]),
				"Frame.png" if not Get_Service(Config["Image"]["URL_or_Path"]).endswith("gif") else "{0}Frame_%05d.png".format("-vf select='not(mod(n\,2))' " if Config["Settings"]["Delay"] == 1 else ""),
				"" if Config["Settings"]["Packages"]["Logs"] else "-hide_banner -loglevel panic"
				))
	except KeyboardInterrupt:
		print("{1}WARNING{2}: User interrupted the frames conversion process. Converted {1}{0}{2} frames so far.{3}".format(str(len([File for File in next(os.walk("."))[2] if File.endswith(__Format)])), Styles.Yellow, Styles.Reset, __BEL))
		pass