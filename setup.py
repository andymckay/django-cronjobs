from setuptools import setup, find_packages
import os

version = '0.1'
readme = open(os.path.join(os.path.dirname(__file__), "readme.rst"))
long_description = readme.read()

setup(name='django-cronjobs',
      version=version,
      description="Cronjob helper for Django",
      long_description=long_description,
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
