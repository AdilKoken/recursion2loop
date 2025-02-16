from setuptools import setup, find_packages

setup(
    name="recursion2loop",
    version="0.1.1",
    packages=find_packages(include=["recursion2loop"]),
    description="conversion of recursive functions to iterative implementations. Optimize your Python code by transforming stack-heavy recursion into efficient loops.",
    author='Adil Köken',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)

