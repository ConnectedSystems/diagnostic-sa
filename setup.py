from setuptools import setup, find_packages

setup(
    name='diagnostic-sa',
    version='0.0.1',
    url='https://github.com/ConnectedSystems/diagnostic-sa.git',
    author='Takuya Iwanaga',
    author_email='takuyai@gmail.com',
    description='Examples for diagnostic SA paper',
    packages=find_packages(),    
    install_requires=['numpy == 1.18.5'],
)