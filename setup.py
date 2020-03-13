# If you need help about packaging, read
# https://python-packaging-user-guide.readthedocs.org/en/latest/distributing.html
#
# To build this package run
# python3 setup.py sdist bdist_wheel
# in this directory.
#
# To install this package in your virtual environment run
#
# cd ..
# pip install -e otrade/
#

import sys
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# now, setup can do his thing...
setuptools.setup(
    name="otrade",
    version="0.0.1",
    entry_points={
        'console_scripts':
        [
            'otrade=otrade.app:run',
            'get_quote=otrade.utils.get_quote:run',
            'get_news=otrade.utils.get_news:run',
            'get_price_direction=otrade.utils.get_price_direction:run'
        ],
    },
    author="Owen",
    install_requires=requirements,
    python_requires='>=3.8.0',
    author_email="owenmcgettrick@gmail.com",
    description="A sample stock analysis package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kinetickode/otrade",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
