__FFmpeg = "FFmpeg"
__FFmpeg_Error_1 = "\n{0}FFmpeg{1} not found!".format(Styles.Yellow, Styles.Reset)
__FFmpeg_Error_2 = "\n{0}Image will not be processed.{1}{2}".format(Styles.Red, Styles.Reset, __BEL)

if not Config["Settings"]["Packages"]["Location"][__FFmpeg]:
	for File in next(os.walk("."))[2]:
		if os.path.basename(File)[:6] == __FFmpeg.lower():
			try:
				__FFmpeg = os.path.abspath(File)
			except:
				pass
	else:
		__FFmpeg = Variable_Search(Content = __FFmpeg.lower())
		if __FFmpeg:
			if os.path.isfile(__FFmpeg):
				pass
			else:
				raise SystemExit(__FFmpeg_Error_1 + ' {1}("{0}"){2}'.format(__FFmpeg, Styles.DarkGray, Styles.Reset) + __FFmpeg_Error_2)
else:
	__FFmpeg = os.path.abspath(Config["Settings"]["Packages"]["Location"][__FFmpeg])
	if os.path.isfile(__FFmpeg):
		pass
	else:
		raise SystemExit(__FFmpeg_Error + "({0})".format(__FFmpeg))