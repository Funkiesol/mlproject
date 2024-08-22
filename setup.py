from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    Functions return the list of packages in requirements 
    '''
    requirements = [] 
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements 

setup(
    name='ML Project',
    version = '0.0.1',
    author= 'Gabriel',
    author_email= ' e0775571@u.nus.edu',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)