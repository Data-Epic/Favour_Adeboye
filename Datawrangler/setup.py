from setuptools import setup, find_packages

setup(
    name='datawrangler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A utility package for data wrangling and manipulation',
)