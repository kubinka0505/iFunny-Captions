print("{1}Removing Frame{0}...".format("" if len(Frames) < 2 else "s", Styles.Reset))
__REM_TIME = time()
Remove_Pictures()
__REM_TIME = timedelta(seconds = time() - __REM_TIME)