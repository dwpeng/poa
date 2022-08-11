import setuptools
from setuptools import setup

__version__ = '0.0.1'

setup(
    name="poa",
    author="dwpeng",
    author_email="1732889554@qq.com",
    url="https://github.com/dwpeng/poa",
    description="A simple partial order alignment implement.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    version=__version__,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=['numpy'],
)
