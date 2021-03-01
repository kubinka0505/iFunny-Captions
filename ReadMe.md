<a href="https://ifunny.co/"><img style="width: 75%; display: block; margin-left: auto; margin-right: auto" src="https://cdn.discordapp.com/attachments/312993895887929355/714526409468412004/iFunny_Captions.png"></img></a>
<center> <a href="https://www.python.org/downloads/release/python-375/"><img alt="Python 3.7.5" src="https://img.shields.io/badge/Python-3.7.5-brightgreen?style=for-the-badge&link=https://www.python.org/&https://www.python.org/downloads/&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAMAAAAMCGV4AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABVlBMVEUAAAA5e7Q3ebA3eK43dak3dKY2dKI5gLg4ebA1eq83d6s3caI8aaU5e7M3eK42eKs4cJsAgIA4eK85d7A2dqs2dKk2dKc3cqR2koD/10v/20k2ebU4ebDRvlz/1UX/00Q4erDbxFf/0UA2eK42aZb/1ET/zz83d6s3cqQ6c6GZpXuprXCpq2y8s2P900X/00M3cKL/3lH/zDs2dKZVg5L/yjk3c6U3caJihoz/yTn/xzg7dp03bpuqqnH/0kP/0kD/0D7/zjz/yzz/wzz//wD/2E7/zj7/yDf/41X/1Ub/zj3/zTz/yjn/yDf/1Ub/00L/0ED/zj3/zDv/yTr/xzg3d6s3dak3dKc3cqQ3caI3cJ82bp03eK42bZr/10c2a5j/1UX/00P/0UE3dKb/zz//zT3/3U7/20z/2Ur/10j/1Ub/zj3/zDv/00T/0D//0kL/1ET///8twZG5AAAAVXRSTlMAVcbw67tCEuhD9/YRG/ukKQIgLYiIiL44MxUm3HX1QKxwwuqzlfj6/oVudnZvhf2fq/aydbYz7njbKQ0zLb13d3ciEQEaoSoJ7vxN4Rw3suj27MNWkzfuJAAAAAFiS0dEca8HXOIAAAAHdElNRQfkBQcLNhpsHcMTAAAAuklEQVQI12NgAAJGJuZQFlY2Bihg5+DkCguP4OaB8nn5+IHcyCgBME9QSFhEVEw8MipaQlKKgUFaJiYULBsdKxsnJ8+gAOfGKyYkKjEow7kqqolJagzqYckamlraOjq6evpJKakMLMkRBoZp6RmZWYlArhGDcUSkCYybnWPKYGYeZQHi5iblZedYWjEwWNvYArl29g6OTs4uYBe5AmXz89yM3KHu9fAsyM/z8vbxhXnIzz8gMCg4BMQEAKy7MbtksegJAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA1LTA3VDExOjU0OjI2KzAwOjAw1j8VsQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wNS0wN1QxMTo1NDoyNiswMDowMKdirQ0AAAAASUVORK5CYII="></center></a>

## Description
I was very unsatisfied that there was only a mobile app caption tool so I've decided to create one.

## Completed & Planned Features
- [x] Completed
- [ ] In Development
---
- [x] PNG Captions
- [x] GIF Captions
- [ ] Offline support
- [x] <code>Giphy</code> URLs support＊
- [x] <code>Tenor</code> URLs support＊
- [x] Optimization
- [ ] GIF size reduction
- [ ] Transparent GIF support
- [ ] <i>([Showcase])("")</i>

＊ - Beta

## Requirements
- <code>Python 3.5</code> +
- <code>PIL</code>
- <code>requests</code>
- <code>textwrap</code>
- <b><code>ffmpeg.exe >= 4.0.0</code></b> ([Download version based on Your OS, unzip and move <code>ffmpeg.exe</code> from <code>bin</code> to main folder](https://www.videohelp.com/software/ffmpeg/old-versions ""))

## Usage
1. Modify the parameters in the <code>Config.json</code>:
- <code>Image</code> :
  - <code>URL</code> : <b>Direct</b> media URL. Can be any Image/Video format that <code>ffmpeg</code> supports.
  - <code>Max_Width</code> : Maximum single frame width. Height is relatively scaled, same as font size. Formula: <code>Max Width ÷ 10</code>. <b>Default is <code>false</code></b>.
  - <code>Crop</code> : Crops transparent pixels around the <b><u>every frame</u></b>. <b>Default is 300</b>.
- <code>Font</code> :
  - <code>Type</code> : Defines font style used as caption text. <b>Default is <code>2</code></b>.
    - <code>1</code> : <code>Roboto Black</code> (otf)
    - <code>2</code> : <code>Futura Condensed Extra Bold</code> (otf)
    - <code>3</code> : <code>Futura BT Pro Condensed Extra Black</code> (ttf)
- <code>Settings</code> :
  - <code>Speed</code> : Single frame display time. (in milliseconds). <b>Default is 28</b>.
- <code>Text</code> : Image caption text.
- <code>Wrap</code> : Text-wrap, used to break the words. <b>Default is 14</b>.
2. Open <code>Run.sh</code>
3. ...or go to Your command prompt and type following:
	```bash
	git clone https://github.com/kubinka0505/iFunny-Captions
	cd iFunny-Captions
	py __init__.py
	```
4. Share Your image from <code>Captions</code> directory.
