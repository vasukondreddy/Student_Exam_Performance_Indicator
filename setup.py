from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' # when -e . is return in requiremnts.txt it aumatically install requiremnets in run from the requiremnts.txt 
# if we execute from setpu.py -e . triggers the requiremtns.txt file 


def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Vasu',
    author_email='vasudevareddykondreddy@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)