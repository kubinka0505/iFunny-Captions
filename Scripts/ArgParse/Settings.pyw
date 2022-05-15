if all((not args.text, args.audio)):
	Config["Text"]["Content"] = args.audio.replace(os.sep, "/").split("/")[-1].split("?")[0].split("#")[0].split(".")[0]
else:
	Config["Text"]["Content"] = args.text
Config["Text"]["Additional_Wrap"] = args.wrap
Config["Text"]["Kerning"] = (args.kerning * 4) - 1
Config["Text"]["Font"]["Type"] = args.font
Config["Media"]["Image"]["URL_or_Path"] = args.image
Config["Media"]["Image"]["Scale_Back"] = args.scale_back
Config["Media"]["Image"]["Watermark"] = args.watermark
Duration = list(map(str, [
		str(args.time_start) if args.time_start else 0,
		str(args.time_end) if args.time_end else 0
		]
	)
)
Config["Media"]["Video"]["Audio"]["URL_or_Path"] = args.audio
if args.audio:
	try:
		try:
			_AF = io.BytesIO(get(args.audio, stream = 1).raw.data)
		except:
			_AF = Get_Path(args.audio)
		_AF = mFile(_AF)
	except:
		raise SystemExit(Styles.Error + "Couldn't read an audio file. Exiting." + Styles.Reset)

	args.audio_bitrate = int("".join([Character for Character in str(args.audio_bitrate) if Character.isdigit()]))
	Config["Media"]["Video"]["Audio"]["Bitrate"] = args.audio_bitrate
	Config["Media"]["Video"]["Audio"]["Channels"] = args.audio_channels

try:
	if not args.delay:
		args.delay = Delay(Image.open(get(args.image, stream = 1).raw))
except:
	Config["Settings"]["Delay"] = args.delay
Config["Settings"]["Loop_Count"] = 0 if args.loop_count < 1 else args.loop_count

if args.dark_mode:
	Config["Settings"]["Dark_Mode"]["Enabled"] = args.dark_mode
	Config["Settings"]["Dark_Mode"]["After_Hour"] = 0

C = Config["Settings"]["Caption_Design"]["Colors"]
C.update({Key: Value for Key, Value in zip(C, args.colors.split(","))})

if args.quiet:
	os.sys.stdout = open(os.devnull, "w")
	os.sys.stderr = open(os.devnull, "w")
else:
	Config["Settings"]["Logs"]["Time"] = 1
Config["Settings"]["Logs"]["Packages"] = not Config["Settings"]["Logs"]["Packages"]

Config["Media"]["Video"]["Keep_Image"] = args.keep_image
Config["Media"]["Video"]["WebM"] = args.webm
Config["Settings"]["Optimize"]["Enabled"] = args.no_optimize
Config["Settings"]["Add_Metadata"] = args.no_metadata
Config["Settings"]["Open_Folder"] = args.popup

__Out_Dir = Get_Path(args.output)