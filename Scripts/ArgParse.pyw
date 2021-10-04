p = ap(
	description = "Pack of scripts providing widely customizable {0}iFunny Captions{1} generation".format(
		Styles.Warning, Styles.Reset
	),
	add_help = 0,
	formatter_class = \
		lambda prog, size = float("inf"): \
			__import__("argparse").HelpFormatter(
				prog,
				width = size,
				max_help_position = size
			)
	)

#-----#

pr = p.add_argument_group("Required arguments")
pr.add_argument(
	"-t", "--text", help = "Caption text",
	type = str,	metavar = '"str"', required = 1, default = SUPPRESS
)

pr.add_argument(
	"-i", "--image", help = "URL / Absolute Path to Image",
	type = str, metavar = '"str"', required = 1, default = SUPPRESS
)

#-----#

po = p.add_argument_group("Optional arguments")

po.add_argument(
	"-k", "--kerning", help = "Text kerning",
	type = int, metavar = "int", default = -1
)

po.add_argument(
	"-w", "--wrap", help = "Additional text wrap decrement",
	type = int, metavar = "int", default = 2
)

# Video

po.add_argument(
	"-ls", "--duration-start", help = "Video start value in suitable FFmpeg format. {0}(seconds reccomended){1}".format(
		Styles.Warning, Styles.Reset
	),
	type = str, metavar = "str", default = "0"
)

po.add_argument(
	"-le", "--duration-end", help = "Encodes video {0}for{1} given amount of {0}seconds{1}".format(
		Styles.Meta_Info_2, Styles.Reset
	),
	type = str, metavar = "str", default = "0"
)

## Audio
po.add_argument(
	"-a", "--audio", help = "URL / Absolute Path to audio. {0}If given, video will be produced{2}. {1}This won't keep the original input file's sound{2}".format(
		Styles.Warning, Styles.Error, Styles.Reset
	),
	type = str, metavar = '"str"', default = ""
)

po.add_argument(
	"-ab", "--audio-bitrate", help = "Audio Bitrate ({0}kb/s{1})".format(
		Styles.Meta_Info, Styles.Reset
	),
	type = int, metavar = "int>96", default = 1024
)

po.add_argument(
	"-ac", "--audio-channels", help = "Amount of audio Channels",
	choices = [1, 2, 3, 4], type = int, metavar = "4<=int>0", default = 2
)

#---#

po.add_argument(
	"-f", "--font", help = "Font face",
	type = int, metavar = "0<=int<3", choices = [0, 1, 2], default = 2
)

PES = "10,67,112,150,25"
po.add_argument(
	"-pes", "--design", help = "CSV of {0}Percentage_Elements_Size{1} keys in configuration file".format(Styles.Meta_Info_2, Styles.Reset),
	type = str, metavar = "*int>0,[:3]", default = PES
)

po.add_argument(
	"-c", "--colors", help = "CSV values for colors for default mode consecutively for text and caption field",
	type = str, metavar = "*str,[:2]", default = "#000,#FFF"
)

po.add_argument(
	"-d", "--delay", help = "Delay between frames (ms)",
	type = int, metavar = "int>1", default = 0
)

po.add_argument(
	"-o", "--output", help = "Output file save directory",
	type = str, metavar = '"str"', default = __Out_Dir
)

po.add_argument(
	"-v", "--verbose", help = "Package logs visibility",
	type = int, metavar = "int==-1<=1", choices = [-1, 0 ,1], default = 0
)

po.add_argument(
	"-h", "--help", help = "Displays this message",
	action = "help", default = SUPPRESS
)

#-----#

ps = p.add_argument_group("Optional switch arguments")
ps.add_argument(
	"-sb", "--scale-back", help = "Scales the output file to the original size of its first frame after processing.\
	{0}Can degrade image quality if its width is higher than 450 pixels!{1}".format(
		Styles.Error, Styles.Reset
	), action = "store_true"
)

ps.add_argument("-wm", "--watermark", help = "Adds old {0}iFunny{1} watermark on bottom right corner of the caption field".format(Styles.Warning, Styles.Reset), action = "store_true")
ps.add_argument("-dm", "--dark-mode", help = "Enables dark mode. {0}Ignores --colors automatically{1}".format(Styles.Error, Styles.Reset), action = "store_true")
ps.add_argument("-cp", "--colored-prints", help = "Disables colored prints", action = "store_false")
ps.add_argument("-p", "--popup", help = "Enables final Tkinter message box", action = "store_true")

#---#

if len(os.sys.argv) > 1:
	args = p.parse_args()

	Config["Text"]["Content"] = args.text
	Config["Text"]["Additional_Wrap"] = args.wrap
	Config["Text"]["Kerning"] = args.kerning
	Config["Media"]["Image"]["URL_or_Path"] = Get_Service(args.image)
	Config["Media"]["Image"]["Scale_Back"] = args.scale_back
	Config["Media"]["Image"]["Watermark"] = args.watermark
	Duration = [
		args.duration_start if args.duration_start else "0",
		args.duration_end if args.duration_end else "0"
	]
	Config["Media"]["Video"]["Audio"]["URL_or_Path"] = args.audio
	if args.audio:
		try: _AB = io.BytesIO(get(args.audio, stream = 1).raw.data)
		except: _AB = args.audio
		_AB = mFile(_AB).info.bitrate // 1000
		Config["Media"]["Video"]["Audio"]["Bitrate"] = args.audio_bitrate if _AB > args.audio_bitrate else _AB
		Config["Media"]["Video"]["Audio"]["Channels"] = args.audio_channels

	Config["Font"]["Type"] = args.font
	#if not args.delay:
	#	try:
	#		args.delay = Average_FPS(Image.open(
	#				os.path.abspath(Config["Media"]["Image"]["URL_or_Path"]) if os.path.exists(Config["Media"]["Image"]["URL_or_Path"]) else get(Config["Media"]["Image"]["URL_or_Path"], stream = 1).raw
	#			)
	#		)
	#	except:
	#		args.delay = 3
	Config["Settings"]["Delay"] = args.delay

	PES = Config["Settings"]["Caption_Design"]["Percentage_Elements_Size"]
	PES.update(
		{
		Key: Value for Key, Value in zip(
			PES, [int("".join(Char for Char in Character if Char.isdigit())) for Character in args.design.replace(" ", "").split(",")]
			)
		}
	)

	if args.dark_mode:
		Config["Settings"]["Dark_Mode"]["Enabled"] = args.dark_mode
		Config["Settings"]["Dark_Mode"]["After_Hour"] = 0

	C = Config["Settings"]["Caption_Design"]["Colors"]
	C.update({Key: Value for Key, Value in zip(C, args.colors.split(","))})

	__Out_Dir = os.path.abspath(os.path.expandvars(os.path.expanduser(args.output)))

	if args.verbose > 0:
		Config["Settings"]["Packages"]["Logs"] = args.verbose
		Config["Settings"]["Time_Logs"] = 1
	elif args.verbose < 0:
		os.sys.stdout = open(os.devnull, "w")
		os.sys.stderr = open(os.devnull, "w")

	Config["Settings"]["Colored_Prints"]["Enabled"] = args.colored_prints
	Config["Settings"]["Open_Folder"] = args.popup