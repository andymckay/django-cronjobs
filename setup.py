from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='cronjobs',
      version=version,
      description="Cronjob helper for Django",
      long_description=open("readme.rst").read() + "\n",
      classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        ],
      keywords='',
      packages=['cronjobs'],
      author='Mozilla',
      author_email='andym@mozilla.com',
      url='http://mozilla.com',
      license='BSD',
      zip_safe=True,
      )
