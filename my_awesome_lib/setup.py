# setup.py
from setuptools import setup, find_packages

setup(
    name="my_awesome_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Aleksander Rubacha",
    author_email="aleksander.rubacha@gmail.com",
    description="Biblioteka zawierająca funkcje do przetwarzania tekstów, obliczeń matematycznych i operacji na danych.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xAgaVex/python-intro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.13',
)
