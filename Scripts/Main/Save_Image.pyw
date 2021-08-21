__Meta = PngImagePlugin.PngInfo()
__Meta.__dict__ = {
	"chunks":
		[
			(b"tEXt",
			bytes("Text\x00{0}".format(demojize(Config["Text"]["Content"])),
				encoding = "utf-8")
			),
			(b"tEXt",
			bytes("Image\x00{0}".format(Config["Image"]["URL_or_Path"]),
				encoding = "utf-8")
			)
		]
	}

__SAV_TIME = time()
if len(Frames) == 1:
	GIF = Image.open(Frames[0])
	GIF.save("Images/{0}".format(__Name),
	pnginfo = __Meta)