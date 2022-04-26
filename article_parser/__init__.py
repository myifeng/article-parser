from .Extractor import *

def parse(url='', html='', proxies={}, options={}):
    ext = Extractor(url=url, html=html, proxies=proxies, options=options)
    return ext.parse()