from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'OpenLabCluster'
LONG_DESCRIPTION = 'Unsupervised Learning package for labelling actions from keypoints'
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="openlabcluster", 
        version=VERSION,
        author="Jingyuan Li",
        author_email="<jingyli6@uw.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=REQUIREMENTS, # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        entry_points='''
            [console_scripts]
            openlabcluster=openlabcluster:launch_dlc
        ''',
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)