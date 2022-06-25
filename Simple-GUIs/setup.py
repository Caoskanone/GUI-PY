import setuptools

VERSION = '0.1'
DESCRIPTION = 'Libary to make in Python simple GUIs.'
LONG_DESCRIPTION = 'Coming Soon'

# Setting up
setuptools.setup(
    name="Simple-UIs",
    version=VERSION,
    author="Caoskanone",
    author_email="caoskanone.dev@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages(),
    keywords=['python'],
    classifiers=[
       "Operating System :: Unix",
       "Operating System :: MacOS :: MacOS X",
       "Operating System :: Microsoft :: Windows",
       "License :: OSI Approved :: MIT License",
       "Programming Language :: Python :: 3",
    ]
)