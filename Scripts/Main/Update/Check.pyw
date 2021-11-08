Bool = __BaseDir + "/Scripts/Main/Update/No_Update"

if not os.path.exists(Bool):
	try:
		Update_Info = get("https://api.github.com/repos/kubinka0505/iFunny-Captions/releases/latest").json()
		if float(__version__) < float(Update_Info["tag_name"]):
			open(Bool, "w").close()

			Update = msgbox.askyesno(
				title = "New update available",
				message = "Current program version is {0}, but {1} is available.\n\nDo you want to upgrade?".format(
					__version__, Update_Info["tag_name"]
				)
			)

			if Update:
				exec(open_("Update/Update"))
				os.remove(Bool)
	except ConnectionError:
		pass