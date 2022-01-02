p = ap(
	prog = "filedate",
	description = "Pack of scripts providing widely customizable {0}iFunny Captions{1} generation.".format(
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
	"-i", "--image", help = "URL / Absolute Path to Image. {0}As above{1}".format(
		Styles.Hidden, Styles.Reset
	),
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
	"-f", "--font", help = "Font face type",
	type = int, metavar = "0<int<3", choices = [0, 1, 2], default = Config["Text"]["Font"]["Type"]
)

# Video
po.add_argument(
	"-ls", "-ss", "--time-start", help = "Video {1}start{2} value in suitable FFmpeg format. {0}(seconds reccomended){2}".format(
		Styles.Warning, Styles.Meta_Info_2, Styles.Reset
	),
	type = str, metavar = "str", default = Config["Media"]["Video"]["Duration"]["Start"]
)

po.add_argument(
	"-le", "-to", "--time-end", help = "Encodes video {0}for{1} given amount of {0}seconds.milliseconds{1}".format(
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
	"-ab", "--audio-bitrate", help = "Audio Bitrate in {0}kb/s{1}".format(
		Styles.Meta_Info, Styles.Reset
	),
	type = int, metavar = "int>16", default = Config["Media"]["Video"]["Audio"]["Bitrate"]
)

po.add_argument(
	"-ac", "--audio-channels", help = "Amount of audio channels in a video",
	choices = [1, 2, 3, 4, 5], type = int, metavar = "6>int>0", default = Config["Media"]["Video"]["Audio"]["Channels"]
)

#---#

po.add_argument(
	"-d", "--delay", help = "Delay between frames in {0}ms{1}".format(
	Styles.Meta_Info, Styles.Reset
	),
	type = int, metavar = "int>1", default = Config["Settings"]["Delay"]
)

po.add_argument(
	"-l", "--loop-count", help = "Loop count. Numbers {0}< 1{1} means infinite.".format(
	Styles.Meta_Info_2, Styles.Reset
	),
	type = int, metavar = "int", default = Config["Settings"]["Delay"]
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
	"-o", "--output", help = "Output file directory",
	type = str, metavar = '"str"', default = __Out_Dir
)

Verbose_ = po.add_argument(
	"-v", "--verbose", help = "Package logs visibility",
	type = int, metavar = "-2<int<2", choices = [-1, 0 ,1], default = Config["Settings"]["Verbose"]
)

po.add_argument(
	"-h", "--help", help = "Displays this message",
	action = "help", default = SUPPRESS
)

#-----#

ps = p.add_argument_group("Optional switch arguments")
ps.add_argument(
	"-sb", "--scale_back", help = "Scales the output file to the {0}450{2} pixels width.\
	{1}Improves font quality{2}".format(
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

ps.add_argument("-no", "--no_optimize", help = "Disables media optimization. {0}Flag enabled forcefully if making a video{1}".format(
		Styles.Error, Styles.Reset
	), action = ArgParseBool(Config["Settings"]["Optimize"]["Enabled"])
)

ps.add_argument("-dm", "--dark_mode", help = "Enables dark mode. {0}Ignores --colors automatically{1}".format(Styles.Error, Styles.Reset), action = ArgParseBool(Config["Settings"]["Dark_Mode"]["Enabled"]))
ps.add_argument("-m", "--no_metadata", help = "Does not add metadata to a file", action = ArgParseBool(Config["Settings"]["Add_Metadata"]))
ps.add_argument("-p", "--popup", help = "Enables final Tkinter message box", action = ArgParseBool(Config["Settings"]["Open_Folder"]))

#---#

pd = p.add_argument_group("Optional debug arguments")

Debug = pd.add_argument("-test", "--debug", metavar = "\b", help = SUPPRESS)
if any(Arg in Verbose_.option_strings for Arg in os.sys.argv):
	Debug.help = "Checks the functionality of the program. Deletes the final file"

#---#

args = p.parse_args()

if all((not args.text, args.audio)):
	Config["Text"]["Content"] = args.audio.replace(os.sep, "/").split("/")[-1].split("?")[0].split("#")[0].split(".")[0]
else:
	Config["Text"]["Content"] = args.text
Config["Text"]["Additional_Wrap"] = args.wrap
Config["Text"]["Kerning"] = args.kerning
Config["Text"]["Font"]["Type"] = args.font
Config["Media"]["Image"]["URL_or_Path"] = args.image
Config["Media"]["Image"]["Scale_Back"] = args.scale_back
Config["Media"]["Image"]["Watermark"] = args.watermark
Duration = [str(Value) for Value in [
		str(args.time_start) if args.time_start else 0,
		str(args.time_end) if args.time_end else 0
	]
]
Config["Media"]["Video"]["Audio"]["URL_or_Path"] = args.audio
if args.audio:
	try:
		try: _AF = io.BytesIO(get(args.audio, stream = 1).raw.data)
		except: _AF = Get_Path(args.audio)
		_AF = mFile(_AF)
		_AB = round(_AF.info.bitrate / 1E3)
	except:
		raise SystemExit(Styles.Error + "Couldn't read an audio file. Exiting." + Styles.Reset)

	Config["Media"]["Video"]["Audio"]["Bitrate"] = args.audio_bitrate if _AB > args.audio_bitrate else _AB

	if Config["Media"]["Video"]["Audio"]["Bitrate"] > 319:
		Config["Media"]["Video"]["Audio"]["Bitrate"] = 320

	Config["Media"]["Video"]["Audio"]["Channels"] = args.audio_channels

try:
	if not args.delay:
		args.delay = Delay(Image.open(get(args.image, stream = 1).raw))
except:
	pass
finally:
	Config["Settings"]["Delay"] = args.delay

Config["Settings"]["Loop_Count"] = 0 if args.loop_count < 1 else args.loop_count

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

if args.verbose > 0:
	Config["Settings"]["Packages"]["Logs"] = args.verbose
	Config["Settings"]["Time_Logs"] = 1
elif args.verbose < 0:
	os.sys.stdout = open(os.devnull, "w")
	os.sys.stderr = open(os.devnull, "w")

Config["Media"]["Video"]["Keep_Image"] = args.keep_image
Config["Settings"]["Optimize"]["Enabled"] = args.no_optimize
Config["Settings"]["Open_Folder"] = args.popup

__Out_Dir = Get_Path(args.output)