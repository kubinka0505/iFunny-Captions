p = ap(
	description = "Pack of scripts providing widely customizable {0}iFunny Captions{1} generation".format(
		Styles.Warning, Styles.Reset
	),
	add_help = False,
	formatter_class = \
		lambda prog, size = float("inf"): \
			__import__("argparse").HelpFormatter(
				prog,
				width = size,
				max_help_position = size
				)
	)

#-----#

pr = p.add_argument_group("Required \arguments")
pr.add_argument(
	"-t", "--text", help = "Caption text",
	type = str,	metavar = "\b", required = True, default = SUPPRESS
)

pr.add_argument(
	"-i", "--image", help = "URL / Absolute Path to Image",
	type = str, metavar = "\b", required = True, default = SUPPRESS
)

#-----#

po = p.add_argument_group("Optional arguments")

po.add_argument(
	"-k", "--kerning", help = "Text kerning",
	type = int, metavar = int.__name__, default = -1
)

po.add_argument(
	"-w", "--wrap", help = "Additional text wrap decrement",
	type = int, metavar = int.__name__, default = 2
)

po.add_argument(
	"-f", "--font", help = "Font face",
	type = int, metavar = "int>0<3", default = 2
)

PES = "10,67,112,150,25"
po.add_argument(
	"-pes", "--design", help = "CSV of `Percentage_Elements_Size` keys in configuration file",
	type = str, metavar = "*int>0,[:5]", default = PES
)

po.add_argument(
	"-d", "--delay", help = "Delay between frames (ms)",
	type = int, metavar = "int>1", default = 3
)

po.add_argument(
	"-h", "--help", help = "Displays this message",
	action = "help", default = SUPPRESS
)

#-----#

ps = p.add_argument_group("Optional switch arguments")
ps.add_argument(
	"-dm", "--dark_mode", help = "Enables dark mode with hour",
	type = int, metavar = "int>=0<24", default = 22
	)

ps.add_argument(
	"-sb", "--scale_back", help = "Scales picture to its original first frame size after processing.\
	{0}Can degrade image quality if its width is higher 450 pixels!{1}".format(
	Styles.Error, Styles.Reset
	), action = "store_true"
)

ps.add_argument("-cp", "--colored_prints", help = "Disables colored prints", action = "store_false")
ps.add_argument("-nop", "--no_popup", help = "Disables final Tkinter message box", action = "store_false")
ps.add_argument("-v", "--verbose", help = "Enables all package logs", action = "store_true")

#---#

if len(os.sys.argv) > 1:
	args = p.parse_args()

	Config["Text"]["Content"] = args.text
	Config["Text"]["Additional_Wrap"] = args.wrap
	Config["Text"]["Kerning"] = args.kerning
	Config["Image"]["URL_or_Path"] = args.image
	Config["Font"]["Type"] = args.font
	Config["Settings"]["Delay"] = args.delay

	PES = Config["Settings"]["Percentage_Elements_Size"]
	PES.update(
		{Key: Value for Key, Value in zip(
			PES,
			[int(Character) for Character in args.design.replace(" ", "").split(",") if Character.isdigit()]
			)
		}
	)

	try:
		Config["Settings"]["Dark_Mode"]["Enabled"] = False
		Config["Settings"]["Dark_Mode"]["After_Hour"] = args.dark_mode
	except AttributeError: pass

	if args.verbose:
		Config["Settings"]["Packages"]["Logs"] = args.verbose
		Config["Settings"]["Time_Logs"] = True

	Config["Settings"]["Colored_Prints"]["Enabled"] = args.colored_prints
	Config["Settings"]["Open_Folder"] = args.no_popup
	Config["Image"]["Scale_Back"] = args.scale_back
