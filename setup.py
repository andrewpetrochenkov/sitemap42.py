import setuptools

setuptools.setup(
    name='sitemap42',
    version='2021.1.17',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
