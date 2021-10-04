try:
	Frame_Size = Image.open(Frames[0]).size
except IndexError:
	rmtree(os.sep.join(__Folders) + os.sep + __Folder_Name)
	raise SystemExit(Styles.Flaw + "\nNo frames were found - cache folder was wiped.\nPlease Re-run the program." + Styles.Reset)

print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))

__MKE_TIME = time()
for Frame in Frames:
	try:
		Caption = Image.open(Frame)
		#---#
		exec(open("./Scripts/Caption.pyw", encoding = "utf-8").read())	
		exec(open("./Scripts/Gifer.pyw", encoding = "utf-8").read())
		#---#
		# if Config["Settings"]["Optimize"]["Enabled"]: Captionized = Captionized.convert(mode = "P", palette = Image.ADAPTIVE)
		Captionized.save(Frame)
			
	except FileNotFoundError:
		pass
__MKE_TIME = timedelta(seconds = time() - __MKE_TIME)

#---#

Scale_Back = 0
if Config["Media"]["Image"]["Scale_Back"]:
	Scale_Back_ = Captionized.size

	SB_Width = Frame_Size[0]
	SB_Percentage = SB_Width / float(Scale_Back_[0])
	SB_Height_Size = int((float(Scale_Back_[1]) * float(SB_Percentage)))
	Scale_Back = (SB_Width, SB_Height_Size)

print("Saving {0}...{1}".format("PNG" if len(Frames) == 1 else "GIF", Styles.Info))