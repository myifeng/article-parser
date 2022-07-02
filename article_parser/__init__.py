from .Extractor import *


def parse(url='', html='', options={}, **kwargs):
    ext = Extractor(url=url, html=html, options=options, **kwargs)
    return ext.parse()
