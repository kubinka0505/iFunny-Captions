import os
from time import sleep

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("../Images")

for File in os.listdir(os.getcwd()):
	os.remove(File)
	print("Removed {0}".format(File))
	sleep(len(File) / 250)