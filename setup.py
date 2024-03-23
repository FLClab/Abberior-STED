
from setuptools import setup, find_packages

setup(
    name='abberior-sted',
    version='0.0.1',
    description="Interface to Imspector control software for Abberior STED microscopes",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    requires_python=">=3.8",
    keywords="abberior sted imspector specpy",
    license="CC-BY-4.0 license",
    install_requires=[
        "scikit-image",
        "numpy",
        "scipy",
        "matplotlib",
        "pyyaml"
    ],  # And any other dependencies foo needs
    packages=["abberior"],
    include_package_data=True,
    project_urls={
        'Documentation': 'https://github.com/FLClab/Abberior-STED',
        'Source': 'https://github.com/FLClab/Abberior-STED',
    },
)
# I do not require specpy to be installed
