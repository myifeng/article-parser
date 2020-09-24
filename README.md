# article-parser

Extract article or news by url or html, parse the title and content, output in markdown format.


## Basic Usage

[突尼斯成功拦截一非法移民船只 警方共逮捕17人-国际快讯网](http://www.dluohe.cn/post/3909.html)

```python
extractor = Extractor(url="http://www.dluohe.cn/post/3909.html")
title, content=extractor.parse()
print(title)
print('---------------')
print(content)

突尼斯成功拦截一非法移民船只 警方共逮捕17人
---------------
突尼斯媒体当地时间20日报道，突尼斯海岸警卫队在突尼斯南部沙尔巴岛沿岸成【斯诺登再曝新文件】功拦截了一搜非法移民船只，逮捕了船上的17名犯罪嫌疑人。

![](http://rs1.huanqiucdn.cn/dp/api/images/imageDir/3a437422461f207a431885395083049b.jpg)

突尼斯国防部当天发表声明说，这些非法移民承认他们计划【南航a380航线】从杰尔巴岛偷渡到意大利海岸。当天突尼斯海岸警卫队在事发海域巡逻时，在杰尔巴【特朗普会见安倍】岛以东4英里处发现该可疑船只的非正常活动，并设法将其拦截。声明说，船上的17名嫌疑人均被逮捕，包括16名突尼
斯人和一名来自厄立特里亚的人，年龄在18岁至30岁之间。

AD_SURVEY_Add_AdPos("7004636");

非法移民船于前一天晚上从杰尔巴海岸出发，企图秘密越过海上边界前往意大利海岸。17名犯罪嫌疑人已被带到扎尔兹斯港口，移交给当地国民警卫队以完成必要的法律程序。（总台记者
吴爱民）

```
