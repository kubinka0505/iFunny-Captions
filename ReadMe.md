<a href="https://ifunny.co/"><img src="https://cdn.discordapp.com/attachments/312993895887929355/714526409468412004/iFunny_Captions.png"></img></a>
<center> *Made With* <a href="https://www.python.org/downloads/release/python-375/"><img alt="Python 3.7.5" src="https://img.shields.io/badge/Python-3.7.5-brightgreen?style=for-the-badge&link=https://www.python.org/&https://www.python.org/downloads/&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAMAAAAMCGV4AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABVlBMVEUAAAA5e7Q3ebA3eK43dak3dKY2dKI5gLg4ebA1eq83d6s3caI8aaU5e7M3eK42eKs4cJsAgIA4eK85d7A2dqs2dKk2dKc3cqR2koD/10v/20k2ebU4ebDRvlz/1UX/00Q4erDbxFf/0UA2eK42aZb/1ET/zz83d6s3cqQ6c6GZpXuprXCpq2y8s2P900X/00M3cKL/3lH/zDs2dKZVg5L/yjk3c6U3caJihoz/yTn/xzg7dp03bpuqqnH/0kP/0kD/0D7/zjz/yzz/wzz//wD/2E7/zj7/yDf/41X/1Ub/zj3/zTz/yjn/yDf/1Ub/00L/0ED/zj3/zDv/yTr/xzg3d6s3dak3dKc3cqQ3caI3cJ82bp03eK42bZr/10c2a5j/1UX/00P/0UE3dKb/zz//zT3/3U7/20z/2Ur/10j/1Ub/zj3/zDv/00T/0D//0kL/1ET///8twZG5AAAAVXRSTlMAVcbw67tCEuhD9/YRG/ukKQIgLYiIiL44MxUm3HX1QKxwwuqzlfj6/oVudnZvhf2fq/aydbYz7njbKQ0zLb13d3ciEQEaoSoJ7vxN4Rw3suj27MNWkzfuJAAAAAFiS0dEca8HXOIAAAAHdElNRQfkBQcLNhpsHcMTAAAAuklEQVQI12NgAAJGJuZQFlY2Bihg5+DkCguP4OaB8nn5+IHcyCgBME9QSFhEVEw8MipaQlKKgUFaJiYULBsdKxsnJ8+gAOfGKyYkKjEow7kqqolJagzqYckamlraOjq6evpJKakMLMkRBoZp6RmZWYlArhGDcUSkCYybnWPKYGYeZQHi5iblZedYWjEwWNvYArl29g6OTs4uYBe5AmXz89yM3KHu9fAsyM/z8vbxhXnIzz8gMCg4BMQEAKy7MbtksegJAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA1LTA3VDExOjU0OjI2KzAwOjAw1j8VsQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wNS0wN1QxMTo1NDoyNiswMDowMKdirQ0AAAAASUVORK5CYII="></center></a>

## Description 🖥️
I was very unsatisfied that there was only a mobile app caption tool so I've decided to create one.

## Completed & Planned Features 🧑‍💻
- [x] Completed
- [ ] In Development
---
- [x] PNG Captions
- [x] GIF Captions
- [x] Offline support＊
- [x] `Giphy` URLs support＊＊
- [x] `Tenor` URLs support＊＊
- [x] Optimization
- [x] GIF size reduction
- [ ] Transparent GIF support
- [ ] [Program Showcase]()

＊ - **If You are on Windows, you need to add two backslashes instead of one in Path**!
＊＊ - Beta, may not work with some URLs 

## Requirements 📥
- `Python >= 3.5.0` +
- `PIL`
- `requests`
- **`ffmpeg >= 4.0.0`** * static executable binary*
  - [Windows](https://www.videohelp.com/software/ffmpeg/old-versions "Windows") (Move `ffmpeg.exe` from `bin` to main folder)
  - [Linux](https://www.johnvansickle.com/ffmpeg/old-releases/)
- `gifsicle >= 1.9.2` *static executable binary*
  - [Windows](https://eternallybored.org/misc/gifsicle/releases/ "Windows") (Move `gifsicle.exe` to main folder)
  - [Linux](https://www.lcdf.org/gifsicle/ "Linux")

## Usage 📝
1. Modify the parameters in the `Config.json`:
- `Image` :
  - `URL` : **Direct** media URL. **[Can be any Image/Video format that `ffmpeg` supports](https://en.wikipedia.org/wiki/FFmpeg#Supported_formats "Supported ffmpeg formats")**.
  - `Max_Width` : Maximum single frame width. Height is relatively scaled. *Formula: Max Width ÷ 10*. **Default is 300**.
  - `Crop` : Crops transparent pixels around the **every frame**. **Default is `false`**.
- `Font` :
  - `Type` : Defines font style used as caption text. **Default is `2`**.
    - `1` : `Roboto Black` Android font. (otf)
    - `2` : `Futura Condensed Extra Bold` (otf)
    - `3` : `Futura BT Pro Condensed Extra Black` iOS font. (ttf)＊
  - `Size` : Font size in pixels. If value is `false`, then it's calculated by the formula given in the `Max Value`. **Default is `false`**.
- `Settings` :
  - `Delay` : Single frame display time (in milliseconds). **Default is 12**.
  - `Saving_Method` : Image saving methods that *can* optimize its size. **Default is `1`**. **Doesn't support transparency**. <h style="font-size: 10px;">yet</h>
    - `1` : `PIL`
    - `2` : `ffmpeg`
  - `Optimize` : Reduces GIF size by the `gifsicle` encoder.
  - `Logs` : **Default is `false`**. Displays:
    - Image creation time
- `Text` : Image caption text.
- `Wrap_Factor` : Text-wrapping factor, used to break the words. **Is dependent of `Max_Width`**. (Unknown Formula) **Default is 2**.
2. Open `Run.sh`
3. ...or go to Your command prompt and type following:
	```bash
	git clone https://github.com/kubinka0505/iFunny-Captions
	cd iFunny-Captions
	python __init__.py
	```
4. Share Your image from `Captions` directory.

＊ - TrueType fonts (ttf) are poorly resized and will look bad on small images.