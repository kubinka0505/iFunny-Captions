print(Styles.Meta_Info_2 + "Adding metadata..." + Styles.Reset)

#---#

Meta = {
	"Text": normalize(demojize(Config["Text"]["Content"])),
}

Meta["Image"] = Config["Media"]["Image"]["URL_or_Path"]

if os.path.exists(Config["Media"]["Image"]["URL_or_Path"]):
	Meta["Image"] = Get_Path(Config["Media"]["Image"]["URL_or_Path"]).replace(os.environ["UserProfile"], "~")

if Config["Media"]["Video"]["Audio"]["URL_or_Path"]:
	Meta["Audio"] = Config["Media"]["Video"]["Audio"]["URL_or_Path"]
	#---#
	if os.path.exists(Config["Media"]["Video"]["Audio"]["URL_or_Path"]):
		Meta["Audio"] = Get_Path(Config["Media"]["Video"]["Audio"]["URL_or_Path"]).replace(os.environ["UserProfile"], "~")
try:
	Meta["Image"] = Meta["Image"].replace(os.sep, "/")
	Meta["Audio"] = Meta["Audio"].replace(os.sep, "/").split("/")[-1].split(".")[0].replace("_", " ")
except KeyError: pass

#---#

try:
	File = mFile(__Name)
	#---#
	File["\xa9cmt"] = Meta["Text"]
	File["desc"] = Meta["Image"]
	try: File["\xa9nam"] = Meta["Audio"]
	except IndexError: pass
	#---#
	File.save()
except:
	if not __Name.endswith(__Dynamic_Formats):
		__Meta = PngImagePlugin.PngInfo()
		__Meta.__dict__ = {
			"chunks": [
				(b"tEXt", bytes("Text\x00{0}".format(Meta["Text"]), "U8")),
				(b"tEXt", bytes("Image\x00{0}".format(Meta["Image"]), "U8"))
			]
		}
		try:
			__Meta.__dict__["chunks"].append(
			(b"tEXt", bytes("Audio\x00{0}".format(Meta["Audio"]), "U8"))
		)
		except KeyError: pass
		Image.open(__Name).save(__Name, pnginfo = __Meta)