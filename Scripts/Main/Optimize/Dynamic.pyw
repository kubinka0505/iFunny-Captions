exec(open_("Packages_Location/Gifsicle"))
#---#
try:
	os.system('{0} -i "Frame_%05d.png" -vf palettegen=reserve_transparent=1 -gifflags -offsetting "Palette.png" -y {1}'.format(
		__FFmpeg,
		"" if Config["Settings"]["Packages"]["Logs"] else "-hide_banner -loglevel panic"
		)
	)

	os.system('{0} -i "Frame_%05d.png" -i "Palette.png" -lavfi paletteuse=alpha_threshold=128 "{1}" -y {2}'.format(
		__FFmpeg,
		__Name,
		"" if Config["Settings"]["Packages"]["Logs"] else "-hide_banner -loglevel panic"
		)
	)

	os.system('{0} --careful --no-comments -b {1}"{2}" {3}'.format(
		__Gifsicle,
		"" if not Config["Settings"]["Delay"] else "-d{0} ".format(Config["Settings"]["Delay"]),
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
	os.system('{0} -b -i -O8 --lossy={1} -k={2} "{3}" {4}'.format(
		__Gifsicle,
		Config["Settings"]["Optimize"]["Gifsicle"]["Lossy"],
		Config["Settings"]["Optimize"]["Gifsicle"]["Colors"],
		__Name,
		"-i -V" if Config["Settings"]["Packages"]["Logs"] else "-w"
		)
	)