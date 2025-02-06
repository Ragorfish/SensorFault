from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.read().splitlines()

setup(
    name='Fault Detection',
    author='Mohit Singh Sisodia',
    author_email='Mohitsisodia.2000.10@gmail.com',
    version='0.1',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt'),
    include_package_data=True,

)