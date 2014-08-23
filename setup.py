from setuptools import setup, find_packages
import sys, os

setup(name='wa',
      version=':versiontools:wa:',
      description="wa is a flask-based web site develop solution.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='flask, plugins',
      author='LaiYonghao',
      author_email='mail@laiyonghao.com',
      url='https://github.com/laiyonghao/wa',
      license='mit',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      setup_requires=[
          'versiontools>=1.8',
          ],
      install_requires=[
          # -*- Extra requirements: -*-
          'abu.admin',
          'MySQL-python',

          'Flask',
          'Flask-User',
          'Flask-Cache',
          'Flask-CDN',
          'Flask-SQLAlchemy',
          'Flask-Uploads',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [abu.admin]
      wa = wa.admin:Admin
      [wa.entry]
      wa_admin=wa.entry.admin:EntryImpl
      """,
      )
