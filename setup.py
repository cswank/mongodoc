from setuptools import setup, find_packages
import sys, os

version = '0.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='mongodoc',
      version=version,
      description="Creates a uml-like diagram for a nested mongodb document",
      long_description=read('README.rst'),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mongodb database documentation',
      author='Craig Swank',
      author_email='craigswank@gmail.com',
      url='',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'pymongo',
          'argparse',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      doc-db=mongodoc.scripts:document_db
      """,
      )
