# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-contact',
    version='0.9',
    author=u'Edouard Richard',
    author_email='edou4rd@gmail.com',
    url='',
    license='',
    description='Contact page',
    zip_safe=False,
    packages=find_packages(),
    #packages = ['contact', 'contact.templatetags'],
    include_package_data=True,
)



