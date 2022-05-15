__FFmpeg = "FFmpeg"
__FFmpeg_Error_1 = "\n{1}{0}{2} not found!".format(__FFmpeg, Styles.Warning, Styles.Reset)
__FFmpeg_Error_2 = "\n{0}Image will not be processed.{1}{2}".format(Styles.Error, Styles.Reset, __BEL)

if system() == "Windows":
	__FFmpeg = Variable_Search(Content = __FFmpeg)
	if __FFmpeg:
		if os.path.isfile(__FFmpeg):
			pass
		else:
			print(__FFmpeg_Error_1 + ' {1}("{0}"){2}'.format(
				__FFmpeg, Styles.Meta_Info, Styles.Reset) + __FFmpeg_Error_2
			)
	else:
		print(__FFmpeg_Error_1 + ' {1}("{0}"){2}'.format(
			__FFmpeg, Styles.Meta_Info, Styles.Reset) + __FFmpeg_Error_2
		)
else:
	try:
		if cache[__FFmpeg.lower()].is_installed:
			__FFmpeg = __FFmpeg.lower()
	except IndexError:
		print(__FFmpeg_Error_1 + ' {1}("{0}"){2}'.format(
			__FFmpeg, Styles.Meta_Info, Styles.Reset) + __FFmpeg_Error_2
		)

try:
	__FFmpeg += " -fflags +bitexact -flags:v +bitexact -flags:a +bitexact"
except:
	pass