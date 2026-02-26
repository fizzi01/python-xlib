# Distutils script for python-xlib

from packaging.requirements import Requirement
from packaging.version import Version
from setuptools import (__version__ as setuptools_version, setup)


# Check setuptools is recent enough to support `setup.cfg`.
setuptools_require = Requirement('setuptools>=30.3.0')
assert setuptools_require.specifier.contains(Version(setuptools_version)), '{} is required'.format(setuptools_require)


setup(
    install_requires=['six>=1.10.0'],
    setup_requires=['setuptools-scm'],
    packages=[
        'Xlib',
        'Xlib.ext',
        'Xlib.keysymdef',
        'Xlib.protocol',
        'Xlib.support',
        'Xlib.xobject'
    ],
)
