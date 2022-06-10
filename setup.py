"""Setup File"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Package meta-data.
NAME = 'bmiCalculator'
DESCRIPTION = 'bmiCalculator is a tool to calculate BMI'
URL = ''
EMAIL = 'girish.hotchandani@outlook.com'
AUTHOR = 'Girish'
REQUIRES_PYTHON = '>=3.7.0'


setuptools.setup(
    name=NAME,
    version="0.0.1dev",
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    python_requires=REQUIRES_PYTHON,
    entry_points={'console_scripts': ['bmiCalculator = bmiCalculator.__main__:main']}
)
