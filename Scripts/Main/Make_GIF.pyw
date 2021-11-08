try:
	Frame_Size = Image.open(Frames[0]).size
except IndexError:
	rmtree(os.sep.join(__Folders) + os.sep + __Folder_Name)
	raise SystemExit(Styles.Flaw + "\nNo frames were found - cache folder was wiped.\nPlease Re-run the program." + Styles.Reset)

print("Making {0}...".format("PNG" if len(Frames) == 1 else "GIF"))

#---#

if Config["Media"]["Image"]["Scale_Back"]:
	Original_Image = Config["Media"]["Image"]["URL_or_Path"]
	if not os.path.exists(Config["Media"]["Image"]["URL_or_Path"]):
		Original_Image = get(Get_Service(Config["Media"]["Image"]["URL_or_Path"]), stream = 1).raw
	Original_Image = Image.open(Original_Image).convert("RGBA")

__MKE_TIME = time()
for Frame in Frames:
	try:
		Caption = Frame_ = Image.open(Frame).convert("RGBA")
		#---#
		exec(open_("../Caption"))
		exec(open_("../Gifer"))
		#---#
		if Config["Media"]["Image"]["Scale_Back"]:
			Scale_Back_ = Captionized.size
			#---#
			SB_Width = Frame_Size[0]
			SB_Percentage = SB_Width / float(Scale_Back_[0])
			SB_Height_Size = int((float(Scale_Back_[1]) * float(SB_Percentage)))
			#---#
			Captionized = Captionized.resize((SB_Width, SB_Height_Size), Image.LANCZOS)

			Captionized.paste(
				Frame_,
				(
					(Captionized.size[0] - Frame_.size[0]) // 2,
					Captionized.size[1] - Frame_.size[1]
				),
				Frame_
			)
		#---#
		Captionized.save(Frame)
	except FileNotFoundError:
		pass
__MKE_TIME = timedelta(seconds = time() - __MKE_TIME)

#---#

print("Saving {0}...{1}".format("PNG" if len(Frames) == 1 else "GIF", Styles.Info))