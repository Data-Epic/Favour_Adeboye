from setuptools import setup, find_packages

setup(
    name='datawrangler', 
    version='0.1', 
    packages=find_packages(),
    install_requires=[
        'pandas',  # Dependencies
    ],
    author='Favour Adeboye',
    author_email='favouradeboye123@gmail.com',
    description='A utility package for data wrangling and manipulation',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
