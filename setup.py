from setuptools import find_packages,setup
from typing import List


def find_requirements(file_path:str)->list[str]:
    "Reading Requirements.txt file and read line by line"

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]

    return requirements

setup(
    name="credit_cards_inspection",
    author="Anshu Yadav",
    author_email="anshu.yadav.cs23@ggits.net",
    description="Helps bank credit cards feedback",
    version="0.0.1",
    packages=find_packages(),
    install_requires=find_requirements("requirements.txt")
)