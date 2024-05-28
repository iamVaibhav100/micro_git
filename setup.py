from setuptools import setup

setup(name='micro_git',
      version='1.0',
      packages=['micro_git'],
      entry_points={
          'console_scripts': {
              'mgit = micro_git.cli:main'
          }
      }
      )
