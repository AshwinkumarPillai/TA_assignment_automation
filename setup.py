from setuptools import setup, find_packages

setup(
    name='ta_assignment_automation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    license="MIT",
    author='Ashwin Pillai',
    author_email='ashwinkumarpillai1729@gmail.com',
    description='Assign TAs to Classes using a global optimization algorithm',
    url='https://github.com/AshwinkumarPillai/TA_assignment_automation',
)
