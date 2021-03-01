from __future__ import print_function
import os
import PIL
import numpy as np
from json import load
from requests import get
from random import choice
from textwrap import wrap
from platform import system
from string import printable
from PIL import Image, ImageColor, ImageDraw, ImageFont

__author__		= "kubinka0505"
__copyright__		= __author__
__credits__		= [__author__, "SuperCuber"]
__version__		= "0.4"
__date__		= "15.09.2020"
__status__		= "Development"
__license__		= "GPL V3"

exec(open(r"{0}\Scripts\Utils.py".format(os.getcwd())).read())		# import Scripts/Utils.py
exec(open(r"{0}\Scripts\Caption.py".format(os.getcwd())).read())	# import Scripts/Caption.py
exec(open(r"{0}\Scripts\Gifer.py".format(os.getcwd())).read())		# import Scripts/Gifer.py

__Path = "{0}\\Captions\\Caption_{1}.{2}"
__Format = "png"

if system() != "Windows":
	__Path.replace("\\", "/")

Captionized.save(__Path.format(os.getcwd(), Random_String(), __Format)) 
