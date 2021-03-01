<a href="https://ifunny.co/">![](https://cdn.discordapp.com/attachments/312993895887929355/714526409468412004/iFunny_Captions.png)</a>

<a href="https://www.python.org/downloads/release/python-375/">![](https://img.shields.io/badge/Python-3.7.5-brightgreen?style=for-the-badge&link=https://www.python.org/&https://www.python.org/downloads/&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAMAAAAMCGV4AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABVlBMVEUAAAA5e7Q3ebA3eK43dak3dKY2dKI5gLg4ebA1eq83d6s3caI8aaU5e7M3eK42eKs4cJsAgIA4eK85d7A2dqs2dKk2dKc3cqR2koD/10v/20k2ebU4ebDRvlz/1UX/00Q4erDbxFf/0UA2eK42aZb/1ET/zz83d6s3cqQ6c6GZpXuprXCpq2y8s2P900X/00M3cKL/3lH/zDs2dKZVg5L/yjk3c6U3caJihoz/yTn/xzg7dp03bpuqqnH/0kP/0kD/0D7/zjz/yzz/wzz//wD/2E7/zj7/yDf/41X/1Ub/zj3/zTz/yjn/yDf/1Ub/00L/0ED/zj3/zDv/yTr/xzg3d6s3dak3dKc3cqQ3caI3cJ82bp03eK42bZr/10c2a5j/1UX/00P/0UE3dKb/zz//zT3/3U7/20z/2Ur/10j/1Ub/zj3/zDv/00T/0D//0kL/1ET///8twZG5AAAAVXRSTlMAVcbw67tCEuhD9/YRG/ukKQIgLYiIiL44MxUm3HX1QKxwwuqzlfj6/oVudnZvhf2fq/aydbYz7njbKQ0zLb13d3ciEQEaoSoJ7vxN4Rw3suj27MNWkzfuJAAAAAFiS0dEca8HXOIAAAAHdElNRQfkBQcLNhpsHcMTAAAAuklEQVQI12NgAAJGJuZQFlY2Bihg5+DkCguP4OaB8nn5+IHcyCgBME9QSFhEVEw8MipaQlKKgUFaJiYULBsdKxsnJ8+gAOfGKyYkKjEow7kqqolJagzqYckamlraOjq6evpJKakMLMkRBoZp6RmZWYlArhGDcUSkCYybnWPKYGYeZQHi5iblZedYWjEwWNvYArl29g6OTs4uYBe5AmXz89yM3KHu9fAsyM/z8vbxhXnIzz8gMCg4BMQEAKy7MbtksegJAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA1LTA3VDExOjU0OjI2KzAwOjAw1j8VsQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wNS0wN1QxMTo1NDoyNiswMDowMKdirQ0AAAAASUVORK5CYII=)</a>
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
- [ ] GUI Version <h style="font-size:10px">(do not expect it to appear here fast)</h>

¹ - **If You are on Windows, you need to add two backslashes instead of one in `URL /Path`!**

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
2. Modify the parameters in the `Config.json`:
- `Image` :
  - `URL / Path` : **Direct** media URL / Path. **[Can be any Image/Video format that FFmpeg supports](https://en.wikipedia.org/wiki/FFmpeg#Supported_formats)**.
  - `Max_Width` : Maximum single frame width. Height is relatively scaled. *Formula: `Max Width ÷ 10`*. **Default is `300`**.
- `Font` :
  - `Type` : Defines font style used as a caption text. **Default is `2`**.
    - `1` : `Roboto Black` - Android font.
    - `2` : `Futura Extra Black Condensed Regular` - iOS font.
  - `Size` : Font size in pixels. If the value is `false`, then it's calculated by the formula given in the `Max Value`. **Default is `false`**.
- `Settings` :
  - `Delay` : Single frame display time. (in milliseconds) If `0`, it doesn't change its original value. **Default is `5`**.
  - `Optimize` : GIF file size reduction. (`gifsicle` encoder)
    -  `Factor` : If `0`, Image is not optimized. **Values Range: 0 → 3**. **Default is `3`**.
    -  `Lossy` : LZW lossy compression factor. **Default is `200`**.
  - `FFmpeg_Location` : The FFmpeg static executable binary file location.
  Made in case when You have it somewhere else on Your computer.
  **If You are on Windows, you need to add two backslashes instead of one in Path!**
  **Default is `""`** - *program* assumes that file is in *its* main folder.
  - `Logs` : **Default is `false`**. Displays:
    - Detailed information about image creation time
- `Content` : Image text content.
  - `Text` : **If You are on Windows(?), you need to configure Your text like in these examples**:
    - `"Yea, I've played "Helltaker""`, → `"Yea, I've played \"Helltaker\""`
    - `"_\| VIP |/_"` → `"_\\| VIP |/_"`
  - `Wrap_Factor` : Text-wrapping factor used to break the words. **Is dependent on `Max_Width`**. (Unstable Formula)  **Default is `2`**.
3. Open `Run.sh`
...or go to Your command prompt and type the following:
	```bash
	python __init__.py
	```
4. Share Your image from the `Images` directory.

## Meta Info ℹ️
### Disclaimer ⚠️
**All versions of this project have been made on `Windows 7 (64bit)`.**

**[In case of problems create issue](https://github.com/kubinka0505/iFunny-Captions/issues/new)**.

---
### Supported GIF services 🗃️
| Tenor | Giphy | Gfycat | ImgFlip | Pinterest |
|:-:|:-:|:-:|:-:|:-:|
| [![Tenor](https://cdn.discordapp.com/attachments/267356180064501760/778241233297997844/Tenor_Logo.png)](https://tenor.com/) | [![Giphy](https://cdn.discordapp.com/attachments/267356180064501760/778241495508713482/Giphy_Logo.png)](https://giphy.com/) | [![Gfycat](https://cdn.discordapp.com/attachments/267356180064501760/778241493034336296/Gfycat_Logo.png)](https://gfycat.com/) | [![ImgFlip](https://cdn.discordapp.com/attachments/267356180064501760/778372465599971328/ImgFlip_Logo.png)](https://imgflip.com/) | [![Pinterest](https://cdn.discordapp.com/attachments/267356180064501760/778370594617556992/Pinterest_Logo.png)](https://pinterest.com/)
---
### Comparisons 🔢
Fonts may differ because of the app version.

- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | kubinka0505's<br>"iFunny-Captions" | 36 seconds<br>167 microseconds | 1.89 megabytes<br>(1897331 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/778245797753913424/Example_czhSK3ZQ.gif) |
  | iFunny's<br>Android App | 29 seconds<br>890 microseconds<br>*+ saving to device* | 1.62 megabytes<br>(1629670 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/778244115133497364/93f3155533a382a505e26251944e55f914e3d3cf1a43ec1d6b46d59a315c61dc_1.gif.gif) |
- | Created Using | Creation Time | Size | Preview |
  |:-:|:-:|:-:|:-:|
  | kubinka0505's<br>"iFunny-Captions" | 8 seconds<br>682 microseconds | 531 kilobytes<br>(544414 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/778264489271230494/Example_hjHHdTz3.gif) |
  | iFunny's<br>Android App | 12 seconds<br>900 microseconds<br>*+ saving to device* | 535 kilobytes<br>(535869 bytes) | ![](https://cdn.discordapp.com/attachments/267356180064501760/778263102147526676/08d38a26a9396e35512bda67c85fe9716c5ee11f8ef1bccde0cd6fac0640364a_1.gif.gif) |
---
| Tested With | App Version | Device's Processor |
|:-:|:-:|:-:|
| PC | 2.4 | Intel Core i3-2120 |
| Huawei P10 Lite | 6.15.3 | HiSilicon Kirin 658 |
