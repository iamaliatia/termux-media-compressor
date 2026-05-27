import os
from setuptools import setup, find_packages
# باقي الكود كيفما هو...



from setuptools import setup, find_packages

setup(
    name="termux-media-compressor",
    version="0.1.0",
    author="Ali Atia",
    description="A Python CLI tool to compress images and videos locally inside Termux",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "termux-compress=termux_compressor.compressor:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android",
    ],
)
