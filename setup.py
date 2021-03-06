# coding=utf-8
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup

setup(
    name='OSlash',
    version='0.5.1',
    description="Ø for Python 3.5",
    long_description=("is a functional library for playing with "
                      "Functors, Applicatives, and Monads in Python."),
    author='Dag Brattli',
    author_email='dag@brattli.net',
    license='Apache License',
    url='https://github.com/dbrattli/oslash',
    download_url='https://github.com/dbrattli/oslash',
    zip_safe=True,
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

    packages=['oslash', 'oslash.util', 'oslash.abc'],
    package_dir={'oslash': 'oslash'}
)
