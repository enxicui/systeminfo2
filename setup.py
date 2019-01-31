from setuptools import setup


setup(name="systeminfo",
      version="0.1",
      description="Basic system information or COMP30670",
      url="",
      author="enxi cui",
      author_email="enxi.cui@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']})
