__Name = "{0}_{1}.{2}".format(
	re.sub("[^\w\-_\. ]", "_", Config["Text"]["Content"][:192]),\
	Random_String(8),
	"png" if len(Frames) == 1 else "gif"
	).replace(" ", "_")