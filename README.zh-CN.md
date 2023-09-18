# article-parser

![GitHub Repo stars](https://img.shields.io/github/stars/myifeng/article-parser)
[![python](https://img.shields.io/pypi/pyversions/article-parser)](https://pypi.org/project/article-parser/)
[![pypi](https://img.shields.io/pypi/v/article-parser)](https://pypi.org/project/article-parser/)
[![wheel](https://img.shields.io/pypi/wheel/article-parser)](https://pypi.org/project/article-parser/)
[![license](https://img.shields.io/github/license/myifeng/article-parser)](https://pypi.org/project/article-parser/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/article-parser)


**一种通过任意URL或者html文件解析网页的标题和正文的通用库**

*[English]([README.md](https://github.com/myifeng/article-parser/blob/master/README.md))  ∙ [简体中文]([README.zh-CN.md](https://github.com/myifeng/article-parser/blob/master/README.zh-CN.md))*

## 安装

[`article-parser`](https://pypi.org/project/article-parser/) 可以在[`Pipy`](https://pypi.org/project/article-parser/)中下载使用

```
$ pip install article-parser
```

## 使用

```python
>>> import article_parser

article_parser.parse(
  url='',               # 网页的地址.
  html='',              # Html文件内容
  threshold=0.9,        # 阈值，默认0.9
  output='html',        # 输出格式，支持 markdown 和 html, 默认html
  **kwargs              # 可选参数
  ),
  

## 输出markdown格式
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html", output='markdown', timeout=5)

## 输出html格式
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html", timeout=5)

```

## 示例
[Djokovic wins record 36th Masters title in Rome - Chinadaily.com.cn](http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html)


* Markdown

```python
>>> import article_parser
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html", output='markdown', timeout=5)
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
>>> title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html", timeout=5)
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

[![All contributions](https://contrib.rocks/image?repo=myifeng/article-parser)](https://github.com/myifeng/article-parser/graphs/contributors)
