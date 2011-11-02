from setuptools import setup, find_packages
import sys, os

version = '0.3.1'

def read():
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    history = open(os.path.join(os.path.dirname(__file__), 'docs', 'HISTORY.txt')).read()
    return '{0}\n\n{1}'.format(readme, history)

setup(name='mongodoc',
      version=version,
      description="Creates a uml-like diagram for a nested mongodb document",
      long_description=read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mongodb database schema documentation',
      author='Craig Swank',
      author_email='craigswank@gmail.com',
      url='https://github.com/cswank/mongodoc',
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
      mongodoc=mongodoc.scripts:document_db
      """,
      )
