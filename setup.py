"""
Enables `pip install` for emnist package
"""

from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='emnist',
      version="1.0", # TO DO: check correct version
      description="EMNIST model handwritten letter recognition",
      # url=
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
