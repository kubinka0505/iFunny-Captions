__Audio = Config["Media"]["Video"]["Audio"]
__VID_TIME = 0

if __Audio["URL_or_Path"]:
	Audio_Data = ["AAC", __Audio["Bitrate"]] # kb/s
	Video_Data = ["MP4", "x264"]

	if __Audio["Channels"] != 2:
		Audio_Data.append('-af "pan=mono|c0=F{0}"')
		if __Audio["Channels"] == 3: Audio_Data[2] = Audio_Data[2].format("L")
		if __Audio["Channels"] == 4: Audio_Data[2] = Audio_Data[2].format("R")
		if __Audio["Channels"] == 1: Audio_Data[2] = "-ac 1"
	else:
		Audio_Data.append("")

	__Name_In = os.path.abspath(__Out_Dir + "/" + __Name.split(os.sep)[-1].split(".")[0] + "_.mp4")
	__Name_Out = __Name_In.replace(
		"_." + Video_Data[0].lower(),
		"." + Video_Data[0].lower()
	)

	#---#

	print("{3}Making video...{2} ({0} | {1} kb/s){4}".format(
		", ".join([str(Data) for Data in Video_Data]),
		" ".join([str(Data) for Data in Audio_Data[:2]]).upper(),
		Styles.Meta_Info, Styles.Meta_Info_2, Styles.Flaw
		)
	)

	__VID_TIME = time()
	os.system('{0} {1} -i "{2}" -ss {8} -i "{3}" {9} -movflags faststart -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p -c:v lib{4} -tune stillimage {5} -ar 44100 -shortest "{6}" -y -strict experimental -loglevel {7} -y'.format(
		__FFmpeg,
		"-ignore_loop 0" if __Name.endswith("gif") else "-loop 1",
		__Name,
		__Audio["URL_or_Path"],
		Video_Data[1],
		"-c:a {0} -b:a {1}k".format(*Audio_Data).lower(),
		__Name_In,
		"40" if Config["Settings"]["Packages"]["Logs"] else "-8 -hide_banner",
		Duration[0] if not Duration[0] == "0" else "0",
		("-t " + Duration[1]) if Duration[1] != "0" else ""
		)
	)

	# Trim useless duration
	os.system('{0} -ss 0 -i "{1}" -t {2} -pix_fmt yuv420p -c:v lib{3} -c:a aac -b:a {4}k {5} -map 0 -map_metadata 0:s:0 {6} "{7}" -y -strict experimental -loglevel {8}'.format(
		__FFmpeg,
		__Name_In,
		mFile(__Name_In).info.length,
		Video_Data[1],
		Audio_Data[1],
		Audio_Data[2],
		"-vf format=gray" if Grayscale else "",
		__Name_Out,
		"40" if Config["Settings"]["Packages"]["Logs"] else "-8 -hide_banner"
		)
	)

	__VID_TIME = timedelta(seconds = time() - __VID_TIME)

	os.remove(__Name_In)
	if not Config["Media"]["Video"]["Keep_Image"]:
		print("{0}Removing image caption...{1}".format(Styles.Meta_Info_2, Styles.Reset))
		os.remove(__Name)