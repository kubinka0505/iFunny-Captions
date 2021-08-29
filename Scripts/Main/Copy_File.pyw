for File in next(os.walk("."))[2]:
	if File.endswith("png"):
		try:
			copyfile(os.path.abspath(File), __BaseDir + "/" + File)
			#os.rename(File, "Frame_{0}.png".format(str(__FileToCopy.index(File)).zfill(5)))
		except KeyboardInterrupt:
			print("{1}Warning{2}: User interrupted the frames copying process. Copied {1}{0}{2} frames so far.{3}".format(
				str(
					len(
						[File for File in next(os.walk("."))[2] if File.endswith("png")]
						)
					), Styles.Warning, Styles.Reset, __BEL
				)
			)