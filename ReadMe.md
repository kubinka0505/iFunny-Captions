<p align=center><a href=http://ifunny.co><img src=http://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Main/iFunny-Captions.svg width=675></a></p>

<p align=center><a href=http://python.org/downloads/release/python-376><img src=http://img.shields.io/badge/Python-3.7.6-brightgreen?logo=python&logoColor=white&link=http://python.org/downloads/release/python-376&style=for-the-badge></a>　<a href=http://colab.research.google.com/github/kubinka0505/iFunny-Captions/blob/master/Documents/iFunny-Captions.ipynb><img src=http://img.shields.io/badge/colab-open-F9AB00?&logo=google-colab&logoColor=F9AB00&style=for-the-badge></a>　<a href=http://youtube.com/watch?v=r8KTluI9Q5Q><img src=http://shields.io/badge/showcase-watch-FF0000?logo=youtube&style=for-the-badge></p>

<p align=center><a href=http://github.com/kubinka0505/iFunny-Captions/releases/><img src=http://img.shields.io/github/v/release/kubinka0505/iFunny-Captions?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/iFunny-Captions/commit><img src=http://img.shields.io/github/last-commit/kubinka0505/iFunny-Captions?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/iFunny-Captions/issues><img src=http://img.shields.io/github/issues/kubinka0505/iFunny-Captions?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/iFunny-Captions/blob/master/License.txt><img src=http://img.shields.io/github/license/kubinka0505/iFunny-Captions?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>

<p align=center><img src=http://img.shields.io/tokei/lines/github/kubinka0505/iFunny-Captions?style=for-the-badge>　<img src=http://img.shields.io/github/languages/code-size/kubinka0505/iFunny-Captions?style=for-the-badge>　<img src=http://img.shields.io/codeclimate/maintainability/kubinka0505/iFunny-Captions?logo=code-climate&style=for-the-badge></p>

## Description 📝
Pack of scripts providing widely customizable <a href=http://knowyourmeme.com/memes/gif-captions target=_blank>iFunny Captions</a> generation.

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
- ✔️ <a href="http://youtube.com/watch?v=r8KTluI9Q5Q" target=_blank>Program Showcase</a> (<a href="http://youtube.com/watch?v=Uf-D2iEOvDU" target=_blank>Colab</a>)
- ❌ Get smaller FFmpeg build
- ✔️ ~~GUI Version~~ Colab Notebook
- ✔️ Emoji support<sup>3</sup>
- ✔️❌ Automatic text wrap

<sup>1</sup> - May not work with some URLs. Please look at [supported GIF services](http://github.com/kubinka0505/iFunny-Captions#supported-gif-services-%EF%B8%8F) below.<br>
<sup>2</sup> - Please look at <a href="http://github.com/kubinka0505/iFunny-Captions/wiki/Custom-Fonts">Custom Fonts</a> section in wiki.<br>
<sup>3</sup> - Problems with wrap height might occur.

## Requirements 📥
Programs:
- <a href="http://www.python.org/downloads" target=_blank>`Python >= 3.6`</a> 🐍

Modules:
- <a href=http://github.com/python-pillow/Pillow target=_blank>`Pillow >= 5.1.0`</a> - Making images 🖼️
- <a href=http://github.com/psf/requests target=_blank>`requests >= 2.12.5`</a> - URL fetching 🔗
- <a href=http://github.com/carpedm20/emoji target=_blank>`emoji >= 0.4.5`</a> - Text to emoji support ✨
- <a href=http://github.com/terryyin/clipboard target=_blank>`clipboard >= 0.0.4`</a> - Clipboard values handling 📋
- <a href=http://github.com/feluxe/sty target=_blank>`sty >= 0.0.4`</a> - Colored prints 🎨
- <a href=http://github.com/avian2/unidecode target=_blank>`unidecode`</a> - [Text normalization](http://en.wikipedia.org/wiki/Text_normalization#Techniques) ⚙️
- <a href=http://github.com/kubinka0505/auepa target=_blank>`auepa`</a> - API for [EmojiPedia](http://emojipedia.org) 📕 fetching *(optional)*

Packages (bold links are **Windows** static executable binaries):
- <a href=http://videohelp.com/software/ffmpeg/old-versions target=_blank>**`FFmpeg >= 4.2.0`**</a> - Since `PIL.ImageSequence.Iterator` messes up the frames colors.
- <a href=http://eternallybored.org/misc/gifsicle/releases target=_blank>**`Gifsicle >= 1.92-2`**</a> - **Check after 64-bit if possible!** (<a href=http://github.com/kubinka0505/iFunny-Captions/wiki/Known-Issues-%F0%9F%93%9D%F0%9F%90%9B#4-scale_back-option-doesnt-work target=_blank>`Scale_Back`</a> option)
- <a href=http://pngquant.org/#download target=_blank>**`PNGQuant >= 2.12.10`**</a> *(optional)*
- <a href=http://packages.debian.org/sid/python3-pip target=_blank>`Python3-PIP`</a><sup>1</sup>
- <a href=http://packages.debian.org/sid/python3-tk target=_blank>`Python3-TK`</a><sup>1</sup>

<sup>1</sup> - Required on Linux

---
## Installation & Usage 📝

**When on Linux**, install packages using this one-liner:
```bash
sudo apt-get install git python3-pip python3-tk ffmpeg pngquant gifsicle
```
1. Clone the repository and move to its directory.
	```bash
	git clone http://github.com/kubinka0505/iFunny-Captions
	cd iFunny-Captions
	```
2. Install required modules  by inputting `pip install -r requirements.txt`
3. Allocate [the required files](http://github.com/kubinka0505/iFunny-Captions#requirements-) to `PATH` system environment variable <s>or move them to repository folder</s>.
4. Modify the parameters in the `Config.json`. <a href=http://github.com/kubinka0505/iFunny-Captions/wiki/Configuration-Documentation target=_blank>Its documentation can be found here</a>.
5. Open shell script file named `Run`. Supports positional arguments - type `python __init__.pyw -h` for more.
6. Share Your image from the `Images` directory.

## Meta Info ℹ️
All versions of this project have been tested on:
| OS | Distribution | OS Version | Python Version | System Architecture (`bits`) |
|:-:|:-:|:-:|:-:|:-:|
Windows | ― | 10 | 3.7.6 | 32, 64
Linux | Ubuntu | LTS 20.04 | 3.8.10 | 64 |

<a href=http://github.com/kubinka0505/iFunny-Captions/issues/new/choose target=_blank>**In case of problems create issue.**</a>

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
      <td><a href=http://tenor.com target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Tenor.svg alt=Tenor width=65></a></td>
      <td><a href=http://giphy.com target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Giphy.svg alt=Giphy width=65></a></td>
      <td><a href=http://gfycat.com target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Gfycat.svg alt=Gfycat width=65></a></td>
      <td><a href=http://tumblr.com target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Tumblr.svg alt=Tumblr width=65></a></td>
      <td><a href=http://imgflip.com target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ImgFlip.svg alt=ImgFlip width=65></a></td>
      <td><a href=http://gifimage.net target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifImage.png alt=GifImage width=65></a></td>
      <td><a href=http://bestanimations.com target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/BestAnimations.png alt=BestAnimations width=65></a></td>
      <td><a href=http://gif-finder.com target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifFinder.png alt=GifFinder width=65></a></td>
      <td><a href=http://reactiongifs.us target=_blank><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ReactionGIFs.svg alt=ReactionGIFs width=65></a></td>
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