# -*- coding: utf-8 -*-

import re
import copy
import requests
import html2text
from bs4 import BeautifulSoup, Comment, NavigableString


class Extractor():
    def __init__(self, url, html, threshold, output, **kwargs):
        self.url = url
        self.title = ''
        self.html = html
        self.output = output
        self.threshold = threshold
        self.kwargs = kwargs
        if not self.html:
            self.html = self.__download()

    def __process_text_ratio(self, soup) -> tuple:
        soup = copy.copy(soup)
        if soup:
            if type(soup) is NavigableString:
                return 1
            for t in soup.find_all(['script', 'style', 'noscript', 'a', 'img']):
                t.extract()
            soup_str = re.sub(
                r'\s*[^=\s+]+\s*=\s*([^=>]+)?(?=(\s+|>))', "", str(soup))
            total_len = len(soup_str)
            if total_len:
                tag_len = 0.0
                for tag in re.compile(r'</?\w+[^>]*>|[\s]', re.S).findall(soup_str):
                    tag_len += len(tag)
                return (total_len-tag_len)/total_len, total_len
        return 0, 0

    def __find_article_html(self, soup) -> BeautifulSoup:
        tmp_len = 0
        tmp_tag = None
        tmp_radio = 0.0
        parent_radio = self.__process_text_ratio(soup)[0]
        if not soup:
            return None
        if type(soup) is NavigableString:
            return soup

        for tag in soup.contents:
            if tag == '\n' or not tag.name or tag.name in ['script', 'style', 'noscript', 'a']:
                continue
            # double check
            tag_radio, tag_len = self.__process_text_ratio(tag)
            if tag_len >= tmp_len and tag_radio >= parent_radio:
                tmp_len = tag_len
                tmp_tag = tag
                tmp_radio = tag_radio
        if tmp_radio == 1:
            return soup
        if tmp_radio >= parent_radio and tmp_tag.name != 'p':
            # article radio
            if soup.find_all(re.compile("h[1-6]")) or tmp_radio < self.threshold:
                return self.__find_article_html(tmp_tag)
            return tmp_tag
        else:
            return soup

    def __get_title(self, soup) -> str:
        title = ''
        if soup:
            for t in soup.find_all_previous(re.compile("^h[1-6]")):
                if t.text:
                    title = t.text
                    break

        if not title:
            html = BeautifulSoup(self.html, 'lxml')
            if html.title:
                title = html.title.text.split('_')[0].split('|')[0]

        self.title = re.sub(r'<[\s\S]*?>|[\t\r\f\v]|^\s+|\s+$', "", title)
        return self.title

    def __download(self) -> str:
        response = requests.get(self.url, **self.kwargs)
        response.raise_for_status()
        html = ''
        if response.encoding != 'ISO-8859-1':
            # return response as a unicode string
            html = response.text
        else:
            html = response.content
            if 'charset' not in response.headers.get('content-type'):
                encodings = requests.utils.get_encodings_from_content(
                    response.text)
                if len(encodings) > 0:
                    response.encoding = encodings[0]
                    html = response.text
        return html


    def parse(self) -> tuple:
        soup = BeautifulSoup(self.html, 'lxml').find('body')
        if soup:
            for tag in soup.find_all(style=re.compile('display:\s?none')):
                tag.extract()
            for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
                comment.extract()
            article_html = self.__find_article_html(soup)
            if self.output == 'markdown':
                return self.__get_title(article_html), self.__html_to_md(article_html)
            else:
                return self.__get_title(article_html), article_html
        return '', ''

    def __html_to_md(self, soup) -> str:
        return html2text.html2text(str(soup), baseurl=self.url)
