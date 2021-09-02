"""
Installation script.
"""
from setuptools import find_packages, setup

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='ldap_shell',
    version='0.0.1',
    description='LDAP shell utility from Impacket',
    long_description=readme,
    author='saber-nyan',
    author_email='saber-nyan@ya.ru',
    url='https://gitlab.bss-b.local/pentest-tools/ldap-shell',
    install_requires=[
        'ldap3==2.9.1',
        'ldapdomaindump==0.9.3',
        'pyasn1==0.4.8',
        'pycryptodomex==3.10.1',
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['ldap_shell=ldap_shell.__main__:main', ],
    },
)