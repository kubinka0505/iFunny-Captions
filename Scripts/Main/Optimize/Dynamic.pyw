exec(open_("Packages_Location/Gifsicle"))

#-=-=-=-#

try:
	os.system('{0} -i "Frame_%05d.png" -vf palettegen=reserve_transparent=1 -gifflags -offsetting "Palette.png" -y {1}'.format(
		__FFmpeg,
		"-hide_banner -loglevel panic" if Config["Settings"]["Logs"]["Packages"] else ""
		)
	)

	os.system('{0} -i "Frame_%05d.png" -i "Palette.png" -lavfi paletteuse=alpha_threshold=128 "{1}" -y {2}'.format(
		__FFmpeg,
		__Name,
		"-hide_banner -loglevel panic" if Config["Settings"]["Logs"]["Packages"] else ""
		)
	)

	os.system('{0} --careful --no-comments -b {1}"{2}" -l{3} {4}'.format(
		__GifSicle,
		"-d{0} ".format(Config["Settings"]["Delay"]) if Config["Settings"]["Delay"] else "",
		__Name,
		str(Config["Settings"]["Loop_Count"]),
		"-w" if Config["Settings"]["Logs"]["Packages"] else "-i -cinfo -xinfo -sinfo -V"
		)
	)
except KeyboardInterrupt:
	print("{1}{0}{2}".format(KeyboardInterrupt.__name__, Styles.Error, Styles.Reset))

#-=-=-=-#

if Config["Settings"]["Optimize"]["Enabled"]:
	print("{4}Optimizing... {2}(Gifsicle, lossy: {0}, {1} colors){3}".format(
		Config["Settings"]["Optimize"]["Gifsicle"]["Lossy"],
		Config["Settings"]["Optimize"]["Gifsicle"]["Colors"],
		Styles.Meta_Info,
		Styles.Flaw,
		Styles.Reset
		)
	)
	# gifsicle -b -l0 -i -O8 --lossy=200 -k=256 "{$IN}" -V
	os.system('{0} -b -l{1} -i -O8 --lossy={2} -k={3} "{4}" {5}'.format(
		__GifSicle,
		str(Config["Settings"]["Loop_Count"]),
		Config["Settings"]["Optimize"]["Gifsicle"]["Lossy"],
		Config["Settings"]["Optimize"]["Gifsicle"]["Colors"],
		__Name,
		"-w" if Config["Settings"]["Logs"]["Packages"] else "-V"
		)
	)