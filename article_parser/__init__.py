from .Extractor import *

def parse(url='', html='', options={}):
    ext = Extractor(url=url, html=html, options=options)
    return ext.parse()