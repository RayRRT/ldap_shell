"""
Installation script.
"""
from setuptools import find_packages, setup

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='ldap_shell',
    version='0.1.1',
    description='LDAP shell utility from Impacket',
    long_description=readme,
    author='Riocool and saber-nyan',
    author_email='z-Riocool@gmail.com',
    url='https://github.com/PShlyundin/ldap_shell',
    install_requires=[
        'ldap3==2.9.1',
        'ldapdomaindump==0.9.3',
        'pyasn1==0.4.8',
        'pycryptodomex==3.10.1',
        'dsinternals==1.2.4',
        'minikerberos',
        'winsspi',
	'impacket',
	'pyOpenSSL'
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['ldap_shell=ldap_shell.__main__:main', ],
    },
)
