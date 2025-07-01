# the packaging setup script

from setuptools import setup, find_packages

setup(
    name='jobstats',
    version='0.1',
    packages=find_packages(),  # this finds your app/ package
)
