__PNGQuant = "PNGQuant"
__PNGQuant_Error_1 = "\n{0}PNGQuant{1} not found!".format(Styles.Yellow, Styles.Reset)
__PNGQuant_Error_2 = "\n{0}Image will not be optimized.{1}{2}".format(Styles.Red, Styles.Reset, __BEL)

if system() == "Windows":
	if not Config["Settings"]["Packages"]["Location"][__PNGQuant]:
		for File in next(os.walk("."))[2]:
			if os.path.basename(File)[:6] == __PNGQuant.lower():
				try:
					__PNGQuant = os.path.abspath(File)
				except:
					pass
		else:
			__PNGQuant = Variable_Search(Content = __PNGQuant.lower())
			if __PNGQuant:
				if os.path.isfile(__PNGQuant):
					pass
				else:
					print(__PNGQuant_Error_1 + ' {1}("{0}"){2}'.format(__PNGQuant, Styles.DarkGray, Styles.Reset) + __PNGQuant_Error_2)
	else:
		__PNGQuant = os.path.abspath(Config["Settings"]["Packages"]["Location"][__PNGQuant])
		if os.path.isfile(__PNGQuant):
			pass
		else:
			print(__PNGQuant_Error + "({0})".format(__PNGQuant))
else:
	try:
		if cache[__PNGQuant.lower()].is_installed:
			__PNGQuant = __PNGQuant.lower()
	except:
		print(__PNGQuant_Error_1 + ' {1}("{0}"){2}'.format(__PNGQuant, Styles.DarkGray, Styles.Reset) + __PNGQuant_Error_2)
