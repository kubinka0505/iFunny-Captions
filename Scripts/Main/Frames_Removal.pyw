print("{1}Removing Frame{0}...".format("" if len(Frames) == 1 else "s", Styles.Reset))
__REM_TIME = time()
[os.remove(Frame) for Frame in next(os.walk("."))[2] if Frame.endswith("png")]
__REM_TIME = timedelta(seconds = time() - __REM_TIME)
print("{0}Done!{1}".format(Styles.Green, Styles.Reset))
