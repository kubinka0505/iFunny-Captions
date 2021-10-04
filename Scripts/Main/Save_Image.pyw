if os.path.exists(Config["Media"]["Image"]["URL_or_Path"]):
	__Image_Meta = "/".join([Part.capitalize() for Part in os.path.abspath(Config["Media"]["Image"]["URL_or_Path"]).lower().replace(os.path.expanduser("~").lower(), "~").replace(os.sep, "/").split("/")])
else: __Image_Meta = quote_plus(Config["Media"]["Image"]["URL_or_Path"])

#---#

__Meta = PngImagePlugin.PngInfo()
__Meta.__dict__ = {
	"chunks":
		[
			(b"tEXt",
			bytes("Text\x00{0}".format(
				demojize(Config["Text"]["Content"])
				),
				encoding = "utf-8")
			),
			(b"tEXt",
			bytes("Image\x00{0}".format(
				__Image_Meta
				),
				encoding = "utf-8")
			)
		]
	}

#---#

__SAV_TIME = time()
if len(Frames) == 1:
	PNG = Image.open(Frames[0])

	if Scale_Back:
		print(Styles.Meta_Info_2 + "Scaling back..." + Styles.Reset)
		PNG = PNG.resize(Scale_Back, Image.ANTIALIAS)

	PNG.save(__Name, pnginfo = __Meta)