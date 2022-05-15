__PNGQuant = "PNGQuant"
__PNGQuant_Error_1 = "\n{1}{0}{2} not found!".format(__PNGQuant, Styles.Warning, Styles.Reset)
__PNGQuant_Error_2 = "\n{0}Image will not be optimized.{1}{2}".format(Styles.Error, Styles.Reset, __BEL)

if system() == "Windows":
	__PNGQuant = Variable_Search(Content = __PNGQuant)
	if __PNGQuant:
		if os.path.isfile(__PNGQuant):
			pass
		else:
			print(__PNGQuant_Error_1 + ' {1}("{0}"){2}'.format(
				__PNGQuant, Styles.Meta_Info, Styles.Reset) + __PNGQuant_Error_2
			)
	else:
		print(__PNGQuant_Error_1 + ' {1}("{0}"){2}'.format(
			__PNGQuant, Styles.Meta_Info, Styles.Reset) + __PNGQuant_Error_2
		)
else:
	try:
		if cache[__PNGQuant.lower()].is_installed:
			__PNGQuant = __PNGQuant.lower()
	except IndexError:
		print(__PNGQuant_Error_1 + ' {1}("{0}"){2}'.format(
			__PNGQuant, Styles.Meta_Info, Styles.Reset) + __PNGQuant_Error_2
		)