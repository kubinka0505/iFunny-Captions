__Audio = Config["Media"]["Video"]["Audio"]
try: __Audio["URL_or_Path"] = get(__Audio["URL_or_Path"]).url
except: __Audio["URL_or_Path"] = Get_Path(__Audio["URL_or_Path"])

Audio_Data = ["aac", str(__Audio["Bitrate"])]
Video_Data = ["MP4", "libx264"]

# Audio channels
if __Audio["Channels"] != 2:
	Audio_Data.append("-af ")
	if __Audio["Channels"] != 5:
		Audio_Data[2] += ('"pan=mono|c0=F{0}"')
		if __Audio["Channels"] == 3: Audio_Data[2] = Audio_Data[2].format("L")
		if __Audio["Channels"] == 4: Audio_Data[2] = Audio_Data[2].format("R")
		if __Audio["Channels"] == 1: Audio_Data[2] = "-ac 1"
	else: Audio_Data[2] += '"stereotools=mode=ms>rr" -ac 1'
else:
	Audio_Data.append("")

Audio_Data = [str(Value) for Value in Audio_Data]

#---#

__Name_In = os.path.abspath(__Out_Dir + "/" + __Name.split(os.sep)[-1].split(".")[0] + "_.mp4")
__Name_Out = __Name_In.replace(
	"_." + Video_Data[0].lower(),
	"." + Video_Data[0].lower()
)

#---#

print("{3}Making Video...{2} ({0} | {1} kb/s){4}".format(
	", ".join([str(Data).replace("lib", "") for Data in Video_Data]),
	" ".join([str(Data).replace("lib", "") for Data in Audio_Data[:2]]).upper(),
	Styles.Meta_Info, Styles.Meta_Info_2, Styles.Flaw
	)
)

__VID_TIME = time()
os.system('{0} -{1} -i "{2}" -ss {3} -i "{4}" {5} -movflags faststart -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p -c:v {6} -tune stillimage -sws_flags lanczos -c:a {7} -b:a {8}k -af aresample=resampler=soxr -ar 44100 -shortest -strict -2 "{9}" -y -loglevel {10} -y'.format(
	__FFmpeg,
	"ignore_loop 0" if __Name.endswith("gif") else "loop 1",
	__Name,
	Duration[0] if not Duration[0] == "0" else "0",
	__Audio["URL_or_Path"],
	("-t " + Duration[1]) if Duration[1] != "0" else "",
	Video_Data[1],
	*Audio_Data[:2],
	__Name_In,
	"40" if Config["Settings"]["Packages"]["Logs"] else "-8 -hide_banner"
	)
)

# Trim useless duration
os.system('{0} -ss 0 -i "{1}" -t {2} -pix_fmt yuv420p -c:v {3} -c:a {4} -b:a {5}k {6} -map 0 -map_metadata 0:s:0 {7} -strict -2 "{8}" -y -loglevel {9}'.format(
	__FFmpeg,
	__Name_In,
	mFile(__Name_In).info.length,
	Video_Data[1],
	*Audio_Data,
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