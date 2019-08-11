import os
from distutils.core import setup

setup(
    name='phuzzer', version='8.19.4.30.pre2', description="Python wrapper for multiarch AFL",
    packages=['phuzzer', 'phuzzer.extensions', 'phuzzer.phuzzers'],
    install_requires=['angr', 'shellphish-qemu', 'tqdm'],
    dependency_links=['git+https://github.com/derdav3/shellphish-afl#egg=package-1.0']
)
