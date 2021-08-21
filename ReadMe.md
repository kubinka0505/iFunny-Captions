<p align="center"><a href="https://ifunny.co"><img src=https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Main/iFunny-Captions.svg width=675></a></p>

<p align="center"><a href="https://python.org/downloads/release/python-376/"><img src="https://img.shields.io/badge/Python-3.7.6-brightgreen?style=for-the-badge&logoColor=white&link=https://python.org/downloads/release/python-376/&logo=python"></a>　<a href="https://colab.research.google.com/github/kubinka0505/iFunny-Captions/blob/master/Documents/iFunny-Captions%20(Demo).ipynb"><img src="https://img.shields.io/badge/colab-open-F9AB00?&logoColor=F9AB00&style=for-the-badge&logo=google-colab"></a></p>

<p align="center"><a href="https://github.com/kubinka0505/iFunny-Captions/releases/"><img src="https://img.shields.io/github/v/release/kubinka0505/iFunny-Captions?style=for-the-badge"></a>　<a href="https://github.com/kubinka0505/iFunny-Captions/commit/"><img src="https://img.shields.io/github/last-commit/kubinka0505/iFunny-Captions?style=for-the-badge"></a>　<a href="https://github.com/kubinka0505/iFunny-Captions/issues/"><img src="https://img.shields.io/github/issues/kubinka0505/iFunny-Captions?style=for-the-badge"></a>　<a href="https://github.com/kubinka0505/iFunny-Captions/blob/master/License.txt"><img src="https://img.shields.io/github/license/kubinka0505/iFunny-Captions?color=red&logo=readthedocs&logoColor=white&style=for-the-badge"></a></p>

<p align="center"><img src="https://img.shields.io/tokei/lines/github/kubinka0505/iFunny-Captions?style=for-the-badge">　<img src="https://img.shields.io/github/languages/code-size/kubinka0505/iFunny-Captions?style=for-the-badge">　<img src="https://img.shields.io/codeclimate/maintainability/kubinka0505/iFunny-Captions?logo=code-climate&style=for-the-badge"></p>

## Description 📝
I was very unsatisfied that there was only a mobile app for those captions, so I've decided to create one for the PC.

## Capabilities 📝
|  | Android App | iOS App | `iFunny-Captions` |
|:-:|:-:|:-:|:-:|
| PNG Captions | ❌ | ❌ | ✔️ |
| GIF Captions | ✔️ | ✔️ | ✔️ |
| Font Changing ability | ❌ | ❌ | ✔️ |
| Image Optimization | ❌ | ❌ | ✔️ |
| Custom Fonts | ❌ | ❌ | ✔️ |
| Characters Limit | 140 | ❔ | **≈1000** ❔ |
| Emoji support | ✔️ | ✔️ | ✔️ |
| Caption Customization | ❌ | ❌ | ✔️ |
| Crop support | ✔️ | ✔️ | ❌ |
| Image size optimization | ❌ | ❔ | ✔️ |
| Graphical User Interface | ✔️ | ✔️ | ✔️ <img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Main/Google_Colab.svg" width=25> |
| Command Line Interface | ❌ | ❌ | ✔️ |
---
## Completed & Planned Features 🧑‍💻
- ✔️ Completed
- ❌ In Development
---
- ✔️ PNG Captions
- ✔️ GIF Captions
- ✔️ Offline support<sup>1</sup>
- ✔️ Most popular GIF services support<sup>2</sup>
- ✔️ GIF size reduction
- ✔️ Custom fonts support<sup>3</sup> <sup>4</sup>
- ✔️ Transparent GIF support
- ✔️ [Program Showcase](https://youtube.com/watch?v=Uf-D2iEOvDU) ([Colab](https://youtube.com/watch?v=Uf-D2iEOvDU))
- ❌ Get smaller FFmpeg build
- ✔️ ~~GUI Version~~ Colab Notebook
- ✔️ Emoji support<sup>4</sup>
- ❌✔️ Automatic text wrap

<sup>1</sup> - **If You are on Windows, You need to replace backslashes with slashes in `URL / Path`!**

<sup>2</sup> - May not work with some URLs. Please look at [supported GIF services](https://github.com/kubinka0505/iFunny-Captions#supported-gif-services-%EF%B8%8F) below.

<sup>3</sup> - Please look at [Custom Fonts](https://github.com/kubinka0505/iFunny-Captions/wiki/Custom-Fonts) section in wiki.

<sup>4</sup> - Problems with wrap height might occur.

## Requirements 📥
Programs:
- `Python >= 3.6`](https://www.python.org/downloads/)

Modules:
- [`Pillow >= 5.1.0`](https://github.com/python-pillow/Pillow)
- [`requests >= 2.12.5`](https://github.com/psf/requests)
- [`emoji >= 0.4.5`](https://github.com/carpedm20/emoji/)
- [`clipboard >= 0.0.4`](https://github.com/terryyin/clipboard)
- [`auepa`](https://github.com/kubinka0505/auepa) *(optional)*

Packages (links are **Windows** static executable binaries):
- [**`FFmpeg >= 4.2.0`**](https://videohelp.com/software/ffmpeg/old-versions) - Since `PIL.ImageSequence.Iterator` messes up the frames colors.
- [**`Gifsicle >= 1.92-2`**](https://eternallybored.org/misc/gifsicle/releases)
- [**`PNGQuant >= 2.12.10`**](https://web.archive.org/web/*/https://pngquant.org/#download) *(optional)*
- `Python3-PIP`<sup>1</sup>
- `Python3-TK`<sup>1</sup>

<sup>1</sup> - Required on Linux

---
## Installation & Usage 📝

**When on Linux**, install packages using this oneliner:
```bash
sudo apt-get install git python3-pip python3-tk ffmpeg pngquant gifsicle
```
1. Clone the repository and move to its directory.
	```bash
	git clone https://github.com/kubinka0505/iFunny-Captions
	cd iFunny-Captions
	```
2. Install required modules  by inputting `pip install -r requirements.txt`
3. Move [the required files](https://github.com/kubinka0505/iFunny-Captions#requirements-) to repository folder or allocate them to `PATH` system environment variable.
4. Modify the parameters in the `Config.json`. [Its documentation can be found here](https://github.com/kubinka0505/iFunny-Captions/wiki/Configuration-Documentation).
5. Open shell script file named `Run` or input `python __init__.pyw` command.
6. Share Your image from the `Images` directory.

## Meta Info ℹ️
All versions of this project have been tested on:
| OS | Distribution | OS Version | Python Version | System Architecture (`bits`) |
|:-:|:-:|:-:|:-:|:-:
Windows | ― | 10 | 3.7.6 | 32, 64
Linux | Ubuntu | LTS 20.04 | 3.8.10 | 64 |

**[In case of problems create issue](https://github.com/kubinka0505/iFunny-Captions/issues/new/choose)**.

---
### Supported GIF services 🗃️

In case if service is not working - copy its **direct non-static image URL**.
<table>
  <thead>
    <tr>
      <th>Tenor</th>
      <th>Giphy</th>
      <th>Gfycat</th>
      <th>ImgFlip</th>
      <th>GifImage</th>
      <th>BestAnimations</th>
      <th>GifFinder</th>
      <th>ReactionGIFs</th>
    </tr>
  </thead>
  <tbody>
    <tr align=center>
      <td><a href="https://tenor.com"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Tenor.svg" alt="Tenor" width="65"></a></td>
      <td><a href="https://giphy.com"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Giphy.svg" alt="Giphy" width="65"></a></td>
      <td><a href="https://gfycat.com"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Gfycat.svg" alt="Gfycat" width="65"></a></td>
      <td><a href="https://imgflip.com"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ImgFlip.svg" alt="ImgFlip" width="65"></a></td>
      <td><a href="https://gifimage.net"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifImage.png" alt="GifImage" width="65"></a></td>
      <td><a href="https://bestanimations.com"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/BestAnimations.png" alt="BestAnimations" width="65"></a></td>
      <td><a href="https://gif-finder.com"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifFinder.png" alt="GifFinder" width="65"></a></td>
      <td><a href="https://reactiongifs.us"><img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ReactionGIFs.svg" alt="ReactionGIFs" width="65"></a></td>
    </tr>
  </tbody>
</table>

---
### Comparisons 🔢

- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | iFunny's<br>Android App | 29 seconds<br>890 microseconds<br>*+ saving to device* | 1.62 megabytes<br>(1629670 bytes) | <img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/1/iFunny.gif" width=200> |
  | kubinka0505's<br>"iFunny-Captions" | 40 seconds<br>514 microseconds | 675 kilobytes<br>(690476 bytes) | <img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/1/iFunny-Captions.gif" width=200> |
- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | iFunny's<br>Android App | 12 seconds<br>900 microseconds<br>*+ saving to device* | 535 kilobytes<br>(535869 bytes) | <img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/2/iFunny.gif" width=200> |
  | kubinka0505's<br>"iFunny-Captions" | 9 seconds<br>453 microseconds | 210 kilobytes<br>(214781 bytes) | <img src="https://raw.githubusercontent.com/kubinka0505/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/2/iFunny-Captions.gif" width=200> |
---
| Tested With | App Version | Device's Processor |
|:-:|:-:|:-:|
| PC | 2.6 | Intel Core i3-2120 |
| Huawei P10 Lite | 6.15.3 | HiSilicon Kirin 658 |