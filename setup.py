# -*- coding: utf-8 -*-
import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

setup(
    name='cd_django_thumbnails',
    version='0.3.6',
    author='Selwin Ong',
    author_email='selwin.ong@gmail.com',
    packages=['thumbnails'],
    url='https://github.com/Leonime/cs_django_thumbnails',
    license='MIT',
    description='A simple Django app to manage image/photo thumbnails. '
                'Supports remote/cloud storage systems like Amazon S3.',
    long_description=README,
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=['django', 'da-vinci', 'shortuuid'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
