from distutils.core import setup

setup(name='pal',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Read and write palcal files.',
      url='http://dada.pink/pal/',
      packages=['pal'],
      install_requires = [
      ],
      tests_require = [
      ],
      version='0.0.1',
      license='AGPL',
      entry_points = {'console_scripts': ['pypal = pal.cli']},
)
