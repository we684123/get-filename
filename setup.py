from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_filename",
    version="0.0.1",
    keywords=("filename", "extension"),
    description="from a filename(str) extension or name",
    long_description=long_description,
    license="MIT",
    url="https://github.com/we684123/get_filename",
    author="we684123",
    author_email="we684123@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)
