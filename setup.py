import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

setuptools.setup(
    name="epyppeteer",
    version="2.0.5a",
    author="DMS",
    author_email="masato190411@gmail.com",
    description="This is for google custom search api.",
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
