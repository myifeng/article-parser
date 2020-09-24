#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Extractor import Extractor

if __name__ == '__main__':
    extractor = Extractor(url="http://www.chinadaily.com.cn/a/202009/22/WS5f6962b2a31024ad0ba7afcb.html")
    title, content=extractor.parse()
    print(title)
    print('---------------')
    print(content)