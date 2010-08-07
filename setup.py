from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nxt-turtle',
      version=version,
      description="A Logo-like interface to the Lego NXT robot, written in Python.",
      long_description="""\
A Logo-like interface to the Lego NXT robot, written in Python.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='robotics lego nxt turtle logo',
      author='Sarah Mount',
      author_email='s.mount@wlv.ac.uk',
      url='http://snim2.org',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
