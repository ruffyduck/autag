from setuptools import setup

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="autag",
    version="0.1.0",
    description="Music file tagging library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ruffyduck",
    author_email="",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=[
        "autag",
        "autag.controller",
        "autag.io",
        "autag.model",
    ],
    include_package_data=True,
    install_requires=[
        "mutagen",
        "discogs_client"
    ]
)