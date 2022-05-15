os.chdir(__BaseDir + "/..")
Dirname = os.path.abspath(Update_Info["name"])

Archive = "http://github.com/kubinka0505/iFunny-Captions/archive/refs/tags/" + Update_Info["name"] + ".zip"
Archive_Path = os.path.abspath(Archive.split("/")[-1])

#---#

print("Downloading archive...")
urlretrieve(Archive, Archive_Path)

print("Unpacking archive...")
unpack_archive(Archive.split("/")[-1], Dirname)

#---#

print("Removing useless files...")
os.chdir(Dirname); os.chdir(os.listdir()[0])
for File in os.listdir(): mv(File, "..")

os.remove(Archive_Path)
os.chdir("..")
[rmtree(File) for File in os.listdir() if "iFunny" in File]

#-----#

Command = r'start /max explorer /select,"{0}\__init__.pyw"'
if not system() == "Windows":
	Command = 'nautilus "{0}"'

call(Command.format(Dirname), shell = 1)

#---#

raise SystemExit("Done!" + __BEL)