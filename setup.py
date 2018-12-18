# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '1.0rc11'
description = 'Pacote de temas do Portal Modelo'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='interlegis.portalmodelo.theme',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='portalmodelo interlegis plone diazo theme',
      author='Programa Interlegis',
      author_email='ti@interlegis.leg.br',
      url='https://github.com/interlegis/interlegis.portalmodelo.theme',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['interlegis', 'interlegis.portalmodelo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.app.theming',
          'plone.theme',
          'Products.GenericSetup',
          'setuptools',
          'zope.component',
          'zope.interface',
          'z3c.jbot',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ],
      },
      entry_points='''
      [z3c.autoinclude.plugin]
      target = plone
      ''',
      )
