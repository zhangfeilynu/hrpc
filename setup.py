# coding=utf-8

from setuptools import setup, find_packages
from pip.req import parse_requirements


# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
reqs = [str(ir.req) for ir in install_reqs if ir.req]

setup(
    name='hrpc',
    version='1.0.3',
    keywords="hrpc rpc",
    description='A common interface based RPC framework',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    license='Apache License 2.0',
    url='https://github.com/AirtestProject/hrpc',
)
