from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Bedrock helpers temporary package'
LONG_DESCRIPTION = 'Temporary package for speeding development'

setup(
    name="aws_helpers", 
    version=VERSION,
    author="",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'aws bedrock'],
    classifiers= []
)