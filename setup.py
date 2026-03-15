from setuptools import setup, find_packages 
from typing import List

def find_reuirements(filepath:str)-> List: 
    """
    This function is responsible for read the dependencies and return the list of files.
    """ 
    requirements = []
    with open (filepath,'r') as file:
        requirements = file.readline() 
        requirements=[req.replace('\n','') for req in requirements]
    return requirements 

setup (
    name='Pankaj Mishra',
    version='0.0.1',
    author_email='pankajmishra817395@gmail.com',
    packages=find_packages(),
    install_requires=find_reuirements('requirements.txt')
)