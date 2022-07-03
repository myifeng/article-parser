import sys
sys.path.append("..")

import article_parser

def test_markdown():
    title, content = article_parser.parse(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html", output='markdown', timeout=5)
    
    assert title == 'Djokovic wins record 36th Masters title in Rome'
    assert content == '''![](http://img2.chinadaily.com.cn/images/202009/22/5f6962b2a31024adbd959228.jpeg)
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

'''