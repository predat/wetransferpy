from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wetransferpy',
    version='0.1.1',
    description='WeTransfer',
    long_description=long_description,
    url='https://github.com/creemerica/wetransfer-upload',
    author='Sylvain Maziere, Paul Delannoy',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['wetransfer', 'upload','download'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        "requests",
        "requests_toolbelt",
	"lxml"
    ],
    scripts=['bin/wetransfer-upload','bin/wetransfer-download']
)
