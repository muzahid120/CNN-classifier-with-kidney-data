from setuptools import setup,find_packages

from typing import List
def get_requirements(file_path:str) -> List[str]:
    hype_dot= '-e .'


    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', '').strip() for req in requirements]
        if hype_dot in requirements:
            requirements.remove(hype_dot)

    return requirements




setup(
name='CNN_project',
version="0.0.1",
author='Sk Mozahid',
author_email='muzahidsk771@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)





