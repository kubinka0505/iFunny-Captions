__Folder_Name = re.compile("[^a-zA-Z0-9]").sub("_", str(Get_Service("".join(Config["Image"]["URL_or_Path"].split("//")[1:]))))

if not __Folder_Name:
	__Folder_Name = re.compile("[^a-zA-Z0-9]").sub("_", str("".join(Config["Image"]["URL_or_Path"])))
else:
	pass

__Folder_Name = __Folder_Name[:100]