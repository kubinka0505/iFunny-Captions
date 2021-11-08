__Folder_Name = re.sub("[^\w\-_\. ]", "_", str(Get_Service("".join(Config["Media"]["Image"]["URL_or_Path"].split("//")[1:]))))

if not __Folder_Name:
	__Folder_Name = re.sub("[^\w\-_\. ]", "_", str("".join(Config["Media"]["Image"]["URL_or_Path"])))

__Folder_Name = __Folder_Name[:100].replace(".", "_")