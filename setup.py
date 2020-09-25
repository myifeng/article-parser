from os import path as os_path
import setuptools

this_directory = os_path.abspath(os_path.dirname(__file__))

def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setuptools.setup(
    name="article-parser",
    version="0.0.4",
    author="myifeng",
    author_email="myifengs@gmail.com",
    keywords = 'article news html parser extractor', 
    description="parser what article and news from url or html",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/myifeng/article-parser",
    packages=[str('article_parser')],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)