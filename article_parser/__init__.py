from .Extractor import *

def parse(url='', html=''):
    ext = Extractor(url=url, html=html)
    return ext.parse()