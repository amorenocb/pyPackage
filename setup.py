import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # This is the name of the package, its a good idea that this matches the actual package name.
    # So if name = a_name then after installing it, if you list the pip installed packages you would
    # see the package a_name.
    name="a_package_name",
    version="0.0.1",
    author="Juan Andres Moreno",
    author_email="amorenocb@gmail.com",
    description="Example Python package that is pip-instalable.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amorenocb/pyPackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy==1.17.0"],
)
