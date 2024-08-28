from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Mostafa Mohamed Atef",
    description="A package for executing programs, files, websites by using shortcuts.",
    name='aukey',
    packages=find_packages(include=['aukey', 'aukey.*']),
    version='0.1.2',
    install_requires=['keyboard'],
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='aukey',    
    zip_safe=False,
)