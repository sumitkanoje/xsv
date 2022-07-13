from setuptools import setup, find_packages
from setuptools_rust import RustBin

setup(
    name="andrews-xsv",
    version="0.13.0",
    author="Andrew Gallant",
    author_email="jamslam@gmail.com",
    maintainer="Sumitkumar Kanoje",
    maintainer_email="sumitkanoje@gmail.com",
    description="A fast CSV command line toolkit written in Rust.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BurntSushi/xsv",
    packages=find_packages(),
    setup_requires=["setuptools", "wheel", "setuptools-rust"],
    rust_extensions=[
        RustBin(
            "xsv",
            args=["--profile", "release-lto"],
        )
    ],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Environment :: MacOS X',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)