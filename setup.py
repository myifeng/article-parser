from os import path as os_path
from setuptools import setup, find_packages

this_directory = os_path.abspath(os_path.dirname(__file__))


def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name="article-parser",
    author="myifeng",
    author_email="myifengs@gmail.com",
    maintainer="myifeng",
    maintainer_email="myifengs@gmail.com",
    keywords="article news html parser extractor",
    description="A parser to parse article from url or html",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/myifeng/article-parser",
    packages=find_packages(exclude=['.github', 'test']),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation",
    ],
    python_requires='>=3.7',
    version_config={
        "template": "{tag}",
        "dirty_template": "{tag}",
        "dev_template": "{tag}"
    },
    setup_requires=["setuptools-git-versioning"]
)
