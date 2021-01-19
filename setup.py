from setuptools import find_packages, setup
from pg_demo import __version__

setup(
    name='pg_demo',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='Demo of CICD in Databricks',
    author=''
)
