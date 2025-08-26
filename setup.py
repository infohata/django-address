import os
import sys

from setuptools import find_packages, setup

version = "0.3"

if sys.argv[-1] == "tag":
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

setup(
    name="django-address",
    version=version,
    author="Luke Hodkinson",
    author_email="furious.luke@gmail.com",
    maintainer="Kestutis Januskevicius",
    maintainer_email="infohata@gmail.com",
    url="https://github.com/infohata/django-address",
    description="A django application for describing addresses.",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.txt", "*.js", "*.html", "*.*"]},
    install_requires=["setuptools"],
    zip_safe=False,
)
