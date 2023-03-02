from setuptools import find_packages, setup
from typing import List

requirement_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."


def get_requirements() -> List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)

    return requirement_list


setup(name='Insurance_Premium',
      version='0.0.1',
      description='Insurance Industry level project',
      author='Vamshi Munukuntla',
      author_email='vamshi.kumar59@gmail.com',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requirements=get_requirements()
      )
