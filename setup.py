from setuptools import setup, find_packages

setup(
    name='DistribuitedMapReduce',
    version='1.0',
    author='Amanda Gomez Gomez & Oussama El Azizi',
    author_email='amanda.gomez@estudiants.urv.cat, oussama.elazizi@estudiants.urv.cat',
    packages=find_packages(),
    url='https://github.com/pedrotgn/pyactor',
    description='Distributed map reduce using pyactor middleware',
    long_description=open('README.rst').read(),
    install_requires=['pyactor==1.4.0'],
)
