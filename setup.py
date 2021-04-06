from setuptools import setup, find_packages

import codecs
import os
import re
import sys

here = os.path.abspath(os.path.dirname(__file__))


min_requires = [
    "pycarol[dataframe]" 
]

extras_require = {
    # "dataframe": min_requires + ['pandas>=0.23.4,!=1.0.4', 'numpy>=1.16.3', 'joblib>=0.11', 'pyarrow>=0.15.1,<1.0.0',],
    "dev": min_requires + ['pytest', 'bumpversion', "sphinx-rtd-theme", "sphinx"],
}
extras_require["complete"] = sorted(
    {v for req in extras_require.values() for v in req}
)


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

readme_note = """\
.. note::
   For the latest source, discussion, etc, please visit the
   `GitHub repository <https://github.com/jnefoussi/pytechfin>`_\n\n
"""

with open('README.rst') as fobj:
    long_description = readme_note + fobj.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")

setup(
    name='pytechfin',
    setup_requires=["wheel"],
    packages=find_packages(exclude=['docs', 'doc']),
    version=find_version("pytechfin", "__init__.py"),
    license='TOTVS SA',
    description='Techfin Python API and Tools',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='TOTVS SA',
    maintainer='TOTVS SA',
    author_email='ops@totvslabs.com',
    url='https://github.com/jnefoussi/pytechfin',
    keywords=['Totvs', 'Carol.ai', 'totvs techfin'],
    install_requires=min_requires,
    extras_require=extras_require,
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 5 - Production/Stable',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
    ],
)
