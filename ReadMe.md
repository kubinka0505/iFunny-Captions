<p align=center><a href=http://ifunny.co><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Main/iFunny-Captions.svg width=675></a></p>

<p align=center><a href=http://python.org/downloads/release/python-376><img src=https://img.shields.io/badge/Python-3.7.6-brightgreen?logo=python&logoColor=white&link=http://python.org/downloads/release/python-376&style=for-the-badge></a>　<a href=http://colab.research.google.com/github/kubinka0505/iFunny-Captions/blob/master/Documents/iFunny-Captions.ipynb><img src=https://img.shields.io/badge/colab-open-F9AB00?&logo=google-colab&logoColor=F9AB00&style=for-the-badge></a>　<a href=http://youtube.com/watch?v=r8KTluI9Q5Q><img src=http://shields.io/badge/showcase-watch-FF0000?logo=youtube&style=for-the-badge></p>

<p align=center><a href=http://github.com/kubinka0505/iFunny-Captions/releases/><img src=https://img.shields.io/github/v/release/kubinka0505/iFunny-Captions?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/iFunny-Captions/commit><img src=https://img.shields.io/github/last-commit/kubinka0505/iFunny-Captions?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/iFunny-Captions/issues><img src=https://img.shields.io/github/issues/kubinka0505/iFunny-Captions?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/iFunny-Captions/blob/master/License.txt><img src=https://img.shields.io/github/license/kubinka0505/iFunny-Captions?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>

<p align=center><img src=https://img.shields.io/tokei/lines/github/kubinka0505/iFunny-Captions?style=for-the-badge>　<img src=https://img.shields.io/github/languages/code-size/kubinka0505/iFunny-Captions?style=for-the-badge>　<img src=https://img.shields.io/codeclimate/maintainability/kubinka0505/iFunny-Captions?logo=code-climate&style=for-the-badge>　<img src=https://img.shields.io/codacy/grade/c8aeb5f42a38414da83d4156b546a4d1?logo=codacy&style=for-the-badge></p>

## Description 📝
Pack of scripts providing widely customizable [iFunny Captions](http://knowyourmeme.com/memes/gif-captions) generation.

## Capabilities 📈
|  | Android App | iOS App | `iFunny-Captions` |
|:-:|:-:|:-:|:-:|
| PNG Captions | ❌ | ❌ | ✔️ |
| GIF Captions | ✔️ | ✔️ | ✔️ |
| MP4 Captions | ❌ | ❌ | ✔️ |
| Font Changing ability | ❌ | ❌ | ✔️ |
| Image Optimization | ❌ | ❌ | ✔️ |
| Custom Fonts | ❌ | ❌ | ✔️ |
| Characters Limit | 140 | ❔ | **≈1000** ❔ |
| Emoji support | ✔️ | ✔️ | ✔️ |
| Caption Customization | ❌ | ❌ | ✔️ |
| Crop support | ✔️ | ✔️ | ❌ |
| Image size optimization | ❌ | ❌ | ✔️ |
| Graphical User Interface | ✔️ | ✔️ | ✔️ <img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Main/Google_Colab.svg width=25> |
| Command Line Interface | ❌ | ❌ | ✔️ |
---
## Completed & Planned Features 🧑‍💻
- ✔️ Completed
- ❌ In Development
---
- ✔️ PNG Captions
- ✔️ GIF Captions
- ✔️ Offline support
- ✔️ Most popular GIF services support<sup>1</sup>
- ✔️ GIF size reduction
- ✔️ Custom fonts support<sup>2</sup> <sup>3</sup>
- ✔️ Transparent GIF support
- ✔️ [Program Showcase](http://youtube.com/watch?v=r8KTluI9Q5Q) ([Colab](http://youtube.com/watch?v=Uf-D2iEOvDU))
- ❌ Get smaller FFmpeg build
- ✔️ ~~GUI Version~~ Colab Notebook
- ✔️ Emoji support<sup>3</sup>
- ✔️❌ Automatic text wrap

<sup>1</sup> - May not work with some URLs. Please look at [supported GIF services](http://github.com/kubinka0505/iFunny-Captions#supported-gif-services-%EF%B8%8F) below.<br>
<sup>2</sup> - Please look at [Custom Fonts](http://github.com/kubinka0505/iFunny-Captions/wiki/Custom-Fonts) section in wiki.<br>
<sup>3</sup> - Problems with wrap height might occur.

## Requirements 📥
Programs:
- [`Python >= 3.6`](http://www.python.org/downloads) 🐍

Modules:
- [`Pillow >= 5.1.0`](http://github.com/python-pillow/Pillow) - Making images 🖼️
- [`requests >= 2.13`](http://github.com/psf/requests) - URL fetching 🔗
- [`emoji >= 0.4.5`](http://github.com/carpedm20/emoji) - Text to emoji support ✨
- [`clipboard >= 0.0.4`](http://github.com/terryyin/clipboard) - Clipboard values handling 📋
- [`sty >= 0.0.4`](https://github.com/vaab/colour) - Colored prints 🎨
- [`colour >= 0.1.5`](http://github.com/colour) - Colored text values handling 🎨
- [`unidecode`](http://github.com/avian2/unidecode) - [Text normalization](http://wikipedia.org/wiki/Text_normalization#Techniques) ⚙️
- [`auepa`](http://github.com/kubinka0505/auepa) - API for [EmojiPedia](http://emojipedia.org) 📕 fetching *(optional)*

Packages (bold links are **Windows** static executable binaries):
- [**`FFmpeg >= 4.2.0`**](http://videohelp.com/software/ffmpeg/old-versions) - Since `PIL.ImageSequence.Iterator` messes up the frames colors.
- [**`Gifsicle >= 1.92-2`**](http://eternallybored.org/misc/gifsicle/releases) - **Check after 64-bit if possible!** ([`Scale_Back`](http://github.com/kubinka0505/iFunny-Captions/wiki/Known-Issues-%F0%9F%93%9D%F0%9F%90%9B#4-scale_back-option-doesnt-work) option)
- [**`PNGQuant >= 2.14`**](http://pngquant.org/#download) *(optional)*
- [**`OxiPNG >= 5.0.1`**](https://github.com/shssoichiro/oxipng/releases) *(optional)*
- [`Python3-PIP`](http://packages.debian.org/sid/python3-pip)</a><sup>1</sup>
- [`Python3-TK`](http://packages.debian.org/sid/python3-tk)</a><sup>1</sup>

<sup>1</sup> - Required on Linux

---
## Installation & Usage 📝

**When on Linux**, install packages using this one-liner:
```bash
sudo apt-get install git python3-apt python3-pip python3-tk ffmpeg pngquant gifsicle
```
1. Clone the repository and move to its directory.
	```bash
	git clone http://github.com/kubinka0505/iFunny-Captions
	cd iFunny-Captions
	```
2. Install required modules	 by inputting `pip install -r requirements.txt`
3. Allocate [the required files](http://github.com/kubinka0505/iFunny-Captions#requirements-) to `PATH` system environment variable <s>or move them to repository folder</s>.
4. Modify the parameters in the `Config.json`. [Its documentation can be found here](http://github.com/kubinka0505/iFunny-Captions/wiki/Configuration-Documentation).
5. Open shell script file named `Run`. Supports positional arguments - type `python __init__.pyw -h` for more.
6. Share Your image from the `Images` directory.

## Meta Info ℹ️
All versions of this project have been tested on:
| OS | Distribution | OS Version | Python Version | System Architecture (`bits`) |
|:-:|:-:|:-:|:-:|:-:|
Windows | ― | 10 | 3.7.6 | 32, 64
Linux | Ubuntu | LTS 21.04 | 3.8.10 | 64 |

[**In case of problems create issue.**](http://github.com/kubinka0505/iFunny-Captions/issues/new/choose)

---
### Supported GIF services 🗃️

In case if service is not working - copy its **direct non-static image URL**.
<table>
  <thead>
	<tr>
		<th>Tenor</th>
		<th>Giphy</th>
		<th>Gfycat</th>
		<th>Tumblr<br>(<code>GIFV</code>)</th>
		<th>ImgFlip</th>
		<th>GifImage</th>
		<th>BestAnimations</th>
		<th>GifFinder</th>
		<th>ReactionGIFs</th>
	</tr>
  </thead>
  <tbody>
	<tr align=center>
		<td><a href=http://tenor.com target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Tenor.svg alt=Tenor width=65></a></td>
		<td><a href=http://giphy.com target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Giphy.svg alt=Giphy width=65></a></td>
		<td><a href=http://gfycat.com target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Gfycat.svg alt=Gfycat width=65></a></td>
		<td><a href=http://tumblr.com target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Tumblr.svg alt=Tumblr width=65></a></td>
		<td><a href=http://imgflip.com target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ImgFlip.svg alt=ImgFlip width=65></a></td>
		<td><a href=http://gifimage.net target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifImage.png alt=GifImage width=65></a></td>
		<td><a href=http://bestanimations.com target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/BestAnimations.png alt=BestAnimations width=65></a></td>
		<td><a href=http://gif-finder.com target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifFinder.png alt=GifFinder width=65></a></td>
		<td><a href=http://reactiongifs.us target="_blank"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ReactionGIFs.svg alt=ReactionGIFs width=65></a></td>
	</tr>
  </tbody>
</table>

---
### Comparisons 🔢

- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | iFunny's<br>Android App | 29 seconds<br>890 microseconds<br>*+ saving to device* | 1.62 megabytes<br>(1629670 bytes) | <img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/1/iFunny.gif width=200> |
  | kubinka0505's<br>"iFunny-Captions | 40 seconds<br>514 microseconds | 675 kilobytes<br>(690476 bytes) | <img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/1/iFunny-Captions.gif width=200> |
- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | iFunny's<br>Android App | 12 seconds<br>900 microseconds<br>*+ saving to device* | 535 kilobytes<br>(535869 bytes) | <img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/2/iFunny.gif width=200> |
  | kubinka0505's<br>"iFunny-Captions | 9 seconds<br>453 microseconds | 210 kilobytes<br>(214781 bytes) | <img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/2/iFunny-Captions.gif width=200> |
---
| Tested With | App Version | Device's Processor |
|:-:|:-:|:-:|
| PC | 2.6 | Intel Core i3-2120 |
| Huawei P10 Lite | 6.15.3 | HiSilicon Kirin 658 |