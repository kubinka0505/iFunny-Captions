[os.remove(Frame) for Frame in next(os.walk(__BaseDir))[2] if Frame.endswith("png")]

exec(open("Scripts/Utils.pyw", encoding = "utf-8").read())

try:
	Config = load(open("Config.json", encoding = "utf-8"))
except decoder.JSONDecodeError as Error:
	raise SystemExit("Haven't You forgot something? (Line {0} / Position {1})".format(Error.__dict__["lineno"], Error.__dict__["pos"]))

_COLP = Config["Settings"]["Colored_Prints"]

#---#

ImageFile.LOAD_TRUNCATED_IMAGES = True
__BEL = "" if Config["Settings"]["Sound"] else ""

class Styles():
	"""Colored Prints."""
	Red			= "\033[31m" if _COLP else ""
	Green		= "\033[32m" if _COLP else ""
	Yellow		= "\033[33m" if _COLP else ""
	LightBlue	= "\033[36m" if _COLP else ""
	DarkGray	= "\033[90m" if _COLP else ""
	LightRed	= "\033[91m" if _COLP else ""
	Reset		= "\033[0m" if _COLP else ""

try: os.mkdir("Images")
except FileExistsError: pass

