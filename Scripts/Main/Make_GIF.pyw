print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))
__MKE_TIME = time()
for Frame in Frames:
	try:
		Caption = Image.open(Frame)
		#---#
		exec(open("Scripts/Caption.pyw", encoding = "utf-8").read())	
		exec(open("Scripts/Gifer.pyw", encoding = "utf-8").read())
		#---#
		# if Config["Settings"]["Optimize"]: Captionized = Captionized.convert(mode = "P", palette = Image.ADAPTIVE)
		Captionized.save(Frame)
	except FileNotFoundError:
		pass
__MKE_TIME = timedelta(seconds = time() - __MKE_TIME)

print("Saving {0}...{1}".format("PNG" if len(Frames) == 1 else "GIF", Styles.LightBlue))