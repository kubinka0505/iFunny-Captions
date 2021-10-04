if len(Frames) == 1:
	if Config["Settings"]["Optimize"]["Enabled"]:
		exec(open("./Scripts/Main/Packages_Location/PNGQuant.pyw", encoding = "utf-8").read())
		if __PNGQuant:
			print("{4}Optimizing... {2}(PNGQuant, {1} colors, speed: {0}){3}".format(
					Config["Settings"]["Optimize"]["PNGQuant"]["Speed"],
					Config["Settings"]["Optimize"]["PNGQuant"]["Colors"],
					Styles.Meta_Info,
					Styles.Flaw,
					Styles.Reset
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