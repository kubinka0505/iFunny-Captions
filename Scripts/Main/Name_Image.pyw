__Name = "{0}_{1}.{2}".format(
	re.compile("[^a-zA-Z]").sub("_", Config["Text"]["Content"][:192]),\
	Random_String(8),
	"png" if len(Frames) == 1 else "gif"
	)