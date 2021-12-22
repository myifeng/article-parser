# article-parser

![GitHub Repo stars](https://img.shields.io/github/stars/myifeng/article-parser)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/myifeng/article-parser/CI)
[![python](https://img.shields.io/pypi/pyversions/article-parser)](https://pypi.org/project/article-parser/)
[![pypi](https://img.shields.io/pypi/v/article-parser)](https://pypi.org/project/article-parser/)
[![wheel](https://img.shields.io/pypi/wheel/article-parser)](https://pypi.org/project/article-parser/)
[![license](https://img.shields.io/github/license/myifeng/article-parser)](https://pypi.org/project/article-parser/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/article-parser)


Extract article or news by url or html, parse the title and content, output in markdown format.


## How to install

`article-parser` is available on pypi
https://pypi.org/project/article-parser/

```
$ pip install article-parser
```

## Basic Usage

```python
>>> import article_parser

article_parser.parse(
  url='',               # The URL of the article. optional
  html='',              # The HTML of the article. optional
  options={
    'markdown': True,   # Output in markdown format. defult True. optional
    'threshold': 0.9,   # Content ratio threshold. defult 0.9. optional
    'timeout': 5        # Request webpage timeout time, in seconds, default 5. optional
  })

## ouput html
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html")

## output markdown
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html", options={'markdown': False})
```

## Example
[Djokovic wins record 36th Masters title in Rome - Chinadaily.com.cn](http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html)


* Markdown

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


* HTML
```python
>>> import article_parser
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html", options={'markdown': False})
>>> print(title)
>>> print('----------------')
>>> print(content)

Djokovic wins record 36th Masters title in Rome
----------------
<div id="Content">

<figure class="image" style="display: table;">
<img data-from="newsroom" id="img-5f6962b2a31024adbd959228" src="//img2.chinadaily.com.cn/images/202009/22/5f6962b2a31024adbd959228.jpeg"/>
<figcaption style="font-size: 14px; display: table-caption; caption-side: bottom;">
   Serbia's Novak Djokovic kisses the trophy after winning the final against Argentina's Diego Schwartzman at Italian Open, Foro Italico, Rome, Italy, Sept 21, 2020. [Photo/Agencies]
 </figcaption>
</figure>
<p dir="ltr">ROME - Novak Djokovic won a record 36th Masters crown as he beat Diego Schwartzman in the men's final of the ATP Italian Open on Monday.</p>
<p dir="ltr">Djokovic, the world number one and the top seed at the tournament, won 7-5, 6-3 against Argentine Schwartzman to lift his 36th Masters title, one more than Rafael Nadal.</p>
<p dir="ltr">The Serb said he did not play his best tennis this time in Rome, but could find it when needed.</p>
<p dir="ltr">Simona Halep, top seed of the women's draw, won her first title in Rome after defending champion Karolina Pliskova of the Czech Republic retired while trailing 6-0, 2-1 in the final.</p>
</div>
```
## Contributors

[![All contributions](https://contrib.rocks/image?repo=myifeng/article-parser)](https://github.com/myifeng/mybatis-operation-log/graphs/contributors)