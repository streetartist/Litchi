from setuptools import setup
from os import path
DIR = path.dirname(path.abspath(__file__))
INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()
with open(path.join(DIR, 'README.md')) as f:
 README = f.read()
setup(
 name='litchi_web',
 packages=['litchi'],
 description="Build website with only Python",
 long_description=README,
 long_description_content_type='text/markdown',
 install_requires=INSTALL_PACKAGES,
 version='0.2.4',
 url='http://github.com/streetartist/Litchi',
 author='Streetartist',
 author_email='15252635839@163.com',
 keywords=['web', 'framework', 'flask'],
 tests_require=[
 'pytest',
 'pytest-cov',
 'pytest-sugar'
 ],
 python_requires='>=3'
)
