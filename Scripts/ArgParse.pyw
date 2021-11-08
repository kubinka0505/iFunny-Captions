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

p.add_argument("-nc", "--no_caption", help = SUPPRESS, action = "store_true")

#-----#

pr = p.add_argument_group("Required arguments")

Text_ = pr.add_argument(
		"-t", "--text", help = 'Caption text{0}. Cancels requirement if the "-nc" flag is used{1}'.format(
			Styles.Hidden, Styles.Reset
		),
		type = str,	metavar = '"str"', required = 1, default = Config["Text"]["Content"]
	)

if any(Arg in ["-nc", "--no_caption"] for Arg in os.sys.argv): Text_.required = 0

pr.add_argument(
	"-i", "--image", help = "URL / Absolute Path to Image",
	type = str, metavar = '"str"', required = 1, default = Config["Media"]["Image"]["URL_or_Path"]
)

#-----#

po = p.add_argument_group("Optional arguments")

po.add_argument(
	"-w", "--wrap", help = "Additional text wrap decrement",
	type = int, metavar = "int", default = Config["Text"]["Additional_Wrap"]
)

po.add_argument(
	"-k", "--kerning", help = "Text kerning",
	type = int, metavar = "int", default = Config["Text"]["Kerning"]
)

po.add_argument(
	"-f", "--font", help = "Font face",
	type = int, metavar = "0<=int<3", choices = [0, 1, 2], default = Config["Text"]["Font"]["Type"]
)

# Video

po.add_argument(
	"-ls", "--duration-start", help = "Video {1}start{2} value in suitable FFmpeg format. {0}(seconds reccomended){2}".format(
		Styles.Warning, Styles.Meta_Info_2, Styles.Reset
	),
	type = str, metavar = "str", default = Config["Media"]["Video"]["Duration"]["Start"]
)

po.add_argument(
	"-le", "--duration-end", help = "Encodes video {0}for{1} given amount of {0}seconds.centiseconds{1}".format(
		Styles.Meta_Info_2, Styles.Reset
	),
	type = float, metavar = "float>=0.", default = Config["Media"]["Video"]["Duration"]["End"]
)

## Audio
po.add_argument(
	"-a", "--audio", help = "URL / Absolute Path to audio. {0}If given, video will be produced{1}".format(
		Styles.Warning, Styles.Reset
	),
	type = str, metavar = '"str"', default = Config["Media"]["Video"]["Audio"]["URL_or_Path"]
)

po.add_argument(
	"-ab", "--audio-bitrate", help = "Audio Bitrate ({0}kb/s{1})".format(
		Styles.Meta_Info, Styles.Reset
	),
	type = int, metavar = "int>96", default = Config["Media"]["Video"]["Audio"]["Bitrate"]
)

po.add_argument(
	"-ac", "--audio-channels", help = "Amount of audio Channels",
	choices = [1, 2, 3, 4, 5], type = int, metavar = "5<=int>0", default = Config["Media"]["Video"]["Audio"]["Channels"]
)

#---#

po.add_argument(
	"-d", "--delay", help = "Delay between frames ({0}ms{1})".format(
	Styles.Meta_Info, Styles.Reset
	),
	type = int, metavar = "int>1", default = Config["Settings"]["Delay"]
)

PES = "10,67,112,150,25"
po.add_argument(
	"-pes", "--design", help = "CSV of {0}Percentage_Elements_Size{1} keys in configuration file".format(Styles.Meta_Info_2, Styles.Reset),
	type = str, metavar = "*int>0,[:3]", default = PES
)

po.add_argument(
	"-c", "--colors", help = "CSV for text and caption field colors",
	type = str, metavar = "*str,[:2]", default = Config["Settings"]["Caption_Design"]["Colors"]["Text"] + "," + Config["Settings"]["Caption_Design"]["Colors"]["Caption_Field"]
)

po.add_argument(
	"-o", "--output", help = "Output file save directory",
	type = str, metavar = '"str"', default = __Out_Dir
)

po.add_argument(
	"-v", "--verbose", help = "Package logs visibility",
	type = int, metavar = "-1>=int<=1", choices = [-1, 0 ,1], default = Config["Settings"]["Verbose"]
)

po.add_argument(
	"-h", "--help", help = "Displays this message",
	action = "help", default = SUPPRESS
)

#-----#

ps = p.add_argument_group("Optional switch arguments")
ps.add_argument(
	"-sb", "--scale_back", help = "Scales the output file to the {0}450{2} pixels width.\
	{1}Improves font quality!{2}".format(
		Styles.Meta_Info, Styles.Meta_Info_2, Styles.Reset
	), action = ArgParseBool(Config["Media"]["Image"]["Scale_Back"])
)

ps.add_argument("-wm", "--watermark",
	help = "Adds old {0}iFunny{1} watermark on bottom right corner of the caption field".format(
		Styles.Warning, Styles.Reset
	), action = ArgParseBool(Config["Media"]["Image"]["Watermark"]))

ps.add_argument("-ki", "--keep_image",
	help = "Keeps image file {0}that is processed in video{1}, instead of removing it".format(
		Styles.Meta_Info_2, Styles.Reset
	), action = ArgParseBool(Config["Media"]["Video"]["Keep_Image"])
)

ps.add_argument("-no", "--optimize", help = "Disables media optimization", action = ArgParseBool(Config["Settings"]["Optimize"]["Enabled"]))
ps.add_argument("-dm", "--dark_mode", help = "Enables dark mode. {0}Ignores --colors automatically{1}".format(Styles.Error, Styles.Reset), action = ArgParseBool(Config["Settings"]["Dark_Mode"]["Enabled"]))
ps.add_argument("-cp", "--colored_prints", help = "Disables colored prints", action = ArgParseBool(Config["Settings"]["Colored_Prints"]["Enabled"]))
ps.add_argument("-m", "--no_metadata", help = "Removes metadata from made file, if it exists", action = ArgParseBool(Config["Settings"]["Add_Metadata"]))
ps.add_argument("-p", "--popup", help = "Enables final Tkinter message box", action = ArgParseBool(Config["Settings"]["Open_Folder"]))

#---#

args = p.parse_args()

Config["Text"]["Content"] = "Video" if not args.text else args.text
Config["Text"]["Additional_Wrap"] = args.wrap
Config["Text"]["Kerning"] = args.kerning
Config["Text"]["Font"]["Type"] = args.font
Config["Media"]["Image"]["URL_or_Path"] = args.image
Config["Media"]["Image"]["Scale_Back"] = args.scale_back
Config["Media"]["Image"]["Watermark"] = args.watermark
Duration = [
	str(args.duration_start) if args.duration_start else "0",
	str(args.duration_end) if args.duration_end else "0"
]
Config["Media"]["Video"]["Audio"]["URL_or_Path"] = args.audio
if args.audio:
	try:
		try: _AF = io.BytesIO(get(args.audio, stream = 1).raw.data)
		except: _AF = args.audio
		_AF = mFile(_AF)
		_AB = round(_AF.info.bitrate / 1000)
	except: raise SystemExit(Styles.Error + "Couldn't read an audio file. Exiting." + Styles.Reset)
	Config["Media"]["Video"]["Audio"]["Bitrate"] = args.audio_bitrate if _AB > args.audio_bitrate else _AB
	Config["Media"]["Video"]["Audio"]["Channels"] = args.audio_channels

try: Config["Settings"]["Delay"] = Delay(Image.open(get(args.image, stream = 1).raw)) if not args.delay else args.delay
except: Config["Settings"]["Delay"] = args.delay

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

Config["Media"]["Video"]["Keep_Image"] = args.keep_image
Config["Settings"]["Colored_Prints"]["Enabled"] = args.colored_prints
Config["Settings"]["Optimize"]["Enabled"] = args.optimize
Config["Settings"]["Open_Folder"] = args.popup