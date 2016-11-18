from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = '0.2.3'

setup(
    name='wetransferpy',
    version=version,
    description='WeTransfer command line utility.',
    long_description=long_description,
    author='Sylvain Maziere, Paul Delannoy',
    author_email='sylvain@predat.fr, paul@highwaytv.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords="wetransfer upload download authenticate",
    url='http://github.com/predat/wetransferpy',
    download_url='https://github.com/predat/wetransferpy/tarball/' + version,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        "requests",
        "requests_toolbelt"
    ],
    scripts=['bin/wetransfer-upload','bin/wetransfer-download']
)
