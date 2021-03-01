<p align="center"><a href="https://ifunny.co/"><img src="https://cdn.discordapp.com/attachments/267356180064501760/780370694482821140/iFunny_Captions.svg" width=750></a></p>

<p align="center"><a href="https://www.python.org/downloads/release/python-375/"><img src="https://img.shields.io/badge/Python-3.7.5-brightgreen?style=for-the-badge&logoColor=white&link=https://www.python.org/&https://www.python.org/downloads/&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAMAAAAMCGV4AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABVlBMVEUAAAA5e7Q3ebA3eK43dak3dKY2dKI5gLg4ebA1eq83d6s3caI8aaU5e7M3eK42eKs4cJsAgIA4eK85d7A2dqs2dKk2dKc3cqR2koD/10v/20k2ebU4ebDRvlz/1UX/00Q4erDbxFf/0UA2eK42aZb/1ET/zz83d6s3cqQ6c6GZpXuprXCpq2y8s2P900X/00M3cKL/3lH/zDs2dKZVg5L/yjk3c6U3caJihoz/yTn/xzg7dp03bpuqqnH/0kP/0kD/0D7/zjz/yzz/wzz//wD/2E7/zj7/yDf/41X/1Ub/zj3/zTz/yjn/yDf/1Ub/00L/0ED/zj3/zDv/yTr/xzg3d6s3dak3dKc3cqQ3caI3cJ82bp03eK42bZr/10c2a5j/1UX/00P/0UE3dKb/zz//zT3/3U7/20z/2Ur/10j/1Ub/zj3/zDv/00T/0D//0kL/1ET///8twZG5AAAAVXRSTlMAVcbw67tCEuhD9/YRG/ukKQIgLYiIiL44MxUm3HX1QKxwwuqzlfj6/oVudnZvhf2fq/aydbYz7njbKQ0zLb13d3ciEQEaoSoJ7vxN4Rw3suj27MNWkzfuJAAAAAFiS0dEca8HXOIAAAAHdElNRQfkBQcLNhpsHcMTAAAAuklEQVQI12NgAAJGJuZQFlY2Bihg5+DkCguP4OaB8nn5+IHcyCgBME9QSFhEVEw8MipaQlKKgUFaJiYULBsdKxsnJ8+gAOfGKyYkKjEow7kqqolJagzqYckamlraOjq6evpJKakMLMkRBoZp6RmZWYlArhGDcUSkCYybnWPKYGYeZQHi5iblZedYWjEwWNvYArl29g6OTs4uYBe5AmXz89yM3KHu9fAsyM/z8vbxhXnIzz8gMCg4BMQEAKy7MbtksegJAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA1LTA3VDExOjU0OjI2KzAwOjAw1j8VsQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wNS0wN1QxMTo1NDoyNiswMDowMKdirQ0AAAAASUVORK5CYII="></a></p>

<p align="center"><a href="../../releases/"><img src="https://img.shields.io/github/v/release/kubinka0505/iFunny-Captions?style=for-the-badge"></a>　<a href="../../commit/"><img src="https://img.shields.io/github/last-commit/kubinka0505/iFunny-Captions?style=for-the-badge"></a></p>

<p align="center"><a href="../../issues/"><img src="https://img.shields.io/github/issues/kubinka0505/iFunny-Captions?style=for-the-badge"></a>　<a href="https://www.gnu.org/licenses/gpl-3.0.txt"><img src="https://img.shields.io/badge/license-GPL%20V3-red?style=for-the-badge"></a></p>

<p align="center"><img src="https://img.shields.io/github/languages/code-size/kubinka0505/iFunny-Captions?style=for-the-badge"></p>

## Description 🖥️
I was very unsatisfied that there was only a mobile app for those captions, so I've decided to create one for the PC.

## Completed & Planned Features 🧑‍💻
- [x] Completed
- [ ] In Development
---
- [x] PNG Captions
- [x] GIF Captions
- [x] Offline support¹
- [x] `Giphy` URL support²
- [x] `Tenor` URL support²
- [x] Optimization
- [x] GIF size reduction
- [x] Transparent GIF support
- [ ] [Program Showcase]()
- [ ] Get smaller FFmpeg build
- [ ] GUI Version

¹ - **If You are on Windows, You need to add two backslashes instead of one in `URL / Path`!**

² - Beta, may not work with some URLs.

## Requirements 📥
- `Python >= 3.5.0`
- `PIL`
- `requests`
- **`FFmpeg >= 4.2.0 static executable binary`** - Since `PIL.ImageSequence.Iterator` messes up the frames colors.
  - [Windows](https://www.videohelp.com/software/ffmpeg/old-versions) (Move `ffmpeg.exe` from `bin` to main folder)
  - [Linux](https://www.johnvansickle.com/ffmpeg/old-releases/)
- `gifsicle >= 1.9.2 static executable binary`
  - [Windows](https://eternallybored.org/misc/gifsicle/releases/) (Move `gifsicle.exe` to main folder)
  - [Linux (Debian)](https://www.lcdf.org/gifsicle/)
---
## Usage 📝

1. Clone the repository.
	```bash
	git clone https://github.com/kubinka0505/iFunny-Captions
	cd iFunny-Captions
	```
2. Move <a href="ReadMe.md#requirements-">the required files</a> to repository folder.
3. Modify the parameters in the `Config.json`:
- `Text` :
  - `Content` : **If Your text will contain `"` or `\`, You will have to configure Your text like in these examples**:
	- `Yea, I've played "Helltaker"`, → `Yea, I've played \"Helltaker\"`
	- `_\| VIP |/_` → `_\\| VIP |/_`
  - `Wrap_Factor` : Text-wrapping factor used to break the words. **Is dependent on `Max_Width`**. (Unstable Formula)¹  **Default is `3`**.
- `Image` :
  - `URL / Path` : **Direct** media URL / Path. **[Can be any Image/Video format that FFmpeg supports](https://en.wikipedia.org/wiki/FFmpeg#Supported_formats)**.
  - `Max_Width` : Maximum single frame width. Height is relatively scaled. **Default is `450`**.¹
- `Font` :
  - `Type` : Defines font style used as a caption text. **Default is `2`**.
	- `1` : `Roboto Black` - Android font.
	- `2` : `Futura Extra Black Condensed Regular` - iOS font.
  - `Size` : Font size in pixels. If the value is `false`, then it's calculated by the following formula: *`Max Width ÷ 10`*. **Default is `false`**.
- `Settings` :
  - `Delay` : Single frame display time. (in milliseconds) **Default is `5`**.
	- If `0` : It shouldn't change its original value.
	- If `1` : Delay (in code) is `2`, but removes every 2nd frame, so it tries to *appear* as the Delay was smaller.
	
	**Doesnt Work when `Optimize` is `false`**!
	
	Inputted `Delay` is increased by `1` in code. Issue is under investigation.
  - `Optimize` : **GIF** file size reduction. (`gifsicle` encoder)
	- `Enable` : **Default is `true`**.
	- `Lossy` : LZW lossy compression value. **Default is `200`**.
	
	Some GIFs *can* result in bigger file size **despite** that they are being "*optimized*".
  - `Dark_Mode` : Changes the colors of the Font to `#141414` and Caption Field to `#404040`.
	- `Enable` : **Default is `false`**.
	- `After_Hour` : Activates after set hour in **24-hour time format**. **Default is `22`**.
  - `FFmpeg_Location` : The FFmpeg static executable binary file location.

  Made in the case when You have it somewhere else on Your computer.

  **If You are on Windows, You need to add two backslashes instead of one in Path!**

  **Default is `""`** - *program* assumes that file is in *its* main folder.
  - `Logs` : **Default is `false`**. Displays:
	- Detailed information about image creation time
4. Open `Run.sh`
...or go to Your command prompt and type the following:
	```bash
	python __init__.py
	```
5. Share Your image from the `Images` directory.

¹ - `Max_Width` and `Wrap_Factor` table:
| If `Max_Width` is | 1000 | 800 | 650 | 450 | 300 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Set `Wrap_Factor` to | 6 | 5 | 4 | 3 | 2 |

## Meta Info ℹ️
### Disclaimer ⚠️
**All versions of this project have been made on:**
- `Windows 7 (64-bit)`
- `Python 3.7.5`

**<a href=../../issues/new>In case of problems create issue</a>**.

---
### Supported GIF services 🗃️

If some doesn't work, copy **direct GIF URL** from the Image in site, or just input / paste its location.
| Tenor | Giphy | Gfycat | ImgFlip | Pinterest | Gifer | GifImage | BestAnimations | Gif-Finder | ReactionGIFs | ReplyGIF |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| [![Tenor](https://cdn.discordapp.com/attachments/267356180064501760/778241233297997844/Tenor_Logo.png)](https://tenor.com/) | [![Giphy](https://cdn.discordapp.com/attachments/267356180064501760/778241495508713482/Giphy_Logo.png)](https://giphy.com/) | [![Gfycat](https://cdn.discordapp.com/attachments/267356180064501760/778241493034336296/Gfycat_Logo.png)](https://gfycat.com/) | [![ImgFlip](https://cdn.discordapp.com/attachments/267356180064501760/778372465599971328/ImgFlip_Logo.png)](https://imgflip.com/) | [![Pinterest](https://cdn.discordapp.com/attachments/267356180064501760/778370594617556992/Pinterest_Logo.png)](https://pinterest.com/) | [![Gifer](https://cdn.discordapp.com/attachments/267356180064501760/779682825481093160/Gifer_Logo.png)](https://gifer.com/) | [![GifImage](https://cdn.discordapp.com/attachments/267356180064501760/779685966767980594/GifImage_Logo.png)](https://gifimage.net/) | [![BestAnimations](https://cdn.discordapp.com/attachments/267356180064501760/779686626737651712/BestAnimations_Logo.png)](http://bestanimations.com/) | [![Gif-Finder](https://cdn.discordapp.com/attachments/267356180064501760/779687456269402132/GifFinder_Logo.png)](https://gif-finder.com/) | [![ReactionGIFs](https://cdn.discordapp.com/attachments/267356180064501760/779688523476631552/ReactionGIFs_Logo.png)](https://www.reactiongifs.us/) | [![ReplyGIF](https://cdn.discordapp.com/attachments/267356180064501760/779689535679627284/ReplyGif_Logo.png)](http://replygif.net/) |
---
### Comparisons 🔢
Fonts and caption field height may differ because of the app version.

- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | kubinka0505's<br>"iFunny-Captions" | 40 seconds<br>514 microseconds | 675 kilobytes<br>(690476 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/779733267691733002/Example_iFOkLfuG.gif) |
  | iFunny's<br>Android App | 29 seconds<br>890 microseconds<br>*+ saving to device* | 1.62 megabytes<br>(1629670 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/778244115133497364/93f3155533a382a505e26251944e55f914e3d3cf1a43ec1d6b46d59a315c61dc_1.gif.gif) |
- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | kubinka0505's<br>"iFunny-Captions" | 9 seconds<br>453 microseconds | 210 kilobytes<br>(214781 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/779736416925253662/Example_PTVwpHws.gif) |
  | iFunny's<br>Android App | 12 seconds<br>900 microseconds<br>*+ saving to device* | 535 kilobytes<br>(535869 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/778263102147526676/08d38a26a9396e35512bda67c85fe9716c5ee11f8ef1bccde0cd6fac0640364a_1.gif.gif) |
---
| Tested With | App Version | Device's Processor |
|:-:|:-:|:-:|
| PC | 2.6 | Intel Core i3-2120 |
| Huawei P10 Lite | 6.15.3 | HiSilicon Kirin 658 |
