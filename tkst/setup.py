from os import path
from setuptools import setup

folderPath = path.abspath(path.dirname(__file__))
readme = open(path.join(folderPath, "README.md"), encoding="utf-8").read()

setup(
    name="tkst",
    version="0.1.0",
    description="preview projects using the ST7789 display in a tkinter window",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/mmmsoup/tkst",
    author="mmmsoup",
    author_email="mmmsoup@protonmail.com",
    license="MIT",
    py_modules=["tkst"],
    install_requires=["Pillow"]
)