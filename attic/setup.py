# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='b2',
    version=version,
    description='Command line client for B2 Cloud Storage',
    long_description=long_description,
    url='https://github.com/e12e/B2_Command_Line_Tool',
    author='Eirik Schwenke',
    author_email='github@s.hypertekst.net',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Archiving :: Backup',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='cloud storage backup',
    packages=find_packages(),
    install_requires=['docopt>=0.6.1'],
    package_data={
        '': ['./VERSION'],
    },
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'b2=b2:main',
        ],
    },
)
