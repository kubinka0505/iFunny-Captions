__OxiPNG = "OxiPNG"
__OxiPNG_Error_1 = "\n{1}{0}{2} not found!".format(__OxiPNG, Styles.Warning, Styles.Reset)
__OxiPNG_Error_2 = "\n{0}Image will not be optimized.{1}{2}".format(Styles.Error, Styles.Reset, __BEL)

if system() == "Windows":
	__OxiPNG = Variable_Search(Content = __OxiPNG)
	if __OxiPNG:
		if os.path.isfile(__OxiPNG):
			pass
		else:
			print(__OxiPNG_Error_1 + ' {1}("{0}"){2}'.format(
				__OxiPNG, Styles.Meta_Info, Styles.Reset) + __OxiPNG_Error_2
			)
	else:
		print(__OxiPNG_Error_1 + ' {1}("{0}"){2}'.format(
			__OxiPNG, Styles.Meta_Info, Styles.Reset) + __OxiPNG_Error_2
		)
else:
	try:
		if cache[__OxiPNG.lower()].is_installed:
			__OxiPNG = __OxiPNG.lower()
	except IndexError:
		print(__OxiPNG_Error_1 + ' {1}("{0}"){2}'.format(
			__OxiPNG, Styles.Meta_Info, Styles.Reset) + __OxiPNG_Error_2
		)