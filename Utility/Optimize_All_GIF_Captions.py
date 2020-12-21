import os
from json import load
from time import sleep

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")
Factor = load(open("Config.json", encoding = "utf-8"))["Settings"]["Optimize"]["Lossy"]
os.chdir("Images")

for File in os.listdir(os.getcwd()):
	if File.endswith(".gif"):
		os.system("gifsicle --careful -b -O3 --lossy={0} {1} -w".format(File, Factor))
		sleep(len(File) / 125)