from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'

def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        [req.replace('/n',"") for req   in requirments]

        if hypen_e_dot in requirments:
            requirments.remove(hypen_e_dot)
    return requirments

setup(
name='mlproject',
version='0.0.1',
author="madhujit",
author_email='madhujitrana@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirments.txt')

)