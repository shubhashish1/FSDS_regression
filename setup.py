"""
This file we need to convert our folder structures into package so that we can
add and install using pip command
"""

from setuptools import find_packages, setup
from typing import List # This will give us the list of the packages we read from requirements.txt

# We should also allow setup.py to create it's package using requirements.txt,
# So we need to add -e . in requirements.txt to allow that
# Now this -e . is not installable and it only triggers the setup.py
# Sp we need to ignore it while calling the requirements.txt to install packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]: # The file_path will fetch the path of requirements.txt
    requirements = []                              # List[str] will return the list of requirements
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Now while reading requirements.txt we have \n for new line which wee don't need
        # so we can replace it with blank
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



"""
Now we need to create the package name version etc to showcase
"""

setup(
    name="houseprice_end_to_end",
    version = "0.0.1",
    author="shubhashish mishra",
    author_email = "shubhashish.hello@gmail.com",
    install_requires = get_requirements('requirements.txt'), # This will tell us the pre-requisite packages needed
    # to install this one
    packages = find_packages() # This will allow us to fetch all subpackages or folders created in project

)