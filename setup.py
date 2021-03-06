import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open(f"epyppeteer/__init__.py", "r") as f:
    text = f.read()
    version = text.split('__version__ = "')[1].split('"')[0]
    
def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

setuptools.setup(
    name="epyppeteer",
    version="0.0.5",
    author="DMS",
    author_email="masato190411@gmail.com",
    description="Easy to using pyppeteer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuna2134/easy-pyppeteer",
    install_requires=_requires_from_file('requirements.txt'),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
