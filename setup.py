"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bigquery-sqlalchemy-tutorial',
    version='1.0.0',
    description='ETL script to migrate data from BigQuery to SQL.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/bigquery-sqlalchemy-tutorial',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='SQLAlchemy GCP Google BigQuery SQL ETL RDBMS',
    packages=find_packages(),
    install_requires=['SQLAlchemy',
                      'PyBigQuery',
                      'PyMySQL',
                      'Loguru'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'install = main:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/bigquery-sqlalchemy-tutorial/issues',
        'Source': 'https://github.com/hackersandslackers/bigquery-sqlalchemy-tutorial/',
    },
)
