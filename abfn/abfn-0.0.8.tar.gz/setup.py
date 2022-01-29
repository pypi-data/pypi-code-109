import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='abfn',  # should match the package folder
    packages=['abfn'],                   # This is the name of the package
    version="0.0.8",                        # The initial release version
    author="Shubham Randive",                     # Full name of the author
    description="ABFN rules for text filtering",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
         # Directory of the source code of the package
)