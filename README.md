# article-parser

[![size](https://img.shields.io/github/repo-size/myifeng/article-parser)](https://pypi.org/project/article-parser/)
[![python](https://img.shields.io/pypi/pyversions/article-parser)](https://pypi.org/project/article-parser/)
[![pypi](https://img.shields.io/pypi/v/article-parser)](https://pypi.org/project/article-parser/)
[![wheel](https://img.shields.io/pypi/wheel/article-parser)](https://pypi.org/project/article-parser/)
[![license](https://img.shields.io/github/license/myifeng/article-parser)](https://pypi.org/project/article-parser/)


Extract article or news by url or html, parse the title and content, output in markdown format.


## How to install

`article-parser` is available on pypi
https://pypi.org/project/article-parser/

```
$ pip install article-parser
```

## Basic Usage

[Djokovic wins record 36th Masters title in Rome - Chinadaily.com.cn](http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html)

```python
>>> import article_parser
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html")
>>> print(title)
>>> print('----------------')
>>> print(content)


Djokovic wins record 36th Masters title in Rome
----------------
![](http://img2.chinadaily.com.cn/images/202009/22/5f6962b2a31024adbd959228.jpeg)
Serbia's Novak Djokovic kisses the trophy after winning the final against
Argentina's Diego Schwartzman at Italian Open, Foro Italico, Rome, Italy, Sept
21, 2020. [Photo/Agencies]

ROME - Novak Djokovic won a record 36th Masters crown as he beat Diego
Schwartzman in the men's final of the ATP Italian Open on Monday.

Djokovic, the world number one and the top seed at the tournament, won 7-5,
6-3 against Argentine Schwartzman to lift his 36th Masters title, one more
than Rafael Nadal.

The Serb said he did not play his best tennis this time in Rome, but could
find it when needed.

Simona Halep, top seed of the women's draw, won her first title in Rome after
defending champion Karolina Pliskova of the Czech Republic retired while
trailing 6-0, 2-1 in the final.

```
