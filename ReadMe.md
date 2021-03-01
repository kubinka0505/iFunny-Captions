<a href="https://ifunny.co/"><img style="width: 75%; display: block; margin-left: auto; margin-right: auto" src="https://cdn.discordapp.com/attachments/312993895887929355/714526409468412004/iFunny_Captions.png"></img></a>
<center> <a href="https://www.python.org/downloads/release/python-375/"><img alt="Python 3.7.5" src="https://img.shields.io/badge/Python-3.7.5-brightgreen?style=for-the-badge&link=https://www.python.org/&https://www.python.org/downloads/&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAMAAAAMCGV4AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABVlBMVEUAAAA5e7Q3ebA3eK43dak3dKY2dKI5gLg4ebA1eq83d6s3caI8aaU5e7M3eK42eKs4cJsAgIA4eK85d7A2dqs2dKk2dKc3cqR2koD/10v/20k2ebU4ebDRvlz/1UX/00Q4erDbxFf/0UA2eK42aZb/1ET/zz83d6s3cqQ6c6GZpXuprXCpq2y8s2P900X/00M3cKL/3lH/zDs2dKZVg5L/yjk3c6U3caJihoz/yTn/xzg7dp03bpuqqnH/0kP/0kD/0D7/zjz/yzz/wzz//wD/2E7/zj7/yDf/41X/1Ub/zj3/zTz/yjn/yDf/1Ub/00L/0ED/zj3/zDv/yTr/xzg3d6s3dak3dKc3cqQ3caI3cJ82bp03eK42bZr/10c2a5j/1UX/00P/0UE3dKb/zz//zT3/3U7/20z/2Ur/10j/1Ub/zj3/zDv/00T/0D//0kL/1ET///8twZG5AAAAVXRSTlMAVcbw67tCEuhD9/YRG/ukKQIgLYiIiL44MxUm3HX1QKxwwuqzlfj6/oVudnZvhf2fq/aydbYz7njbKQ0zLb13d3ciEQEaoSoJ7vxN4Rw3suj27MNWkzfuJAAAAAFiS0dEca8HXOIAAAAHdElNRQfkBQcLNhpsHcMTAAAAuklEQVQI12NgAAJGJuZQFlY2Bihg5+DkCguP4OaB8nn5+IHcyCgBME9QSFhEVEw8MipaQlKKgUFaJiYULBsdKxsnJ8+gAOfGKyYkKjEow7kqqolJagzqYckamlraOjq6evpJKakMLMkRBoZp6RmZWYlArhGDcUSkCYybnWPKYGYeZQHi5iblZedYWjEwWNvYArl29g6OTs4uYBe5AmXz89yM3KHu9fAsyM/z8vbxhXnIzz8gMCg4BMQEAKy7MbtksegJAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA1LTA3VDExOjU0OjI2KzAwOjAw1j8VsQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wNS0wN1QxMTo1NDoyNiswMDowMKdirQ0AAAAASUVORK5CYII="></center></a>

## Description
I was very unsatisfied that there was only a mobile app caption tool so I've decided to create one.

## Completed & Planned Features
- [x] Completed
- [ ] In Development
---
- [x] PNG Captions
- [ ] GIF Captions＊

###### ＊<i>Will require a complete rewrite</i>

## Requirements
- <code>Python 3.5</code> +
- <code>PIL</code>
- <code>numpy</code>
- <code>requests</code>
- <code>textwrap</code>

## Usage
1. Modify the parameters in the <code>Config.json</code>:
  - <code>URL</code> : <b>Direct</b> Image URL. <b style="color:red">Cannot be in animated format like <code>GIF</code> / <code>APNG</code></b>.
    - Example: <code>https://iso.500px.com/wp-content/uploads/2016/03/stock-photo-142984111.jpg</code>
  - <code>Font</code> : Font Configuration
    - <code>Type</code> : Defines font style used as caption text.
        - <code>1</code> : <code>Roboto Black</code>
        - <code>2</code> : <code>Limerick Limerick Serial X-Bold Regular</code>
	- <code>Size</code> : Font size in pixels. <b>Default is <code>72</code></b>.
  - <code>Text</code> : Image caption text.
  - <code>Wrap</code> : Text-wrap used to break the words. <b>Default is <code>12</code></b>.
2. Open <code>＿init＿.py</code>
3. Go to Your command prompt and type following:
	```bash
	git clone https://github.com/kubinka0505/iFunny-Captions
	cd iFunny-Captions
	py __init__.py
	```
4. Share Your image from <code>Captions</code> directory.
