from setuptools import setup, find_packages

setup(
    name='datawrangler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'os'
    ],
    description='A package for robust data wrangling operations using Pandas',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    author='Favour Adeboye',
    author_email='adeboyefavour654@gmail.com',
    url='https://github.com/Data-Epic/Favour_Adeboye/tree/Datawrangler/Datawrangler', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)