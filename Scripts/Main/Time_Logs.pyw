__SUM_TIME = __STA_TIME + __CNV_TIME + __MKE_TIME + __SAV_TIME + __REM_TIME
#---#
print("\nModules were loaded in:\t\t\t{1}{0}{2}.".format(str(__STA_TIME)[2:-3], Styles.Info, Styles.Reset))
print("Input {0} was converted to frames in:\t{2}{1}{3}.".format("URL" if Config["Media"]["Image"]["URL_or_Path"].startswith("http") else "file", str(__CNV_TIME)[2:-3], Styles.Info, Styles.Reset))
print("Frames were processed in:\t\t{1}{0}{2}.".format(str(__MKE_TIME)[2:-3], Styles.Info, Styles.Reset))
print("{0} was made in:\t\t\t{2}{1}{3}.".format("PNG" if len(Frames) == 1 else "GIF", str(__SAV_TIME)[2:-3], Styles.Info, Styles.Reset))
print("Frames were deleted in:\t\t\t{1}{0}{2}.".format(str(__REM_TIME)[2:-3], Styles.Info, Styles.Reset))
if __VID_TIME:
	print("Video was made in:\t\t\t{1}{0}{2}.".format(str(__VID_TIME)[2:-3], Styles.Info, Styles.Reset))
	__SUM_TIME += __VID_TIME
__SUM_TIME = str(__SUM_TIME)[2:]
print("All operations were done in:\t\t{1}{0}{2}.".format(__SUM_TIME[:-3], Styles.Info, Styles.Reset))