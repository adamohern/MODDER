#python

from distutils.core import setup

setup(
    name='Sky',
    version='0.1.0',
    author='Adam',
    author_email='adam@mechanicalcolor.com',
    packages=['sky', 'get'],
    license='LICENSE.txt',
    description='Framework for easy MODO scripting.',
    long_description=open('README.txt').read()
)

def marco():
	return "polo!"