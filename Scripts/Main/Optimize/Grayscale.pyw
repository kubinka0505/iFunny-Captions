if Grayscale(__Name):
	Grayscale = 1
	print(Styles.Meta_Info_2 + "Converting image to grayscale colormap..." + Styles.Flaw)
	if __Name.endswith("png"):
		Image.open(__Name).convert("L").save(__Name)
	else:
		os.system('{0} -b --transform-colormap gray "{1}" {2}'.format(
			__GifSicle,
			__Name,
			"-i -cinfo -xinfo -sinfo -V" if Config["Settings"]["Logs"]["Packages"] else "-w"
			)
		)
else:
	Grayscale = 0