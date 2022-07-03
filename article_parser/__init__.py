from .Extractor import *


def parse(url='', html='', threshold=0.9, output='html', **kwargs):
    r"""Extract article by url or html.

    :param url: URL for the article.
    :param html: Html for the article.
    :param threshold: The ratio of text to the entire document, default 0.9.
    :param output: Result output format, support ``markdown`` and ``html``, default ``html``.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`tuple` object
    """

    ext = Extractor(url=url, html=html, threshold=threshold,
                    output=output, **kwargs)
    return ext.parse()
