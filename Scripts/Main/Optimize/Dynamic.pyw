if not len(Frames) == 1:
	exec(open("./Scripts/Main/Packages_Location/Gifsicle.pyw", encoding = "utf-8").read())

	SBS = "\r"
	if system() == "Windows":
		from win32file import GetBinaryType as bt
		if Config["Image"]["Scale_Back"]:
			if not bt(__Gifsicle) == 6:
				print("{0}Warning{2}: {1}Scale_Back option will be ommited - Gifsicle is not 64-bit.{2}".format(
					Styles.Warning, Styles.Error, Styles.Reset)
				)
			else:
				SBS = Styles.Meta_Info_2 + "Scaling back..." + Styles.Reset

	print(SBS)

	try:
		os.system('{0} -i "Frame_%05d.png" -vf palettegen=reserve_transparent=1 "Palette.png" -y {1}'.format(
			__FFmpeg,
			"" if Config["Settings"]["Packages"]["Logs"] else "-hide_banner -loglevel panic"
			)
		)

		os.system('{0} -i "Frame_%05d.png" -i "Palette.png" -lavfi paletteuse=alpha_threshold=128 "Images/{1}" -y {2}'.format(
			__FFmpeg,
			__Name,
			"" if Config["Settings"]["Packages"]["Logs"] else "-hide_banner -loglevel panic"
			)
		)

		os.system('{0} --careful --no-comments {1}{2}-b "Images/{3}" {4}'.format(
			__Gifsicle,
			"" if not Config["Settings"]["Delay"] else "-d{0} ".format(Config["Settings"]["Delay"]),
			"" if not Config["Image"]["Scale_Back"] else "--resize {0}x{1} ".format(*Scale_Back),
			__Name,
			"-w" if not Config["Settings"]["Packages"]["Logs"] else "-i -cinfo -xinfo -sinfo -V"
			)
		)
	except KeyboardInterrupt:
		print("{1}{0}{2}".format(KeyboardInterrupt.__name__, Styles.Error, Styles.Reset))

	#---#

	if Config["Settings"]["Optimize"]["Enabled"]:
		print("{4}Optimizing... {2}(Gifsicle, lossy: {0}, {1} colors){3}".format(
				Config["Settings"]["Optimize"]["Gifsicle"]["Lossy"],
				Config["Settings"]["Optimize"]["Gifsicle"]["Colors"],
				Styles.Meta_Info,
				Styles.Flaw,
				Styles.Reset
				)
			)
		os.system('{0} --careful -b -i -O8 --lossy={1} -k={2} "Images/{3}" {4}'.format(
			__Gifsicle,
			Config["Settings"]["Optimize"]["Gifsicle"]["Lossy"],
			Config["Settings"]["Optimize"]["Gifsicle"]["Colors"],
			__Name,
			"-i -V" if Config["Settings"]["Packages"]["Logs"] else "-w"
			)
		)