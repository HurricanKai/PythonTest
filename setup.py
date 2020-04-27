import setuptools

from version import get_version

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-pkg-Kai-Jellinghaus",  # Replace with your own username
    version=get_version(pep440=True),
    author="Kai-Jellinghaus",
    author_email="contact@kaij.tech",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HurricanKai/PythonTest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
