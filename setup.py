import sys

from setuptools import find_packages, setup

LONG_DESCRIPTION = '\n'.join([open('README.rst').read(),
                              open('CHANGES.rst').read()])

_TESTS_REQUIRE = []
if sys.version_info < (3, 3):
    _TESTS_REQUIRE += ['mock']

setup(
    name='django-lockdown',
    version='1.6.0',
    description=('Lock down a Django site or individual views, with '
                 'configurable preview authorization'),
    long_description=LONG_DESCRIPTION,
    author='Carl Meyer',
    author_email='carl@dirtcircle.com',
    maintainer='Daniel Roschka',
    maintainer_email='danielroschka@phoenitydawn.de',
    url='https://github.com/Dunedan/django-lockdown/',
    packages=find_packages(exclude=['lockdown.tests']),
    install_requires=['Django>=1.11'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
    ],
    zip_safe=False,
    tests_require=_TESTS_REQUIRE,
    test_suite='runtests.runtests',
    package_data={'lockdown': ['templates/lockdown/*.html']},
)
