__Name = os.path.abspath("Images/" + __Name)

try:		
	if Grayscale(__Name):
		print("{0}Converting image to grayscale colormap...{1}".format(
			Styles.Meta_Info_2, Styles.Flaw
			)
		)
		if __Name.endswith("png"):
			Image.open(__Name).convert("L").save(__Name)
		else:
			os.system('{0} -b --transform-colormap gray "{1}" {2}'.format(
				__Gifsicle,
				__Name,
				"-i -cinfo -xinfo -sinfo -V" if Config["Settings"]["Packages"]["Logs"] else "-w"
				)
			)
except UserWarning:
	pass