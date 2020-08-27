import os
import re

from setuptools import setup, find_packages


def read_meta():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'TEMPLATE/__init__.py')
    with open(path) as fh:
        hits = re.findall(r'__(\w+)__ ?= ?["\'](.+)["\']\n', fh.read())
    return {k: v for k, v in hits}


def readme():
    with open('README.md') as f:
        return f.read()


meta = read_meta()
setup(name=meta['title'],
      version=meta['version'],
      description=meta['description'],
      long_description=readme(),
      long_description_content_type='text/markdown',
      author=meta['author'],
      author_email=meta['author_email'],
      url=meta['url'],
      license=meta['license'],
      project_urls={
          "Bug Tracker": "https://github.com/aaronmussig/TEMPLATE/issues",
          "Documentation": "https://github.com/aaronmussig/TEMPLATE",
          "Source Code": "https://github.com/aaronmussig/TEMPLATE",
      },
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
      keywords=meta['keywords'],
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'TEMPLATE = TEMPLATE.__main__:main'
          ]
      },
      install_requires=[],
      python_requires='>=3.6',
      data_files=[("", ["LICENSE"])]
      )
