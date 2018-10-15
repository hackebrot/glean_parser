#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Michael Droettboom",
    author_email='mdroettboom@mozilla.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description="Parser tools for Mozilla's glean telemetry",
    entry_points={
        'console_scripts': [
            'glean_parser=glean_parser.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='glean_parser',
    name='glean_parser',
    packages=find_packages(include=['glean_parser']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='TODO',
    version='0.1.0',
    zip_safe=False,
)