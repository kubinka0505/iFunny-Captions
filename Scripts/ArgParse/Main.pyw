Parser = ap(
	prog = "iFunny_Captions.pyw",
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

Parser.add_argument(
	"-nc", "--no_caption",
	action = "store_true",
	help = SUPPRESS
)

#-----#

Required = Parser.add_argument_group("Required arguments")

Text_ = Required.add_argument(
		"-t", "--text",
		type = str,
		metavar = '"str"',
		default = Config["Text"]["Content"],
		required = 1,
		help = 'Caption text{0}. Cancels requirement if the "-nc" flag is used{1}'.format(
			Styles.Hidden, Styles.Reset
		)
	)

if any(Arg in ["-nc", "--no_caption"] for Arg in os.sys.argv):
	Text_.required = 0

Required.add_argument(
	"-i", "--image",
	type = str,
	metavar = '"str"',
	default = Config["Media"]["Image"]["URL_or_Path"],
	required = 1,
	help = "URL / Absolute Path to Image{0}. As above{1}".format(
		Styles.Hidden, Styles.Reset
	),
)

#-----#

Optional = Parser.add_argument_group("Optional arguments")

Optional.add_argument(
	"-w", "--wrap", help = "Additional text wrap decrement",
	type = int,
	metavar = "int",
	default = Config["Text"]["Additional_Wrap"]
)

Optional.add_argument(
	"-k", "--kerning",
	type = int,
	metavar = "int",
	default = Config["Text"]["Kerning"],
	help = "Text kerning"
)

Optional.add_argument(
	"-f", "--font",
	type = int,
	metavar = "0<int<3",
	choices = [0, 1, 2],
	default = Config["Text"]["Font"]["Type"],
	help = "Font face type",
)

# Video
Optional.add_argument(
	"-ls", "-ss", "--time-start",
	type = str,
	metavar = "str",
	default = Config["Media"]["Video"]["Duration"]["Start"],
	help = "Video {1}start{2} value in suitable FFmpeg format. {0}(seconds reccomended){2}".format(
		Styles.Warning, Styles.Meta_Info_2, Styles.Reset
	),
)

Optional.add_argument(
	"-le", "-to", "--time-end", help = "Encodes video {0}for{1} given amount of {0}seconds.milliseconds{1}".format(
		Styles.Meta_Info_2, Styles.Reset
	),
	type = float,
	metavar = "float>=0.",
	default = Config["Media"]["Video"]["Duration"]["End"]
)

## Audio
Optional.add_argument(
	"-a", "--audio",
	type = str,
	metavar = '"str"',
	default = Config["Media"]["Video"]["Audio"]["URL_or_Path"],
	help = "{0}URL / Absolute Path to audio{2}. {1}If given, video will be produced{2}".format(
		Styles.Info, Styles.Warning, Styles.Reset
	),
)

Optional.add_argument(
	"-ab", "--audio-bitrate",
	type = str,
	metavar = "[int]k",
	default = Config["Media"]["Video"]["Audio"]["Bitrate"],
	help = "Audio Bitrate in {0}kb/s{1}".format(
		Styles.Meta_Info, Styles.Reset
	),
)

Optional.add_argument(
	"-ac", "--audio-channels",
	type = int,
	metavar = "6>int>0",
	choices = [1, 2, 3, 4, 5],
	default = Config["Media"]["Video"]["Audio"]["Channels"],
	help = "Amount of audio channels in a video",
)

#---#

Optional.add_argument(
	"-d", "--delay",
	type = int,
	metavar = "int>1",
	default = Config["Settings"]["Delay"],
	help = "Delay between frames in {0}ms{1}".format(
		Styles.Meta_Info, Styles.Reset
	),
)

Optional.add_argument(
	"-l", "--loop-count",
	type = int,
	metavar = "int",
	default = Config["Settings"]["Delay"],
	help = "Loop count. Numbers {0}lower than 1{1} means infinite".format(
		Styles.Meta_Info_2, Styles.Reset
	),
)

Optional.add_argument(
	"-c", "--colors",
	type = str,
	metavar = "*str,[:2]", 
	default = ",".join([
		Config["Settings"]["Caption_Design"]["Colors"]["Text"],
		Config["Settings"]["Caption_Design"]["Colors"]["Caption_Field"]
	]),
	help = "CSV for text and caption field colors",
)

Optional.add_argument(
	"-o", "--output", help = "Output file directory",
	type = str,
	metavar = '"str"',
	default = __Out_Dir
)

Optional.add_argument(
	"-h", "--help",
	default = SUPPRESS,
	action = "help",
	help = "Displays this message"
)

#-----#

Switch = Parser.add_argument_group("Optional switch arguments")

Switch.add_argument(
	"-q", "--quiet",
	action = ArgParseBool(Config["Settings"]["Quiet"]),
	help = "Does not show the console output",
)

Switch.add_argument(
	"-sb", "--scale_back",
	action = ArgParseBool(Config["Media"]["Image"]["Scale_Back"]),
	help = "Scales the output file to the {0}1000{2} pixels width".format(
		Styles.Meta_Info, Styles.Meta_Info_2, Styles.Reset
	)
)

Switch.add_argument("-wm", "--watermark",
	action = ArgParseBool(Config["Media"]["Image"]["Watermark"]),
	help = "Adds old {0}iFunny{1} watermark on bottom right corner of the caption field".format(
		Styles.Warning, Styles.Reset
	)
)

Switch.add_argument(
	"-ki", "--keep_image",
	action = ArgParseBool(Config["Media"]["Video"]["Keep_Image"]),
	help = "Does not remove the image file that video is based on"
)

Switch.add_argument(
	"-no", "--no_optimize",
	action = ArgParseBool(Config["Settings"]["Optimize"]["Enabled"]),
	help = "Disables media optimization. {0}Enabled forcefully if making a video{1}".format(
		Styles.Error, Styles.Reset
	)
)

Switch.add_argument(
	"-dm", "--dark_mode",
	action = ArgParseBool(Config["Settings"]["Dark_Mode"]["Enabled"]),
	help = "Enables dark mode. {0}Ignores and overrides --colors{1}".format(
		Styles.Error, Styles.Reset
	)
)

Switch.add_argument(
	"-nm", "--no_metadata",
	action = ArgParseBool(Config["Settings"]["Add_Metadata"]),
	help = "Does not add metadata to a file"
)

Switch.add_argument(
	"-webm",
	action = ArgParseBool(Config["Media"]["Video"]["WebM"]),
	help = "Re-encodes video to VP9 WebM format. {0}Obsolete with static images{2}, {1}takes a very long time!{2}".format(
		Styles.Warning, Styles.Error, Styles.Reset
	)
)

Switch.add_argument(
	"-p", "--popup",
	action = ArgParseBool(Config["Settings"]["Open_Folder"]),
	help = "Enables final Tkinter message box"
)

#---#

args = Parser.parse_args()