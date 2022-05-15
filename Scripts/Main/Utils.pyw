session = Session()
session.headers.update(
	{
		"User-Agent":
		"Mozilla/5.0 (Windows NT 10.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
	}
)
get = session.get

#-=-=-=-#

__Out_Dir = "Images"
__Dynamic_Formats = ("apng", "gif", "gifv"), ("3gp", "flv", "mkv", "mov", "mp4", "webm")

try:
	Config = load(open("Config.json", encoding = "U8"))
except decoder.JSONDecodeError as Error:
	raise SystemExit("Haven't You forgot something? (Line {0} / Position {1})".format(
		Error.__dict__["lineno"], Error.__dict__["pos"]
		)
	)

__BEL = "" if Config["Settings"]["Sound"] else ""
_COLP = Config["Settings"]["Colored_Prints"]
_COLPC = _COLP["Colors"]
_COLP = _COLP["Enabled"]

#-=-=-=-#

Image.MAX_IMAGE_PIXELS = float("inf")
ImageFile.LOAD_TRUNCATED_IMAGES = 1
Image.warnings.filterwarnings("ignore", category = UserWarning)
os.sys.platform = os.sys.platform.lower()
UNICODE_EMOJI_ENGLISH = {Key.lower(): Value for Key, Value in UNICODE_EMOJI_ENGLISH.items()}

#-=-=-=-#

class Styles:
	"""Colored Prints"""
	Error = _COLPC["Error"]
	OK = _COLPC["OK"]
	Flaw = _COLPC["Flaw"]
	Info = _COLPC["Info"]["Main"]
	Meta_Info = _COLPC["Info"]["Meta"]["1"]
	Meta_Info_2 = _COLPC["Info"]["Meta"]["2"]

_CLS = Styles
for Variable in list(vars(_CLS))[2:-2]:
	exec('{0}.{1} = "{2}" if _COLP else ""'.format(
		_CLS.__name__, Variable,
		fg(*IC.getrgb(Color(getattr(_CLS, Variable)).hex_l))
		)
	)

_CLS.Warning = fg(*IC.getrgb("#FC0")) if _COLP else ""
_CLS.Reset = fg.rs if _COLP else ""
_CLS.Hidden = fg(*IC.getrgb("#1A1A1A")) if _COLP else ""

#-=-=-=-#

try: os.mkdir(__Out_Dir)
except FileExistsError: pass

os.system("")