from __future__ import with_statement
import os.path
import setuptools


MISC_DIR = "misc"
REQUIREMENT_DIR = "requirements"

with open("README.rst") as fp:
    long_description = fp.read()

with open(os.path.join(MISC_DIR, "summary.txt")) as f:
    summary = f.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_require = [line.strip() for line in f if line.strip()]

setuptools.setup(
    name="DateTimeRange",
    version="0.2.0",
    author="Tsuyoshi Hombashi",
    author_email="gogogo.vm@gmail.com",
    url="https://github.com/thombashi/DateTimeRange",
    keywords=["datetimerange", "date", "time", "range"],
    license="MIT License",
    description=summary,
    long_description=long_description,
    include_package_data=True,
    install_requires=install_requires,
    packages=setuptools.find_packages(exclude=['test*']),
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
