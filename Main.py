#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Extractor import Extractor

if __name__ == '__main__':
    extractor = Extractor(url="http://www.dluohe.cn/post/3909.html")
    title, content=extractor.parse()
    print(title)
    print('---------------')
    print(content)