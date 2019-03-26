from setuptools import setup

setup(name='arduino-python',
      version='0.3',
      install_requires=['pyserial'],
      description="A light-weight Python library that provides a serial \
      bridge for communicating with Arduino microcontroller boards.",
      author='Tristan Hearn',
      author_email='tristanhearn@gmail.com',
      url='https://github.com/thearn/Python-Arduino-Command-API',
      license='Apache 2.0',
      packages=['Arduino'],
      )
