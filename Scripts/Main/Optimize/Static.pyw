if Config["Settings"]["Optimize"]["Enabled"]:
	exec(open_("Packages_Location/PNGQuant"))
	if __PNGQuant:
		print("{4}Optimizing... {2}(PNGQuant, {1} colors, speed: {0}){3}".format(
			Config["Settings"]["Optimize"]["PNGQuant"]["Speed"],
			Config["Settings"]["Optimize"]["PNGQuant"]["Colors"],
			Styles.Meta_Info, Styles.Flaw, Styles.Reset
			)
		)

		os.system('{0} {2} --ext .png -f -s {1} --skip-if-larger --nofs "{3}" {4}'.format(
			__PNGQuant,
			Config["Settings"]["Optimize"]["PNGQuant"]["Speed"],
			Config["Settings"]["Optimize"]["PNGQuant"]["Colors"],
			__Name,
			"" if not Config["Settings"]["Packages"]["Logs"] else "-v"
			)
		)

	exec(open_("Packages_Location/OxiPNG"))
	try:
		if __OxiPNG:
			__OxiPNG_Args = ["a", "i 1", "o max", "p", "-strip all", "q" if not Config["Settings"]["Packages"]["Logs"] else "v"]
			__OxiPNG_Args = ["-" + Arg for Arg in __OxiPNG_Args]

			print("{3}Optimizing... {1}(OxiPNG, {0}){2}".format(
				", ".join(__OxiPNG_Args),
				Styles.Meta_Info, Styles.Flaw, Styles.Reset
				)
			)

			os.system('{0} "{1}" {2}'.format(
				__OxiPNG, __Name,
				" ".join(__OxiPNG_Args)
				)
			)
	except KeyboardInterrupt:
		print(Styles.Flaw + "\nOxiPNG optimization was interrupted by the user." + Styles.Reset + __BEL)
